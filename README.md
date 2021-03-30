<p align="center">
<img src="https://camo.githubusercontent.com/13c4e50d88df7178ae1882a203ed57b641674f94/68747470733a2f2f63646e2e7261776769742e636f6d2f73696e647265736f726875732f617765736f6d652f643733303566333864323966656437386661383536353265336136336531353464643865383832392f6d656469612f62616467652e737667">
</p>

<h1 align="center"> HACS CLI</h1>

<p align="center" style="display: flex; flex-direction: row; align-content: center; justify-content: center; ">
  <img width="460" height="300"  src="https://hacs.xyz/img/hacs-logo.svg" >

</p>

# HACS CLI

```bash
> hacs-cli -h

usage: hacs-cli

Hacs CLI

positional arguments:
  {integrations,themes,plugins,pythonscripts,netdaemon,appdaemon}

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -c CONFIG, --config CONFIG Path for your config homeassistant
```

## Install

```bash
    \
    git clone https://github.com/jadson179/hacs-cli.git && cd hacs-cli \
    && pip3 install -r requirements.txt \
    && pyinstaller --onefile __main__.py -n hacs-cli && sudo mv ./dist/hacs-cli /usr/local/bin
```

## Autor 

<table>
  <tr>
    <td align="center"><a href="https://github.com/jadson179"><img src="https://avatars0.githubusercontent.com/u/42282908?s=460&u=79ce909209ebf14da91a2d2517c9b0f9e378a4e1&v=4" width="100px;" alt=""/><br /><sub><b>Jadson Santos</b></sub></a><br /><a href="https://github.com/jadson179/hacs-cli/commits?author=jadson179" title="Code">💻</a> <a href="https://github.com/jadson179" title="Design">🎨</a></td>
  <tr>
</table>


## License

MIT License

Copyright (c) 2020 Jadson Santos

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
