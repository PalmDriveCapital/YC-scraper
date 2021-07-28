import argparse

def command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument('-S21', '--Summer21', action='store_true', 
        help="shows output")
    parser.add_argument('-W21', '--Winter21', action='store_true', 
        help="shows output")
    parser.add_argument('-S20', '--Summer20', action='store_true', 
        help="shows output")
    parser.add_argument('-W20', '--Winter20', action='store_true', 
        help="shows output")
    parser.add_argument('-S19', '--Summer19', action='store_true', 
        help="shows output")
    parser.add_argument('-W19', '--Winter19', action='store_true', 
        help="shows output")
    parser.add_argument('-S18', '--Summer18', action='store_true', 
        help="shows output")
    parser.add_argument('-W18', '--Winter18', action='store_true', 
        help="shows output")
    parser.add_argument('-S17', '--Summer17', action='store_true', 
        help="shows output")
    parser.add_argument('-W17', '--Winter17', action='store_true', 
        help="shows output")
    parser.add_argument('-IK12', '--ImagineK12', action='store_true', 
        help="shows output")
    parser.add_argument('-W16', '--Winter16', action='store_true', 
        help="shows output")
    parser.add_argument('-S16', '--Summer16', action='store_true', 
        help="shows output")
    parser.add_argument('-W15', '--Winter15', action='store_true', 
        help="shows output")
    parser.add_argument('-S15', '--Summer15', action='store_true', 
        help="shows output")
    parser.add_argument('-S14', '--Summer14', action='store_true', 
        help="shows output")
    parser.add_argument('-W14', '--Winter14', action='store_true', 
        help="shows output")
    parser.add_argument('-S13', '--Summer13', action='store_true', 
        help="shows output")
    parser.add_argument('-W13', '--Winter13', action='store_true', 
        help="shows output")
    parser.add_argument('-S12', '--Summer12', action='store_true', 
        help="shows output")
    parser.add_argument('-W12', '--Winter12', action='store_true', 
        help="shows output")
    parser.add_argument('-S11', '--Summer11', action='store_true', 
        help="shows output")
    parser.add_argument('-W11', '--Winter11', action='store_true', 
        help="shows output")
    parser.add_argument('-S10', '--Summer10', action='store_true', 
        help="shows output")
    parser.add_argument('-W10', '--Winter10', action='store_true', 
        help="shows output")
    parser.add_argument('-S09', '--Summer09', action='store_true', 
        help="shows output")
    parser.add_argument('-W09', '--Winter09', action='store_true', 
        help="shows output")
    parser.add_argument('-S08', '--Summer08', action='store_true', 
        help="shows output")
    parser.add_argument('-W08', '--Winter08', action='store_true', 
        help="shows output")
    parser.add_argument('-W07', '--Winter07', action='store_true', 
        help="shows output")
    parser.add_argument('-S07', '--Summer07', action='store_true', 
        help="shows output")
    parser.add_argument('-W06', '--Winter06', action='store_true', 
        help="shows output")
    parser.add_argument('-S06', '--Summer06', action='store_true', 
        help="shows output")
    parser.add_argument('-S05', '--Summer05', action='store_true', 
        help="shows output")
    args = parser.parse_args()
    
    string = "?"
    if args.Winter21:
        string = string + "batch=W21&"
    if args.Summer21:
        string = string + "batch=S21&"
    if args.Winter20:
        string = string + "batch=W20&"
    if args.Summer20:
        string = string + "batch=S20&"
    if args.Winter19:
        string = string + "batch=W19&"
    if args.Summer19:
        string = string + "batch=S19&"
    if args.Winter19:
        string = string + "batch=W19&"
    if args.Summer18:
        string = string + "batch=S18&"
    if args.Winter18:
        string = string + "batch=W18&"
    if args.Summer17:
        string = string + "batch=S17&"
    if args.Winter17:
        string = string + "batch=W17&"
    if args.Summer16:
        string = string + "batch=S16&"
    if args.Winter16:
        string = string + "batch=w16&"
    if args.ImagineK12:
        string = string + "batch=IK21&"
    if args.Summer15:
        string = string + "batch=S15&"
    if args.Winter15:
        string = string + "batch=W15&"
    if args.Summer14:
        string = string + "batch=S14&"
    if args.Winter14:
        string = string + "batch=W14&"
    if args.Summer13:
        string = string + "batch=S13&"
    if args.Winter13:
        string = string + "batch=W13&"
    if args.Summer12:
        string = string + "batch=S12&"
    if args.Winter12:
        string = string + "batch=W12&"
    if args.Summer11:
        string = string + "batch=S11&"
    if args.Winter11:
        string = string + "batch=S11&"
    if args.Summer10:
        string = string + "batch=S10&"
    if args.Winter10:
        string = string + "batch=W10&"
    if args.Summer09:
        string = string + "batch=S09&"
    if args.Winter09:
        string = string + "batch=W09&"
    if args.Summer08:
        string = string + "batch=S08&"
    if args.Winter08:
        string = string + "batch=W08&"
    if args.Summer07:
        string = string + "batch=S07&"
    if args.Winter07:
        string = string + "batch=W07&"
    if args.Summer06:
        string = string + "batch=S06&"
    if args.Winter06:
        string = string + "batch=W06&"
    if args.Summer05:
        string = string + "batch=S05&"
    return string
