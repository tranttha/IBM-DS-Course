# IBM-DS-Course
## Purpose: Repo containing notes, coursework, assingments and projects 
## Tools used will be updated here:
1. Python 3.10
2. Jupyter
3. R-base=3.5

## env setup (very tiresome, had no exp in setting up config from scratch):
0. config from terminal of main
1. Create & activate new Conda Environment:
# conda **create --name** *name of the env*
conda create --name ibm_ds_env python=3.10
# conda activate *name of the env*
conda activate ibm_ds_env
2. Install Python librabries:
pip install numpy pandas matplotlib seaborn scikit-learn jupyter notebook
3. Install R and R Essentials:
- Add the R channel to Conda (if not already added):
conda config --add channels r
- Install R and R essentials:
conda install r-base=3.5
conda install r-essentials=3.5.0
**It seems that the conda install r-base=3.5 command is going to downgrade several packages, including Python and OpenSSL. This is because r-base 3.5 has dependencies that are not fully compatible with the newer versions of these packages.**
Hence:
conda install r-base=4.3.1
conda install r-essentials
conda install -c r r-ggplot2 r-dplyr r-tidyr r-shiny r-plotly r-data.table r-stringr

## Saving config:
If changes are made to your env: installing or updating packages,..., should commit these changes to version control so that you can track changes, share setup, or revert if needed.
1. Update environment.yml:
- Export Environment:
conda env export --no-builds > environment.yml
2. Check the environment.yml File:
3. Commit Changes:
git add environment.yml
git commit -m *commit msg*


