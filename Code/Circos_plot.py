
from pycirclize import Circos
import pandas as pd
import os

BED_PATH = ''
QTL_PATH = ''
GENE_PATH = ''
EFFECT_PATH = ''
INTERACTION_PATH = ''
SAVE_PATH = ''

MODEL = ['rrBLUP','BayesB','RKHS','RF','SVR','GAT','ensemble-naive']

 # a list of colours corresponding to each keyword
CYTOBAND_COLORMAP = {   
    "gpos100": "#000000",  # 0,0,0
    "gpos": "#000000",  # 0,0,0
    "gpos75": "#828282",  # 130,130,130
    "gpos66": "#A0A0A0",  # 160,160,160
    "gpos50": "#C8C8C8",  # 200,200,200
    "gpos33": "#D2D2D2",  # 210,210,210
    "gpos25": "#C8C8C8",  # 200,200,200
    "gvar": "#DCDCDC",  # 220,220,220
    "gneg": "#FFFFFF",  # 255,255,255
    "acen": "#D92F27",  # 217,47,39
    "stalk": "#647FA4",  # 100,127,164
    "green": "#47c462",
    "brown": "#e0a22f",
    "purple": "#a62bcc",
    "blue1": "#def2ff",
    "blue2": "#c2e5fc",
    "blue3": "#addeff",
    "blue4": "#99d6ff",
    "blue5": "#83ccfc",
    "blue6": "#68c1fc",
    "blue7": "#45b5ff",
    "blue8": "#14a0fc",
    "blue9": "#027ac9",
    "blue10": "#014f82",
    "red1": "#fce1a7",
    "red2": "#ffd780",
    "red3": "#ffc954",
    "red4": "#fcba2b",
    "red5": "#ffaf03",
    "red6": "#d99502",
    "red7": "#b57c02",
    "red8": "#8a5e01",
    "red9": "#874001",
    "red10": "#610901"
}

SPACE = 3  # This determines the space between rings (setors)
START = 20 # This decides from which angle you want to start making a ring (0-360 degree)
END = 340 # This decides from which angle you want to end making a ring (0-360 degree). Making space for adding a text (space for 40 degree)

cnt = 0 # This adjusts the radius of rings

# Create a frame for rings (decides the lenght of eahc chromosome)
os.chdir(BED_PATH)
circos = Circos.initialize_from_bed("FILE.bed", space=SPACE, start=START, end=END)


# Create the rings showing genomic marker effects
for i in range(len(MODEL)):  # Change here for iteration
    circos.add_cytoband_tracks((97-(3*cnt), 100-(3*cnt)), 'FILE.tsv',track_name='add a name here', cytoband_cmap=CYTOBAND_COLORMAP)
    circos.text('add a name here', r=circos.tracks[-1].r_center-2, deg=0, size=8, color="black")
    cnt+=1
    
# Create the ring showing QTLs
os.chdir(QTL_PATH)
circos.add_cytoband_tracks((97-(3*cnt), 100-(3*cnt)), 'P-value_FILE.tsv',track_name='add a name here', cytoband_cmap=CYTOBAND_COLORMAP)
circos.text('add a name here', r=circos.tracks[-1].r_center-2, deg=0, size=8, color="black")
cnt+=1

# Create the ring showing key gene regions
os.chdir(GENE_PATH)
circos.add_cytoband_tracks((97-(3*cnt), 100-(3*cnt)), 'prior-knowledge_FILE.tsv', track_name='add a name here', cytoband_cmap=CYTOBAND_COLORMAP)
circos.text('add a name here', r=circos.tracks[-1].r_center-2, deg=0, size=8, color="black")
cnt+=1

# Add ticks to the outermost ring
for sector in circos.sectors:
    sector.text(sector.name, r=120, size=10)
    sector.get_track('put name of the outermost ring here').xticks_by_interval(
        #1000000,
        label_size=8,
        label_orientation="vertical",
        #label_formatter=lambda v: f"{v / 100000:.0f} cM",
    )

# Add interactions
os.chdir(INTERACTION_PATH)
interactions = pd.read_csv('interaction_FILE.csv')
for ii in range(interactions.shape[0]):
    region1 = (interactions.iloc[ii,0], interactions.iloc[ii,1], interactions.iloc[ii,2])
    region2 = (interactions.iloc[ii,3], interactions.iloc[ii,4], interactions.iloc[ii,5])
    if interactions.iloc[ii,0] != interactions.iloc[ii,3]:   #within chromosome or between chromosome
        colour = 'blue'
    else:
        colour = 'red'
    circos.link(region1, region2, lw=interactions.loc[ii,'value'], color=colour)

# Store the figure
fig = circos.plotfig()

os.chdir(SAVE_PATH)
fig.savefig('FILE_NAME.png',dpi=300)  
