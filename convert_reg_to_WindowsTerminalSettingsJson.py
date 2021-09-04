#!/usr/bin/env python3
import re
import sys
import os
import json


clrnmap = {
    # CSI FG BG
    0: 'foreground',
    1: None,
    2: 'background',
    3: 'selectionBackground',
    4: None,
    5: 'cursorColor',
    # 16 colors
    6: 'black',
    7: 'brightBlack',
    8: 'red',
    9: 'brightRed',
    10: 'green',
    11: 'brightGreen',
    12: 'yellow',
    13: 'brightYellow',
    14: 'blue',
    15: 'brightBlue',
    16: 'purple',
    17: 'brightPurple',
    18: 'cyan',
    19: 'brightCyan',
    20: 'white',
    21: 'brightWhite',
}


def main():
    """
    copy output json to "%LocalAppData%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json"
    """
    input_fname = '46. Tomorrow Night.reg'
    input_fname = sys.argv[1] if len(sys.argv) > 1 else input_fname
    ret = {"name": os.path.splitext(input_fname)[0], }
    with open(input_fname) as fin:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            if not line.startswith('"Colour'):
                continue
            ci = re.findall(r'Colour(\d+)', line)[0]
            ci = int(ci)
            cname = clrnmap[ci]
            if not cname:
                continue
            rgb = line.split('=')[-1].strip('"').split(',')
            ret[cname] = '#' + ''.join(map(lambda x: f'{int(x):02X}', rgb))

    output_fname = os.path.splitext(input_fname)[0] + '.json'
    with open(output_fname, 'w') as fout:
        json.dump(ret, fout, indent=2)


if __name__ == '__main__':
    main()
