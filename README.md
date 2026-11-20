# Lamia SVG – Διαδραστικός Χάρτης

## Περιγραφή του Project

Το συγκεκριμένο project αφορά τη δημιουργία ενός διαδραστικού χάρτη (Interactive Map) του Δήμου Λαμιέων, με επίκεντρο τις πέντε Δημοτικές Ενότητες (Δ.Ε.) που τον αποτελούν.

Η εργασία ξεκίνησε από τον γεωγραφικό χάρτη του Νομού Φθιώτιδας, από τον οποίο απομονώθηκε ο Δήμος Λαμιέων.

<p align="center">
  <img src="lamia.svg" alt="Lamia Map" width="600">
</p>

<div style="position: relative; width: 500px; margin: auto;">

  <img src="done_svgs/ypatis.svg"
       style="position: absolute; top: 0; left: 0; width: 100%;">

  <img src="done_svgs/lianokladi.svg"
       style="position: absolute; top: 0; left: 0; width: 100%;">

  <img src="done_svgs/lamieon.svg"
       style="position: absolute; top: 0; left: 0; width: 100%;">

  <img src="done_svgs/gorgopotamos.svg"
       style="position: absolute; top: 0; left: 0; width: 100%;">

  <img src="done_svgs/pauliani.svg"
       style="position: absolute; top: 0; left: 0; width: 100%;">

</div>

## Δημοτικές Ενότητες

Ο Δήμος Λαμιέων αποτελείται από τις παρακάτω πέντε Δημοτικές Ενότητες:

1. **Υπάτης**
2. **Λιανοκλαδίου**
3. **Λαμιέων**
4. **Γοργοποτάμου**
5. **Παύλιανης**

<p align="center">
  <img src="blue_svgs/upati_blue.svg" alt="Lamia Map" width="600">
</p>

<p align="center">
  <img src="blue_svgs/lianokladi_blue.svg" alt="Lamia Map" width="600">
</p>

<p align="center">
  <img src="blue_svgs/lamiewn_blue.svg" alt="Lamia Map" width="600">
</p>

<p align="center">
  <img src="blue_svgs/gorgopotamos_blue.svg" alt="Lamia Map" width="600">
</p>

<p align="center">
  <img src="blue_svgs/pauliani_blue.svg" alt="Lamia Map" width="600">
</p>

## Επεξεργασία Χάρτη

Η διαδικασία που ακολουθήθηκε:

1. Χρησιμοποιήθηκε ως αρχικό υλικό ένας γεωγραφικός χάρτης του Δήμου Λαμιέων.
2. Ο χάρτης επεξεργάστηκε και διαχωρίστηκε γεωγραφικά στις πέντε Δημοτικές Ενότητες.
3. Κάθε Δημοτική Ενότητα απομονώθηκε και μετατράπηκε σε ξεχωριστό αρχείο SVG.
4. Τα επιμέρους SVG προορίζονται για χρήση σε εφαρμογή, όπου κάθε Δημοτική Ενότητα μπορεί να αναγνωρίζεται και να χρωματίζεται ανεξάρτητα.

## Δομή Αρχείων

| Αρχείο / Φάκελος | Περιγραφή |
|---|---|
| `lamia.svg` | Ο αρχικός χάρτης του Δήμου Λαμιέων. |
| `blue_svgs/` | SVG αρχεία με μπλε χρωματισμό. |
| `done_svgs/` | Τα επεξεργασμένα SVG των Δημοτικών Ενοτήτων. |
| `recolor_svg.py` | Python script για τον χρωματισμό των SVG σε μπλε αποχρώσεις. |

## Σκοπός

Στόχος είναι η δημιουργία ενός διαδραστικού γεωγραφικού χάρτη, στον οποίο οι πέντε Δημοτικές Ενότητες θα αποτελούν ανεξάρτητα και επεξεργάσιμα στοιχεία.

Με αυτόν τον τρόπο, κάθε ενότητα θα μπορεί να χρωματίζεται, να επιλέγεται και να χρησιμοποιείται ξεχωριστά μέσα στην εφαρμογή.
