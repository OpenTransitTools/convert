#
# copies .yml localization files from OTP-UI to this folder (with a bunch of sub-folders)
#

OTP_PACKS=../../otp-ui/packages

for n in `find $OTP_PACKS | grep i18n.*yml`
do
    d=${n##$OTP_PACKS/}
    d=${d%/i18n*}
    mkdir $d
    cp $n $d/
done

