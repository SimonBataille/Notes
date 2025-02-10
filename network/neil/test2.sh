#!/bin/bash

# Vérifier si pdfjam est installé
if ! command -v pdfjam &> /dev/null; then
    echo "Erreur : pdfjam n'est pas installé. Installez-le avec : sudo apt install texlive-extra-utils"
    exit 1
fi

# Boucle sur tous les fichiers PDF du dossier courant
for file in *.pdf; do
    # Vérifier que des fichiers existent
    [ -e "$file" ] || continue
    
    # Extraire le nom de base sans extension
    base_name="${file%.pdf}"
    
    # Définir le nom du fichier de sortie avec _4x4
    output_file="${base_name}_4x4.pdf"
    
    # Appliquer pdfjam pour générer le fichier avec 4 pages par feuille et en A4
    pdfjam --nup 2x2 --landscape --paper a4paper --outfile "$output_file" "$file"
    
    # Réduire la taille du fichier sans perte de qualité notable
    gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -dNOPAUSE -dQUIET -dBATCH -sOutputFile="compressed_$output_file" "$output_file"
    mv "compressed_$output_file" "$output_file"
    echo "✔️ Fichier traité et compressé : $output_file"

done

echo "Tous les fichiers PDF ont été traités."

# Concaténer tous les fichiers _4x4.pdf en un seul fichier
output_concat="merged_4x4.pdf"
files_to_merge=( *_4x4.pdf )

if [ ${#files_to_merge[@]} -gt 0 ]; then
    pdftk "${files_to_merge[@]}" output "$output_concat"
    
    # Compression finale du fichier fusionné
    gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -dNOPAUSE -dQUIET -dBATCH -sOutputFile="compressed_$output_concat" "$output_concat"
    mv "compressed_$output_concat" "$output_concat"
    
    if [ $? -eq 0 ]; then
        echo "Fichier final concaténé et compressé : $output_concat"
    else
        echo "❌ Erreur lors de la fusion des fichiers avec pdftk."
    fi
else
    echo "Aucun fichier 4x4 valide trouvé pour la concaténation."
fi

