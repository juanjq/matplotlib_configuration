import matplotlib.pyplot as plt

def params():   
    #fontsize
    plt.rcParams['font.size'] = 18   
    #figure size
    plt.rcParams['figure.figsize'] = 16,9    
    #LaTex font
    plt.rcParams['mathtext.fontset'] = 'custom'
    plt.rcParams['mathtext.rm'] = 'Bitstream Vera Sans'
    plt.rcParams['mathtext.it'] = 'Bitstream Vera Sans:italic'
    plt.rcParams['mathtext.bf'] = 'Bitstream Vera Sans:bold'
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['font.family'] = 'STIXGeneral'
    #ticks
    plt.rcParams["xtick.direction"] = "in"
    plt.rcParams["ytick.direction"] = "in"
    plt.rcParams['xtick.top'] = True
    plt.rcParams['ytick.right'] = True
    plt.rcParams['xtick.minor.visible'] = True
    plt.rcParams['ytick.minor.visible'] = True
    plt.rcParams['xtick.major.size'] = 8
    plt.rcParams['xtick.major.width'] = 2
    plt.rcParams['xtick.minor.size'] = 5
    plt.rcParams['xtick.minor.width'] = 1
    plt.rcParams['ytick.major.size'] = 8
    plt.rcParams['ytick.major.width'] = 2
    plt.rcParams['ytick.minor.size'] = 5
    plt.rcParams['ytick.minor.width'] = 1
    #figure
    plt.rcParams['figure.facecolor'] = 'w'
    plt.rcParams['figure.frameon'] = False
    plt.rcParams['figure.dpi'] = 200
    plt.rcParams['savefig.dpi'] = 200
    plt.rcParams['savefig.format'] = 'pdf'
    plt.rcParams['savefig.transparent'] = True
    plt.rcParams['figure.dpi'] = 100
    #errorbars
    plt.rcParams['errorbar.capsize'] = 3
    #histograms
    plt.rcParams['hist.bins'] = 30
    #lines
    plt.rcParams['lines.linewidth'] = 1
    plt.rcParams['lines.marker'] = None
    #axes
    plt.rcParams['axes.facecolor'] ='w'
    plt.rcParams['axes.edgecolor'] ='k'
    plt.rcParams['axes.linewidth'] =1
    plt.rcParams['axes.titlesize'] = 18
    plt.rcParams['axes.labelsize'] = 18
    plt.rcParams['axes.labelcolor'] = 'k'
    #grid
    plt.rcParams['axes.grid'] =False
    plt.rcParams['grid.color'] ='k'
    plt.rcParams['grid.linestyle'] ='-'
    plt.rcParams['grid.linewidth'] =0.5
    plt.rcParams['grid.alpha'] =1
    #legend
    plt.rcParams['legend.fancybox'] =True
    plt.rcParams['legend.fontsize'] =17
    plt.rcParams['legend.markerscale'] =1.5
    #colors
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=[
        'darkblue','darkviolet','deeppink','crimson','orangered','darkorange','sandybrown','gold','yellow'])

def simple():   
    plt.rcParams['mathtext.fontset'] = 'custom'
    plt.rcParams['mathtext.rm'] = 'Bitstream Vera Sans'
    plt.rcParams['mathtext.it'] = 'Bitstream Vera Sans:italic'
    plt.rcParams['mathtext.bf'] = 'Bitstream Vera Sans:bold'
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['font.family'] = 'STIXGeneral'
   
    plt.rcParams['savefig.format'] = 'pdf'
    plt.rcParams['savefig.transparent'] = True
    plt.rcParams['figure.dpi'] = 100
   
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=[
        'darkblue','darkviolet','deeppink','crimson','orangered','darkorange','sandybrown','gold','yellow'])
        
    
    
    
def default():
    plt.rcParams.update(plt.rcParamsDefault)

with   plt.rc_context( rc={'font.size':20,
                           'figure.figsize':(16,9) ,
                            #LaTex font
                            'mathtext.fontset' : 'custom',
                            'mathtext.rm' : 'Bitstream Vera Sans',
                            'mathtext.it' : 'Bitstream Vera Sans:italic',
                            'mathtext.bf' : 'Bitstream Vera Sans:bold',
                            'mathtext.fontset' : 'stix',
                            'font.family' : 'STIXGeneral',
                            #ticks
                            'xtick.direction' : 'in',
                            'ytick.direction' : 'in',
                            'xtick.top' : True,
                            'ytick.right' : True,
                            'xtick.minor.visible' : True,
                            'ytick.minor.visible' : True,
                            'xtick.major.size' : 8,
                            'xtick.major.width' : 2,
                            'xtick.minor.size' : 5,
                            'xtick.minor.width' : 1,
                            'ytick.major.size' : 8,
                            'ytick.major.width' : 2,
                            'ytick.minor.size' : 5,
                            'ytick.minor.width' : 1,
                            #figure
                            'figure.facecolor' : 'w',
                            'figure.frameon' : False,
                            'figure.dpi' : 200,
                            'savefig.dpi' : 200,
                            'savefig.format' : 'pdf',
                            'savefig.transparent' : True,
                            'figure.dpi' : 100,
                            #errorbars
                            'errorbar.capsize' : 3,
                            #histograms
                            'hist.bins' : 30,
                            #lines
                            'lines.linewidth' : 1,
                            'lines.marker' : None,
                            #axes
                            'axes.facecolor' :'w',
                            'axes.edgecolor' :'k',
                            'axes.linewidth' :1,
                            'axes.titlesize' : 18,
                            'axes.labelsize' : 18,
                            'axes.labelcolor' : 'k',
                            #grid
                            'axes.grid' :False,
                            'grid.color' :'k',
                            'grid.linestyle' :'-',
                            'grid.linewidth' :0.5,
                            'grid.alpha' :1,
                            #legend
                            'legend.fancybox' :True,
                            'legend.fontsize' :17,
                            'legend.markerscale' :1.5,
                            #colors
                            'axes.prop_cycle' : plt.cycler(color=
                                                           ['darkblue','darkviolet','deeppink','crimson','orangered','darkorange','sandybrown','gold','yellow']) }):
    
    
    pass
