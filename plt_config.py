import matplotlib.pyplot as plt

def complex(n=18):   
    
    #fontsize
    plt.rcParams['font.size'] = n   
    
    #figure size
    plt.rcParams['figure.figsize'] = 16,9    
    
    #LaTex font
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['font.family']      = 'STIXGeneral'
    plt.rcParams['mathtext.rm']      = 'Bitstream Vera Sans'
    plt.rcParams['mathtext.it']      = 'Bitstream Vera Sans:italic'
    plt.rcParams['mathtext.bf']      = 'Bitstream Vera Sans:bold'
    
    #ticks
    plt.rcParams["xtick.direction"]     = "in"
    plt.rcParams["ytick.direction"]     = "in"
    plt.rcParams['xtick.top']           = True
    plt.rcParams['ytick.right']         = True
    plt.rcParams['xtick.minor.visible'] = True
    plt.rcParams['ytick.minor.visible'] = True
    plt.rcParams['xtick.major.size']    = 8
    plt.rcParams['xtick.major.width']   = 2
    plt.rcParams['xtick.minor.size']    = 5
    plt.rcParams['xtick.minor.width']   = 1
    plt.rcParams['ytick.major.size']    = 8
    plt.rcParams['ytick.major.width']   = 2
    plt.rcParams['ytick.minor.size']    = 5
    plt.rcParams['ytick.minor.width']   = 1
    
    #figure
    plt.rcParams['figure.facecolor']    = 'w'
    plt.rcParams['figure.frameon']      = False
    plt.rcParams['figure.dpi']          = 200
    plt.rcParams['savefig.dpi']         = 200
    plt.rcParams['savefig.format']      = 'pdf'
    plt.rcParams['savefig.transparent'] = True
    plt.rcParams['figure.dpi']          = 100
    
    #errorbars
    plt.rcParams['errorbar.capsize'] = 3
    
    #histograms
    plt.rcParams['hist.bins'] = 33
    
    #lines
    plt.rcParams['lines.linewidth'] = 1
    plt.rcParams['lines.marker']    = None
    
    #axes
    plt.rcParams['axes.facecolor']  = 'w'
    plt.rcParams['axes.edgecolor']  = 'k'
    plt.rcParams['axes.linewidth']  = 1
    plt.rcParams['axes.titlesize']  = 18
    plt.rcParams['axes.labelsize']  = 18
    plt.rcParams['axes.labelcolor'] = 'k'
    
    #grid
    plt.rcParams['axes.grid']      = False
    plt.rcParams['grid.color']     = 'k'
    plt.rcParams['grid.linestyle'] = '-'
    plt.rcParams['grid.linewidth'] = 0.5
    plt.rcParams['grid.alpha']     = 1
    
    #legend
    plt.rcParams['legend.fancybox']    = True
    plt.rcParams['legend.fontsize']    = 17
    plt.rcParams['legend.markerscale'] = 1.5
    
    #colors
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=[
        'darkblue','darkviolet','deeppink','crimson','orangered','darkorange','sandybrown','gold','yellow'])

def simple(n=18):   
    
    #fontsize
    plt.rcParams['font.size'] = n   
    
    #LaTex font   
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['font.family']      = 'STIXGeneral'
    plt.rcParams['mathtext.rm']      = 'Bitstream Vera Sans'
    plt.rcParams['mathtext.it']      = 'Bitstream Vera Sans:italic'
    plt.rcParams['mathtext.bf']      = 'Bitstream Vera Sans:bold'
   
    #figure
    plt.rcParams['savefig.format'] = 'pdf'
    plt.rcParams['figure.dpi']     = 100
    
    #histograms
    plt.rcParams['hist.bins'] = 30
    
    #errorbars
    plt.rcParams['errorbar.capsize'] = 3   
   
    #colors
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=[
        'darkblue','darkviolet','deeppink','crimson','orangered','darkorange','sandybrown','gold','yellow'])
        
    
    
def default():
    plt.rcParams.update(plt.rcParamsDefault)

#for use a configuration without changing the before configuration that is used:
'''
with   plt.rc_context( rc={    
    #fontsize
    plt.rcParams['font.size'] = n   
    
    #figure size
    plt.rcParams['figure.figsize'] = 16,9    
    
    #LaTex font
    plt.rcParams['mathtext.fontset'] = 'stix'
    plt.rcParams['font.family']      = 'STIXGeneral'
    plt.rcParams['mathtext.rm']      = 'Bitstream Vera Sans'
    plt.rcParams['mathtext.it']      = 'Bitstream Vera Sans:italic'
    plt.rcParams['mathtext.bf']      = 'Bitstream Vera Sans:bold'
    
    #ticks
    plt.rcParams["xtick.direction"]     = "in"
    plt.rcParams["ytick.direction"]     = "in"
    plt.rcParams['xtick.top']           = True
    plt.rcParams['ytick.right']         = True
    plt.rcParams['xtick.minor.visible'] = True
    plt.rcParams['ytick.minor.visible'] = True
    plt.rcParams['xtick.major.size']    = 8
    plt.rcParams['xtick.major.width']   = 2
    plt.rcParams['xtick.minor.size']    = 5
    plt.rcParams['xtick.minor.width']   = 1
    plt.rcParams['ytick.major.size']    = 8
    plt.rcParams['ytick.major.width']   = 2
    plt.rcParams['ytick.minor.size']    = 5
    plt.rcParams['ytick.minor.width']   = 1
    
    #figure
    plt.rcParams['figure.facecolor']    = 'w'
    plt.rcParams['figure.frameon']      = False
    plt.rcParams['figure.dpi']          = 200
    plt.rcParams['savefig.dpi']         = 200
    plt.rcParams['savefig.format']      = 'pdf'
    plt.rcParams['savefig.transparent'] = True
    plt.rcParams['figure.dpi']          = 100
    
    #errorbars
    plt.rcParams['errorbar.capsize'] = 3
    
    #histograms
    plt.rcParams['hist.bins'] = 33
    
    #lines
    plt.rcParams['lines.linewidth'] = 1
    plt.rcParams['lines.marker']    = None
    
    #axes
    plt.rcParams['axes.facecolor']  = 'w'
    plt.rcParams['axes.edgecolor']  = 'k'
    plt.rcParams['axes.linewidth']  = 1
    plt.rcParams['axes.titlesize']  = 18
    plt.rcParams['axes.labelsize']  = 18
    plt.rcParams['axes.labelcolor'] = 'k'
    
    #grid
    plt.rcParams['axes.grid']      = False
    plt.rcParams['grid.color']     = 'k'
    plt.rcParams['grid.linestyle'] = '-'
    plt.rcParams['grid.linewidth'] = 0.5
    plt.rcParams['grid.alpha']     = 1
    
    #legend
    plt.rcParams['legend.fancybox']    = True
    plt.rcParams['legend.fontsize']    = 17
    plt.rcParams['legend.markerscale'] = 1.5
    
    #colors
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=[
        'darkblue','darkviolet','deeppink','crimson','orangered','darkorange','sandybrown','gold','yellow']) }):
    
    pass
'''
