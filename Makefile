
convert-data1:
	python scripts/convert_data_format.py convert-type1 --prefix-dir "" --input-images-dir data/FROM-LATEX-OCR \
		--input-label-fp data/FROM-LATEX-OCR/pdfmath.txt -o data/FROM-LATEX-OCR/train-all.txt
	python scripts/convert_data_format.py convert-type1 --prefix-dir "" --input-images-dir data/CROHME \
		--input-label-fp data/CROHME/CROHME_math.txt -o data/CROHME/train-all.txt

convert-data2:
#	python scripts/convert_data_format.py convert-type2 --prefix-dir "data/Data-for-LaTeX_OCR/small/images" \
# 		--input-match-index-dir data/Data-for-LaTeX_OCR/small/matching \
# 		--input-images-dir data/Data-for-LaTeX_OCR/small/images \
#		--input-label-dir data/Data-for-LaTeX_OCR/small/formulas \
#		-o data/Data-for-LaTeX_OCR/small/train-all.txt
	python scripts/convert_data_format.py convert-type2 --prefix-dir "data/Data-for-LaTeX_OCR/full/images" \
 		--input-match-index-dir data/Data-for-LaTeX_OCR/full/matching \
 		--input-images-dir data/Data-for-LaTeX_OCR/full/images \
		--input-label-dir data/Data-for-LaTeX_OCR/full/formulas \
		-o data/Data-for-LaTeX_OCR/full/train-all.txt
	python scripts/convert_data_format.py convert-type2 --prefix-dir "data/Data-for-LaTeX_OCR/fullhand/images" \
 		--input-match-index-dir data/Data-for-LaTeX_OCR/fullhand/matching \
 		--input-images-dir data/Data-for-LaTeX_OCR/fullhand/images \
		--input-label-dir data/Data-for-LaTeX_OCR/fullhand/formulas \
		-o data/Data-for-LaTeX_OCR/fullhand/train-all.txt
	python scripts/convert_data_format.py convert-type2 --prefix-dir "data/Data-for-LaTeX_OCR/hand/images" \
 		--input-match-index-dir data/Data-for-LaTeX_OCR/hand/matching \
 		--input-images-dir data/Data-for-LaTeX_OCR/hand/images \
		--input-label-dir data/Data-for-LaTeX_OCR/hand/formulas \
		-o data/Data-for-LaTeX_OCR/hand/train-all.txt
	python scripts/convert_data_format.py convert-type2 --with-print --prefix-dir "data/Data-for-LaTeX_OCR/hand/images" \
 		--input-match-index-dir data/Data-for-LaTeX_OCR/hand/matching \
 		--input-images-dir data/Data-for-LaTeX_OCR/hand/images \
		--input-label-dir data/Data-for-LaTeX_OCR/hand/formulas \
		-o data/Data-for-LaTeX_OCR/hand/train-all-print.txt


.PHONY: convert-data1 convert-data2