## Results 
*check list of current config with ***conda list*** 
(ibm_ds_env) @tranttha ➜ /workspaces/IBM-DS-Course (main) $ conda list
# packages in environment at /opt/conda/envs/ibm_ds_env:
#
# Name                    Version                   Build  Channel
_libgcc_mutex             0.1                        main  
_openmp_mutex             5.1                       1_gnu  
_r-mutex                  1.0.0               anacondar_1    r
_sysroot_linux-64_curr_repodata_hack 3                   haa98f57_10  
anyio                     4.2.0           py310h06a4308_0  
argon2-cffi               21.3.0             pyhd3eb1b0_0  
argon2-cffi-bindings      21.2.0          py310h7f8727e_0  
asttokens                 2.0.5              pyhd3eb1b0_0  
async-lru                 2.0.4           py310h06a4308_0  
attrs                     23.1.0          py310h06a4308_0  
babel                     2.11.0          py310h06a4308_0  
beautifulsoup4            4.12.3          py310h06a4308_0  
binutils_impl_linux-64    2.38                 h2a08ee3_1  
binutils_linux-64         2.38.0               hc2dff05_0  
blas                      1.0                    openblas  
bleach                    4.1.0              pyhd3eb1b0_0  
brotli-python             1.0.9           py310h6a678d5_8  
bwidget                   1.9.16               h9eba36c_0  
bzip2                     1.0.8                h5eee18b_6  
c-ares                    1.19.1               h5eee18b_0  
ca-certificates           2024.7.2             h06a4308_0  
cairo                     1.16.0               hb05425b_5  
certifi                   2024.7.4        py310h06a4308_0  
cffi                      1.16.0          py310h5eee18b_1  
charset-normalizer        2.0.4              pyhd3eb1b0_0  
comm                      0.2.1           py310h06a4308_0  
curl                      8.7.1                hdbd6064_0  
debugpy                   1.6.7           py310h6a678d5_0  
decorator                 5.1.1              pyhd3eb1b0_0  
defusedxml                0.7.1              pyhd3eb1b0_0  
exceptiongroup            1.2.0           py310h06a4308_0  
executing                 0.8.3              pyhd3eb1b0_0  
expat                     2.6.2                h6a678d5_0  
fontconfig                2.14.1               h4c34cd2_2  
freetype                  2.12.1               h4a9f257_0  
fribidi                   1.0.10               h7b6447c_0  
gcc_impl_linux-64         11.2.0               h1234567_1  
gcc_linux-64              11.2.0               h5c386dc_0  
gfortran_impl_linux-64    11.2.0               h1234567_1  
gfortran_linux-64         11.2.0               hc2dff05_0  
glib                      2.78.4               h6a678d5_0  
glib-tools                2.78.4               h6a678d5_0  
graphite2                 1.3.14               h295c915_1  
gxx_impl_linux-64         11.2.0               h1234567_1  
gxx_linux-64              11.2.0               hc2dff05_0  
harfbuzz                  4.3.0                hf52aaf7_2  
icu                       73.1                 h6a678d5_0  
idna                      3.7             py310h06a4308_0  
ipykernel                 6.28.0          py310h06a4308_0  
ipython                   8.25.0          py310h06a4308_0  
ipywidgets                8.1.3                    pypi_0    pypi
jedi                      0.18.1          py310h06a4308_1  
jinja2                    3.1.4           py310h06a4308_0  
jpeg                      9e                   h5eee18b_1  
json5                     0.9.6              pyhd3eb1b0_0  
jsonschema                4.19.2          py310h06a4308_0  
jsonschema-specifications 2023.7.1        py310h06a4308_0  
jupyter                   1.0.0                    pypi_0    pypi
jupyter-console           6.6.3                    pypi_0    pypi
jupyter-lsp               2.2.0           py310h06a4308_0  
jupyter_client            8.6.0           py310h06a4308_0  
jupyter_core              5.7.2           py310h06a4308_0  
jupyter_events            0.10.0          py310h06a4308_0  
jupyter_server            2.14.1          py310h06a4308_0  
jupyter_server_terminals  0.4.4           py310h06a4308_1  
jupyterlab                4.0.11          py310h06a4308_0  
jupyterlab-widgets        3.0.11                   pypi_0    pypi
jupyterlab_pygments       0.1.2                      py_0  
jupyterlab_server         2.25.1          py310h06a4308_0  
kernel-headers_linux-64   3.10.0              h57e8cba_10  
krb5                      1.20.1               h143b758_1  
ld_impl_linux-64          2.38                 h1181459_1  
lerc                      3.0                  h295c915_0  
libcurl                   8.7.1                h251f7ec_0  
libdeflate                1.17                 h5eee18b_1  
libedit                   3.1.20230828         h5eee18b_0  
libev                     4.33                 h7f8727e_1  
libffi                    3.4.4                h6a678d5_1  
libgcc-devel_linux-64     11.2.0               h1234567_1  
libgcc-ng                 11.2.0               h1234567_1  
libgfortran-ng            11.2.0               h00389a5_1  
libgfortran5              11.2.0               h1234567_1  
libglib                   2.78.4               hdc74915_0  
libgomp                   11.2.0               h1234567_1  
libiconv                  1.16                 h5eee18b_3  
libnghttp2                1.57.0               h2d74bed_0  
libopenblas               0.3.21               h043d6bf_0  
libpng                    1.6.39               h5eee18b_0  
libsodium                 1.0.18               h7b6447c_0  
libssh2                   1.11.0               h251f7ec_0  
libstdcxx-devel_linux-64  11.2.0               h1234567_1  
libstdcxx-ng              11.2.0               h1234567_1  
libtiff                   4.5.1                h6a678d5_0  
libuuid                   1.41.5               h5eee18b_0  
libwebp-base              1.3.2                h5eee18b_0  
libxcb                    1.15                 h7f8727e_0  
libxml2                   2.10.4               hfdd30dd_2  
lz4-c                     1.9.4                h6a678d5_1  
make                      4.2.1                h1bed415_1  
markupsafe                2.1.3           py310h5eee18b_0  
matplotlib-inline         0.1.6           py310h06a4308_0  
mistune                   2.0.4           py310h06a4308_0  
nbclient                  0.8.0           py310h06a4308_0  
nbconvert                 7.10.0          py310h06a4308_0  
nbformat                  5.9.2           py310h06a4308_0  
ncurses                   6.4                  h6a678d5_0  
nest-asyncio              1.6.0           py310h06a4308_0  
notebook                  7.2.1                    pypi_0    pypi
notebook-shim             0.2.3           py310h06a4308_0  
openssl                   3.0.14               h5eee18b_0  
overrides                 7.4.0           py310h06a4308_0  
packaging                 24.1            py310h06a4308_0  
pandoc                    2.12                 h06a4308_3  
pandocfilters             1.5.0              pyhd3eb1b0_0  
pango                     1.50.7               h05da053_0  
parso                     0.8.3              pyhd3eb1b0_0  
pcre2                     10.42                hebb0a14_1  
pexpect                   4.8.0              pyhd3eb1b0_3  
pip                       24.0            py310h06a4308_0  
pixman                    0.40.0               h7f8727e_1  
platformdirs              3.10.0          py310h06a4308_0  
prometheus_client         0.14.1          py310h06a4308_0  
prompt-toolkit            3.0.43          py310h06a4308_0  
prompt_toolkit            3.0.43               hd3eb1b0_0  
psutil                    5.9.0           py310h5eee18b_0  
ptyprocess                0.7.0              pyhd3eb1b0_2  
pure_eval                 0.2.2              pyhd3eb1b0_0  
pycparser                 2.21               pyhd3eb1b0_0  
pygments                  2.15.1          py310h06a4308_1  
pysocks                   1.7.1           py310h06a4308_0  
python                    3.10.14              h955ad1f_1  
python-dateutil           2.9.0post0      py310h06a4308_2  
python-fastjsonschema     2.16.2          py310h06a4308_0  
python-json-logger        2.0.7           py310h06a4308_0  
pytz                      2024.1          py310h06a4308_0  
pyyaml                    6.0.1           py310h5eee18b_0  
pyzmq                     25.1.2          py310h6a678d5_0  
qtconsole                 5.5.2                    pypi_0    pypi
qtpy                      2.4.1                    pypi_0    pypi
r-askpass                 1.2.0             r43h76d94ec_0    r
r-backports               1.4.1             r43h76d94ec_0    r
r-base                    4.3.1                h1ae530e_0    r
r-base64enc               0.1_3             r43h76d94ec_4    r
r-bit                     4.0.5             r43h76d94ec_0    r
r-bit64                   4.0.5             r43h76d94ec_0    r
r-blob                    1.2.4             r43h6115d3f_0  
r-boot                    1.3_28.1          r43h6115d3f_0  
r-broom                   1.0.5             r43h6115d3f_0  
r-bslib                   0.5.1             r43h6115d3f_0  
r-cachem                  1.0.8             r43h76d94ec_0    r
r-callr                   3.7.3             r43h6115d3f_0  
r-caret                   6.0_94            r43h76d94ec_0    r
r-cellranger              1.1.0             r43h6115d3f_0  
r-class                   7.3_22            r43h76d94ec_0    r
r-cli                     3.6.1             r43h884c59f_0    r
r-clipr                   0.8.0             r43h6115d3f_0  
r-clock                   0.7.0             r43h884c59f_0    r
r-cluster                 2.1.4             r43h640688f_0    r
r-codetools               0.2_19            r43h6115d3f_0  
r-colorspace              2.1_0             r43h76d94ec_0    r
r-commonmark              1.9.0             r43h76d94ec_0    r
r-conflicted              1.2.0             r43h142f84f_0  
r-cpp11                   0.4.6             r43h6115d3f_0  
r-crayon                  1.5.2             r43h6115d3f_0  
r-crosstalk               1.2.0             r43h6115d3f_0  
r-curl                    5.1.0             r43h76d94ec_0    r
r-data.table              1.14.8            r43h76d94ec_0    r
r-dbi                     1.1.3             r43h6115d3f_0  
r-dbplyr                  2.3.4             r43h6115d3f_0  
r-diagram                 1.6.5             r43h6115d3f_0  
r-digest                  0.6.33            r43h884c59f_0    r
r-dplyr                   1.1.3             r43h884c59f_0    r
r-dtplyr                  1.3.1             r43h6115d3f_0  
r-e1071                   1.7_13            r43h884c59f_0    r
r-ellipsis                0.3.2             r43h76d94ec_0    r
r-essentials              4.3.1                     r43_0    r
r-evaluate                0.22              r43h6115d3f_0  
r-fansi                   1.0.5             r43h76d94ec_0    r
r-farver                  2.1.1             r43h884c59f_0    r
r-fastmap                 1.1.1             r43h884c59f_0    r
r-fontawesome             0.5.2             r43h6115d3f_0  
r-forcats                 1.0.0             r43h6115d3f_0  
r-foreach                 1.5.2             r43h6115d3f_0  
r-foreign                 0.8_85            r43h76d94ec_0    r
r-formatr                 1.14              r43h6115d3f_0  
r-fs                      1.6.3             r43h884c59f_0    r
r-future                  1.33.0            r43h6115d3f_0  
r-future.apply            1.11.0            r43h6115d3f_0  
r-gargle                  1.5.2             r43h142f84f_0  
r-generics                0.1.3             r43h142f84f_0  
r-ggplot2                 3.4.4             r43h6115d3f_0  
r-glmnet                  4.1_8             r43hb5eb8f6_0    r
r-globals                 0.16.2            r43h142f84f_0  
r-glue                    1.6.2             r43h76d94ec_0    r
r-googledrive             2.1.1             r43h6115d3f_0  
r-googlesheets4           1.1.1             r43h6115d3f_0  
r-gower                   1.0.1             r43h76d94ec_0    r
r-gtable                  0.3.4             r43h6115d3f_0  
r-hardhat                 1.3.0             r43h6115d3f_0  
r-haven                   2.5.3             r43h884c59f_0    r
r-highr                   0.10              r43h6115d3f_0  
r-hms                     1.1.3             r43h6115d3f_0  
r-htmltools               0.5.6.1           r43h76d94ec_0    r
r-htmlwidgets             1.6.2             r43h6115d3f_0  
r-httpuv                  1.6.11            r43h884c59f_0    r
r-httr                    1.4.7             r43h6115d3f_0  
r-ids                     1.0.1             r43h142f84f_0  
r-ipred                   0.9_14            r43h76d94ec_0    r
r-irdisplay               1.1               r43h6115d3f_0  
r-irkernel                1.3.2                     r43_0  
r-isoband                 0.2.7             r43h884c59f_0    r
r-iterators               1.0.14            r43h6115d3f_0  
r-jquerylib               0.1.4             r43h6115d3f_0  
r-jsonlite                1.8.7             r43h76d94ec_0    r
r-kernsmooth              2.23_22           r43h640688f_0    r
r-knitr                   1.44              r43h6115d3f_0  
r-labeling                0.4.3             r43h6115d3f_0  
r-later                   1.3.1             r43h884c59f_0    r
r-lattice                 0.21_9            r43h76d94ec_0    r
r-lava                    1.7.2.1           r43h6115d3f_0  
r-lazyeval                0.2.2             r43h76d94ec_0    r
r-lifecycle               1.0.3             r43h142f84f_0  
r-listenv                 0.9.0             r43h142f84f_0  
r-lubridate               1.9.3             r43h76d94ec_0    r
r-magrittr                2.0.3             r43h76d94ec_0    r
r-mass                    7.3_60            r43h76d94ec_0    r
r-matrix                  1.6_1.1           r43h76d94ec_0    r
r-memoise                 2.0.1             r43h6115d3f_0  
r-mgcv                    1.9_0             r43h76d94ec_0    r
r-mime                    0.12              r43h76d94ec_0    r
r-modelmetrics            1.2.2.2           r43h884c59f_0    r
r-modelr                  0.1.11            r43h6115d3f_0  
r-munsell                 0.5.0             r43h6115d3f_0  
r-nlme                    3.1_163           r43h640688f_0    r
r-nnet                    7.3_19            r43h76d94ec_0    r
r-numderiv                2016.8_1.1        r43h6115d3f_0  
r-openssl                 2.1.1             r43h76d94ec_0    r
r-parallelly              1.36.0            r43h6115d3f_0  
r-pbdzmq                  0.3_10            r43h884c59f_0    r
r-pillar                  1.9.0             r43h6115d3f_0  
r-pkgconfig               2.0.3             r43h6115d3f_0  
r-plotly                  4.10.2            r43h6115d3f_0  
r-plyr                    1.8.9             r43h884c59f_0    r
r-prettyunits             1.2.0             r43h142f84f_0  
r-proc                    1.18.4            r43h884c59f_0    r
r-processx                3.8.2             r43h76d94ec_0    r
r-prodlim                 2023.08.28        r43h884c59f_0    r
r-progress                1.2.2             r43h142f84f_0  
r-progressr               0.14.0            r43h6115d3f_0  
r-promises                1.2.1             r43h884c59f_0    r
r-proxy                   0.4_27            r43h76d94ec_0    r
r-ps                      1.7.5             r43h76d94ec_0    r
r-purrr                   1.0.2             r43h76d94ec_0    r
r-quantmod                0.4.25            r43h6115d3f_0  
r-r6                      2.5.1             r43h6115d3f_0  
r-ragg                    1.2.6             r43h884c59f_0    r
r-randomforest            4.7_1.1           r43h640688f_0    r
r-rappdirs                0.3.3             r43h76d94ec_0    r
r-rcolorbrewer            1.1_3             r43h6115d3f_1  
r-rcpp                    1.0.11            r43h884c59f_0    r
r-rcppeigen               0.3.3.9.3         r43h884c59f_0    r
r-readr                   2.1.4             r43h884c59f_0    r
r-readxl                  1.4.3             r43h884c59f_0    r
r-recipes                 1.0.8             r43h6115d3f_0  
r-recommended             4.3.1                     r43_0    r
r-rematch                 2.0.0             r43h6115d3f_0  
r-rematch2                2.1.2             r43h142f84f_0  
r-repr                    1.1.6             r43h6115d3f_0  
r-reprex                  2.0.2             r43h6115d3f_0  
r-reshape2                1.4.4             r43h884c59f_0    r
r-rlang                   1.1.1             r43h884c59f_0    r
r-rmarkdown               2.25              r43h6115d3f_0  
r-rpart                   4.1.21            r43h76d94ec_0    r
r-rstudioapi              0.15.0            r43h6115d3f_0  
r-rvest                   1.0.3             r43h6115d3f_0  
r-sass                    0.4.7             r43h884c59f_0    r
r-scales                  1.2.1             r43h6115d3f_0  
r-selectr                 0.4_2             r43h6115d3f_0  
r-shape                   1.4.6             r43h142f84f_0  
r-shiny                   1.7.5.1           r43h6115d3f_0  
r-sourcetools             0.1.7_1           r43h884c59f_0    r
r-spatial                 7.3_17            r43h76d94ec_0    r
r-squarem                 2021.1            r43h142f84f_0  
r-stringi                 1.7.12            r43h884c59f_0    r
r-stringr                 1.5.0             r43h6115d3f_0  
r-survival                3.5_7             r43h76d94ec_0    r
r-sys                     3.4.2             r43h76d94ec_0    r
r-systemfonts             1.0.5             r43h884c59f_0    r
r-textshaping             0.3.7             r43h884c59f_0    r
r-tibble                  3.2.1             r43h76d94ec_0    r
r-tidyr                   1.3.0             r43h884c59f_0    r
r-tidyselect              1.2.0             r43h6115d3f_0  
r-tidyverse               2.0.0             r43h6115d3f_0  
r-timechange              0.2.0             r43h884c59f_0    r
r-timedate                4022.108          r43h6115d3f_0  
r-tinytex                 0.48              r43h142f84f_0  
r-ttr                     0.24.3            r43h76d94ec_0    r
r-tzdb                    0.4.0             r43h884c59f_0    r
r-utf8                    1.2.4             r43h76d94ec_0    r
r-uuid                    1.1_1             r43h76d94ec_0    r
r-vctrs                   0.6.4             r43h884c59f_0    r
r-viridislite             0.4.2             r43h6115d3f_0  
r-vroom                   1.6.4             r43h884c59f_0    r
r-withr                   2.5.1             r43h6115d3f_0  
r-xfun                    0.40              r43h76d94ec_0    r
r-xml2                    1.3.5             r43h884c59f_0    r
r-xtable                  1.8_4             r43h6115d3f_0  
r-xts                     0.13.1            r43h76d94ec_0    r
r-yaml                    2.3.7             r43h76d94ec_0    r
r-zoo                     1.8_12            r43h76d94ec_0    r
readline                  8.2                  h5eee18b_0  
referencing               0.30.2          py310h06a4308_0  
requests                  2.32.2          py310h06a4308_0  
rfc3339-validator         0.1.4           py310h06a4308_0  
rfc3986-validator         0.1.1           py310h06a4308_0  
rpds-py                   0.10.6          py310hb02cf49_0  
send2trash                1.8.2           py310h06a4308_0  
setuptools                69.5.1          py310h06a4308_0  
six                       1.16.0             pyhd3eb1b0_1  
sniffio                   1.3.0           py310h06a4308_0  
soupsieve                 2.5             py310h06a4308_0  
sqlite                    3.45.3               h5eee18b_0  
stack_data                0.2.0              pyhd3eb1b0_0  
sysroot_linux-64          2.17                h57e8cba_10  
terminado                 0.17.1          py310h06a4308_0  
tinycss2                  1.2.1           py310h06a4308_0  
tk                        8.6.14               h39e8969_0  
tktable                   2.10                 h3d55465_1  
tomli                     2.0.1           py310h06a4308_0  
tornado                   6.4.1           py310h5eee18b_0  
traitlets                 5.14.3          py310h06a4308_0  
typing-extensions         4.11.0          py310h06a4308_0  
typing_extensions         4.11.0          py310h06a4308_0  
tzdata                    2024a                h04d1e81_0  
urllib3                   2.2.2           py310h06a4308_0  
wcwidth                   0.2.5              pyhd3eb1b0_0  
webencodings              0.5.1           py310h06a4308_1  
websocket-client          1.8.0           py310h06a4308_0  
wheel                     0.43.0          py310h06a4308_0  
widgetsnbextension        4.0.11                   pypi_0    pypi
xz                        5.4.6                h5eee18b_1  
yaml                      0.2.5                h7b6447c_0  
zeromq                    4.3.5                h6a678d5_0  
zlib                      1.2.13               h5eee18b_1  
zstd                      1.5.5                hc292b87_2  