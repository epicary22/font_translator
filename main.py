import json
from big_char import BigChar

with open("charsets.json", "r") as file:
    data = file.read()
    charsets = json.loads(data)

# print(charsets)
# for hexcode, char in charsets["Hufflepuffian"]["text"].items():
#     print(f"'{hexcode}'\n{char}\n")

to_translate = "EThO VREeSs-KETE O FERNIL-IKUSs Ee EL-EPU. " \
"Ee-ThE NA ANAPAVE-SsE EThO EN EeREe-NEe, E'KsO-REe-SsTREe-E TU KERBIL-LIKUSs, ThOLOFONOSs TU IP-POTEe TU DOR, KYE VASsILEeA'Ss OLU TU KO'SsMU KYE 'OFLEe-POF. " \
"Ee-ThE NA ANAPAF-ThEeTE PADA SsTEeSs EFKhAR-ISsTEe-ESs MASs."

# to_translate = "NOREe E'MNO'T, LO-GIN BE'K FAYG, TRISs-TIN 'ER, BEND-ZhA-MIN KA'SsTE'N-MIY-ER, " \
# "AYVER-Ee KAYN, "

# to_translate = "BUR-Th-DAY"

to_translate = "EPIKEREe"

i = 0
chars = charsets["Hufflepuffian"]["text"]
to_translate += " "
translation = None
translation_lines = []
while i < len(to_translate):
    # if i == len(to_translate) - 1:
    #     short_slice = to_translate[i]
    #     if short_slice in chars.keys():
    #         output_letter = chars[short_slice]
    #         i += 1
    #     else:
    #         output_letter = chars["None"]
    #         i += 1
    # else:
    current_slice = to_translate[i:i+2]
    if current_slice in chars.keys():
        letter_to_translate = current_slice
        i += 2
    elif current_slice[0] in chars.keys():
        letter_to_translate = current_slice[0]
        i += 1
    else:
        letter_to_translate = "None"
        i += 1
    output_letter = BigChar(letter_to_translate, "text", "Hufflepuffian")
    if not translation:
        translation = output_letter
    else:
        translation = translation.append_(output_letter)
        if len(translation.char) / 5 > 120:
            translation_lines.append(translation)
            translation = None

translation_lines.append(translation)

print("TRANSLATION\n===========\n")
for line in translation_lines:
    print(line.char, "\n")

