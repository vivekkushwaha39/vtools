if [ $# -lt 2 ] ; then
	echo "============================="
	echo "usage: collisutils aid count "
	exit
fi


if [ "$collisdir" = "" ]; then
	collisdir="/cygdrive/c/UL Test Tools/BTT 5.3.0/Application/Suites/Images/Discover/Contactless"
	echo "Collis dir is not set"
	echo "using collis dir as: "$collisdir
fi


aid_cards=`grep -nri "A0 00 00 01 52 30 10" "$collisdir" |sort|uniq|cut -f1 -d:|sed 's/$/"/'`
single_aid=`grep -nri "</AID>" "$collisdir" --count|grep :1|sort|uniq|cut -f1 -d:|sed 's/$/"/'`

echo $aid_cards

IFS_BAK=$IFS
IFS="\""

echo "Common AIDs are"
for said in $single_aid ; do
	for aidc in $aid_cards ; do 
		if [ "$said" = "$aidc" ] ; then
			echo $said
		fi
	done
done
