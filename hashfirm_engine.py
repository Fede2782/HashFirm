#!/usr/bin/env python3.13
#
# Copyright (C) 2024 Fede2782
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from sys import argv as args

def seq_gen(sq: list[str], start: str, end: str) -> list[str]:
    lenght: int = len(seq)

    if start not in sq:
        raise ValueError("Start not found in given sequence")
    
    if end not in sq:
        raise ValueError("End not found in given sequence")
    
    pos_start: int = sq.index(start.upper())
    pos_end: int = sq.index(end.upper())

    current_pos: int = pos_start

    out_seq: list[str] = []

    if pos_start < pos_end:
        while current_pos <= pos_end:
            out_seq += sq[current_pos]
            current_pos += 1
    elif pos_start == pos_end:
        out_seq += sq[pos_start]
    elif pos_start > pos_end:
        while current_pos <= (lenght-1):
            out_seq += sq[current_pos]
            current_pos += 1
        current_pos = 0
        while current_pos <= pos_end:
            out_seq += sq[current_pos]
            current_pos += 1
    
    return out_seq

seq: list[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
months: list[str] = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
majors: list[str] = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
years: list[str] = ["U", "V", "W", "X", "Y", "Z"]

def is_valid(start: str, end: str) -> bool:
    # Check if input is valid
    start_list: list[str] = list(start.upper())
    end_list: list[str] = list(end.upper())

    if len(start_list) != 6 or len(end_list) != 6:
        print("ERROR: Start value or end value is not provided correctly!")
        return False
    
    if start_list[0] not in ("U", "S"):
        print("ERROR: Start value not valid!")
        print("Unknown feature flag")
        return False

    if end_list[0] not in ("U", "S"):
        print("ERROR: End value not valid!")
        print("Unknown feature flag")
        return False
    
    rp_start: str = start_list[1]
    rp_end: str = end_list[1]

    if rp_start not in seq:
        print("ERROR: Start RP value not valid")
        return False
    
    if rp_end not in seq:
        print("ERROR: End RP value not valid")
        return False
    
    if seq.index(rp_start) > seq.index(rp_end):
        print("ERROR: Start RP is greater than End RP")
        return False
    
    major_start: str = start_list[2]
    major_end: str = end_list[2]

    if major_start not in majors:
        print("ERROR: Start Major value not valid")
        return False
    
    if major_end not in majors:
        print("ERROR: End Major value not valid")
        return False

    if majors.index(major_start) > majors.index(major_end):
        print("ERROR: Start Major is greater than End Major")
        return False
    
    year_start: str = start_list[3]
    year_end: str = end_list[3]

    if year_start not in years:
        print("ERROR: Start Year value not valid")
        return False
    
    if year_end not in years:
        print("ERROR: End Year value not valid")
        return False

    if years.index(year_start) > years.index(year_end):
        print("ERROR: Start Year is greater than End Year")
        return False
    
    month_start: str = start_list[4]
    month_end: str = end_list[4]
    build_start: str = start_list[5]
    build_end: str = end_list[5]

    # Difficult situations
    if year_start == year_end:
        if month_start == month_end:
            if seq.index(build_start) > seq.index(build_end):
                print("ERROR: Start Build is greater than End Build")
                return False
        if months.index(month_start) > months.index(month_end):
            print("ERROR: Start Month is greater than End Month")
            return False
    
    return True

def get_combinations(start: str, end: str, is_csc: bool = False, check_beta: bool = False) -> list[str]:
    start = start.upper()
    end = end.upper()
    start_list: list[str] = list(start)
    end_list: list[str] = list(end)

    if not is_valid(start, end):
        print("ERROR: Unable to continue. Start and End not valid.")
        exit(1)

    feature_start: str = start_list[0]
    feature_end: str = end_list[0]
    rp_start: str = start_list[1]
    rp_end: str = end_list[1]
    major_start: str = start_list[2]
    major_end: str = end_list[2]
    year_start: str = start_list[3]
    year_end: str = end_list[3]
    month_start: str = start_list[4]
    month_end: str = end_list[4]
    build_start: str = start_list[5]
    build_end: str = end_list[5]

    is_same_rp: bool = rp_start == rp_end
    is_same_major: bool = major_start == major_end
    is_same_year: bool = year_start == year_end
    is_same_month: bool = month_start == month_end
    is_same_build: bool = build_start == build_end
    is_same_feature: bool = feature_start == feature_end

    combos: list = []

    if check_beta:
        is_same_major = False

    if is_same_feature:
        if is_same_rp:
            if is_same_major:
                if is_same_year:
                    if is_same_month:
                        if is_same_build:
                            combos.append(start)
                        else:
                            ap: str = feature_start + rp_start + major_start + year_start + month_start
                            for i in seq_gen(seq, build_start, build_end):
                                combos.append(ap+i)
                    else:
                        diff: int = seq.index(month_end) - seq.index(month_start)
                        if diff == 1:
                            for i in get_combinations(start, feature_start+rp_start+major_start+year_start+month_start+"Z"):
                                combos.append(i)
                            for i in get_combinations(feature_start+rp_start+major_start+year_start+month_end+"0", end):
                                combos.append(i)
                        else:
                            for i in get_combinations(start, feature_start+rp_start+major_start+year_start+month_start+"Z"):
                                combos.append(i)
                            fm_list: list[str] = seq_gen(months, month_start, month_end)
                            fm_list.remove(month_start)
                            fm_list.remove(month_end)
                            for i in fm_list:
                                for i in get_combinations(feature_start+rp_start+major_start+year_start+i+"0", feature_start+rp_start+major_start+year_start+i+"Z"):
                                    combos.append(i)
                            for i in get_combinations(feature_start+rp_start+major_start+year_start+month_end+"0", end):
                                combos.append(i)

                else: # not same year
                    diff: int = seq.index(year_end) - seq.index(year_start)
                    if diff == 1:
                        for i in get_combinations(start, feature_start+rp_start+major_start+year_start+"L"+"Z"):
                            combos.append(i)
                        for i in get_combinations(feature_start+rp_start+major_start+year_end+"A"+"0", end):
                            combos.append(i)
                    else:
                        for i in get_combinations(start, feature_start+rp_start+major_start+year_start+"L"+"Z"):
                            combos.append(i)
                        fm_list  = seq_gen(years, year_start, year_end)
                        fm_list.remove(year_start)
                        fm_list.remove(year_end)
                        for i in fm_list:
                            for i in get_combinations(feature_start+rp_start+major_start+i+"A"+"0",feature_start+rp_start+major_start+i+"L"+"Z" ):
                                combos.append(i)
                        for i in get_combinations(feature_start+rp_start+major_start+year_end+"A"+"0", end):
                            combos.append(i)

            else: # not same major
                major_list: list[str] = seq_gen(majors, major_start, major_end)
                if check_beta:
                    major_list.append("Z")
                for m in major_list:
                    for i in get_combinations(feature_start+rp_start+m+year_start+month_start+build_start, feature_end+rp_end+m+year_end+month_end+build_end):
                        combos.append(i)
        else: # not same rp
            rp_list: list[str] = seq_gen(seq, rp_start, rp_end)
            for m in rp_list:
                for i in get_combinations(feature_start+m+major_start+year_start+month_start+build_start, feature_end+m+major_end+year_end+month_end+build_end):
                    combos.append(i)
    else: # not same feature
        feature_list: list[str] = ["S", "U"]
        if is_csc:
            feature_list.remove("S")
        for f in feature_list:
            for i in get_combinations(f+rp_start+major_start+year_start+month_start+build_start, f+rp_end+major_end+year_end+month_end+build_end):
                combos.append(i)

    return combos

def gen_build_combos(start: str, end: str, modem: bool, also_beta: bool = False) -> list[tuple]:
    combos: list[str] = get_combinations(start, end, check_beta=also_beta)
    ap_csc_list: list = []
    for c in combos:
        for i in get_combinations(start,end, is_csc=True, check_beta=also_beta):
            e = list(i)
            e.pop(0)
            f: str = ""
            for l in e:
                f += str(l)
            ap_csc_list.append((c, f))
    if modem:
        modem_list: list = []
        for ac in ap_csc_list:
            for i in get_combinations(start, end):
                modem_list.append((ac[0], ac[1], i))
        return modem_list

    return ap_csc_list

def gen_full_build(model: str, csc: str, combos: list[tuple], modem: bool):
    csc = csc.upper()
    model = model.upper()
    if csc == "EUX" or csc == "ITV":
        mcsc: str = "OXM"
        omc: str = "XX"
    else: #TODO: handle different CSCs
        omc: str = "XX"
        mcsc: str = "OXM"
    builds_list: list[str] = []
    for combo in combos:
        if modem:
            builds_list.append(str(model+omc+combo[0]+"/"+model+mcsc+combo[1]+"/"+model+omc+combo[2]))
        else:
            builds_list.append(str(model+omc+combo[0]+"/"+model+mcsc+combo[1]+"/"))
    return builds_list

#print(is_valid("U8CXK5", "UBCXL1"))
#print(seq_gen(seq, "5", "8"))
#print(get_combinations("U8CXLM", "S8CXLZ"))
#print(gen_build_combos("U8CXLM", "U8CXLN", True))

def sherlock_main(model: str, csc, start, end, modem, do_beta: bool = False): #-> list[str]:
    model = model.upper()
    csc = csc.upper()
    start = start.upper()
    end = end.upper()
    if "SM-" in model:
        model.replace("SM-", "")
    builds: list[str] = gen_full_build(model, csc, gen_build_combos(start, end, modem, also_beta=do_beta), modem)
    return builds

def sherlock_write(model: str, csc, start, end, modem, out, do_beta = "False"): #-> list[str]:
    model = model.upper()
    csc = csc.upper()
    start = start.upper()
    end = end.upper()
    modem = modem.upper()
    do_beta = do_beta.upper()
    if "SM-" in model:
        model = model.replace("SM-", "")
        #print(model)
    if modem == "TRUE":
        modem = True
    else:
        modem = False
    if do_beta == "TRUE":
        do_beta = True
    else:
        do_beta = False
    builds: list[str] = gen_full_build(model, csc, gen_build_combos(start, end, modem, also_beta=do_beta), modem)
    with open(out, 'w') as f:
        for b in builds:
            f.write(f"{b}\n")

#sherlock_main("A346B", "EUX", "U7CXLM", "U7CXLN", False, "builds.txt")

if __name__ == "__main__":
    if len(args) != 7 and len(args) != 8:
        print("Not enough arguments")
        print("Expected: MODEL CSC START END MODEM OUT_FILE")
    else:
        if len(args) == 7:
            sherlock_write(args[1], args[2], args[3], args[4], args[5], args[6])
        elif len(args) == 8:
            sherlock_write(args[1], args[2], args[3], args[4], args[5], args[6], args[7])
