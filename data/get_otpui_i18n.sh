#
# copies .yml localization files from OTP-UI to this folder (with a bunch of sub-folders)
#

DEV_DIR=../..
OTP_PACKS=$DEV_DIR/otp-ui/packages
TORA_ENGLISH=$DEV_DIR/trimet.org/src/intl/en.json

cp $TORA_ENGLISH ./

for n in `find $OTP_PACKS | grep i18n.*yml`
do
    # create destination sub-dir
    d=${n##$OTP_PACKS/}
    d=${d%/i18n*}
    mkdir -p $d

    # rename the files 
    rn=${n/$OTP_PACKS}
    rn=${rn/\/i18n}
    rn=${rn/_Hans}
    rn=${rn/-US}

    # copy src to renamed file in sub-dir
    cp $n .$rn 
done

