#! /bin/sh
# paramétres 
target_name="$1"  # Nom du fichier final
page_count="$2" # optionnel, le nombre de feuilles à numériser

# on supprime le dossier temporaire de numérisation, on le recrée et on s'y place
if [ -d scans ] ; then
rm -rf scans
fi
mkdir scans
cd scans

# utilisation de scanimage pour déterminer l'adresse de notre scanner
scanner_usb_id=$( scanimage -L | grep pixma | cut -d "\`" -f2 | cut -d"'" -f1)

# options de numérisation par défaut
scanimage_options="--mode color --resolution 150 -d $scanner_usb_id"

# Choix entre 1 et plusieurs pages. 
if [ ! -z $page_count ] ; then
echo "Génération des fichiers sur le modèle $TIME_STAMP"
scanimage $scanimage_options --batch="$target_name %d"  --batch-count $page_count --batch-prompt
else
scanimage $scanimage_options > $target_name
fi

# conversion de toutes les images en JPEG
for file in * ; do 
echo "Conversion de $file en jpg"
convert -quality 80 "$file" "$file.jpg"
rm -rf "$file"
done

# Si nous avons plus d'une page, on converti les JPEG en un seul document PDF
if [ ! -z $page_count ] ; then
convert * "../$target_name.pdf"
else
mv -f * ..
fi
cd ..

# ménage
rm -rf scans

# example of use : ./scanner.sh quittance_nov_dec 1
