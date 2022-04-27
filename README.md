# matplotlib_configuration
A script to use matplotlib configurations.

For installing it you can do:

```
import httpimport
with httpimport.remote_repo(['plt_config'], 'https://raw.githubusercontent.com/juanjq/matplotlib_configuration/main'):
     import plt_config 
```

And we have different options to use it,

# `simple(n)`
A simple configuration but with some features that the default version do not have. As LaTex text, textsize changing and colors.

* `n` is the textsize

# `complex(n)`
A more complex configuration of matplotlib With things as LaTex text, personalized ticks, colors and etc.

* `n` is the textsize
*
# `default()`
The default configuration of matplotlib.
