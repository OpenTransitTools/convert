#
# copies .yml localization files from OTP-UI to this folder (with a bunch of sub-folders)
#
DEV_DIR=../..
OTP_PACKS=$DEV_DIR/otp-ui/packages
TORA_ENGLISH=$DEV_DIR/trimet.org/src/intl/en.json


function to_relative_file()
{
    # turns a ../../blah/path string to a relative ./blah/path string by stripping of characters
    local rn=$1
    rn=${rn/$OTP_PACKS}
    rn=${rn/\/i18n}
    rn=${rn/_Hans}
    rn=${rn/-US}
    echo ".${rn}"
}


function cp_i18n()
{
    cp $TORA_ENGLISH ./

    for n in `find $OTP_PACKS | grep i18n.*yml`
    do
        # create destination sub-dir
        d=${n##$OTP_PACKS/}
        d=${d%/i18n*}
        mkdir -p $d

        # rename the files
        rel=$(to_relative_file $n)

        # copy src to renamed file in sub-dir
        cp $n $rel
    done
}


function diff_i18n()
{
    for n in `find $OTP_PACKS | grep i18n.*yml`
    do
        rel=$(to_relative_file $n)
        diff="diff $n $rel"
        echo $diff
        eval $diff
    done
}


if [[ $1 == "copy" || $1 == "cp" ]]
then
    cp_i18n
else
    diff_i18n
fi
