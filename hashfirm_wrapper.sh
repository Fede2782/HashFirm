#!/bin/bash
#
# Copyright (C) 2024 Fede2782
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.                                                                                                           #
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

if [ "$#" != 5 ] && [ "$#" != 6 ]; then
    #echo "Usage: bash sherlock_wrapper.sh <CSC> <MODEL> <START> <END>"
    echo "Usage: bash hashfirm_wrapper.sh <MODEL> <CSC> <START> <END> <MODEM> <CHECK_BETA>"
    exit 1
fi

#HASHES=($(curl https://fota-cloud-dn.ospserver.net/firmware/$2/$1/version.test.xml | grep fwsize | sed 's/<value rcount=//' | sed 's/<\/value>//' | grep -oP "'\d+' fwsize='\d+'>\K[a-f0-9]{32}"))
HASHES=($(curl -s https://fota-cloud-dn.ospserver.net/firmware/$2/$1/version.test.xml | grep fwsize | sed -E 's/.*'\''[0-9]+'\'' fwsize='\''[0-9]+'\''>//' | sed -E 's/<\/value>//'))

if [ "$#" == 5 ]; then
  python3 hashfirm_engine.py $1 $2 $3 $4 $5 builds.txt
elif [ "$#" == 6 ]; then
  python3 hashfirm_engine.py $1 $2 $3 $4 $5 builds.txt $6
fi

for i in $(cat builds.txt)
do
    #echo $i
    HASH="$(echo -n "$i" | md5sum | sed 's/ -//' )"
    #echo $HASH
    found=false

    for hs in "${HASHES[@]}"
    do
        if [[ "$HASH" == *"$hs"* ]]; then
        found=true
        #HASHES -= "$HASH"
        fi
    done

    if $found; then
        echo "Found $i!"
    fi

done

rm builds.txt
