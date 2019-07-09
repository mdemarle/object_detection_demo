import xml.etree.ElementTree as ET
import os
import glob
import urllib.parse as urlparse
import xml
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(    
    )
    parser.add_argument(
        "--raw_dir",
        help="Directory path to raw documents.",
        default="C:/Users/mdemarle/Documents/projet m/object_detection_demo/data/images/train/Nouveau dossier",
        type=str,
    )
    parser.add_argument(
        "--save_dir",
        help="Directory path to save documents.",
        default="C:/Users/mdemarle/Documents/projet m/object_detection_demo/data/images/train",
        type=str,
    )
    
    args = parser.parse_args()

    raw_dir = args.raw_dir
    save_dir = args.save_dir
    nomsfichiers = os.listdir(raw_dir)
    for nomfichier in nomsfichiers :
        nomfi = nomfichier.split(".")[0]
        tree = ET.parse(raw_dir + "/" + nomfichier)
        root = tree.getroot()
        for i in root.findall('path'):
            ch = i.text
            n = ch.split("\\")[-1] 
            nom = n.split(".")[0]
            ext = n.split(".")[-1] 
            newname = nomfi + "." + ext
            texte = save_dir + "/" + newname
            i.text = texte.replace("/","\\")
            for j in root.findall('filename'):
                j.text = newname
        nomf = os.path.join(save_dir, nomfichier)
        tree.write(nomf)
