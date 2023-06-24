# coding: utf-8
import os
import logging
from glob import glob
import click
from argparse import ArgumentParser

_CONTEXT_SETTINGS = {"help_option_names": ['-h', '--help']}
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@click.group(context_settings=_CONTEXT_SETTINGS)
def cli():
    pass


def save_pairs_to_file(out_pairs, out_fp, prefix_dir):
    with open(out_fp, 'w') as f:
        for pair in out_pairs:
            fp = os.path.join(prefix_dir, pair[0]) if prefix_dir else pair[0]
            f.write(f'{fp.strip()}\t{pair[1]}\n')


@click.command('convert-type1')
@click.option("-p", "--prefix-dir", default='', help="追加在文件名前面的前置路径")
@click.option("--input-images-dir", required=True, help="图片存储的根目录")
@click.option("--input-label-fp", required=True, help="Latex输出所在的label文件路径")
@click.option("-o", "--output-index-fp", required=True, help="path to output file")
def default_convert(prefix_dir, input_images_dir, input_label_fp, output_index_fp):
    # 应用于数据集：FROM-LATEX-OCR，CROHME
    img_fp_list = glob('{}/**/*g'.format(input_images_dir), recursive=True)
    latex_labels = open(input_label_fp, 'r').read().split('\n')

    output_pairs = []
    for img_fp in img_fp_list:
        fn = os.path.basename(img_fp)
        line_idx = int(fn.split('.')[0])
        label = latex_labels[line_idx].strip().replace('\t', ' ')
        output_pairs.append([img_fp, label])

    save_pairs_to_file(output_pairs, output_index_fp, prefix_dir)


@cli.command('convert-type2')
@click.option("-p", "--prefix-dir", default='', help="追加在文件名前面的前置路径")
@click.option("--with-print", is_flag=True, help="图片是在 `images_train` 中，还是在 `images_train_print` 中")
@click.option("--input-match-index-dir", required=True, help="matching文件存储的目录")
@click.option("--input-images-dir", required=True, help="图片存储的根目录")
@click.option("--input-label-dir", required=True, help="Latex输出所在的label目录")
@click.option("-o", "--output-index-fp", required=True, help="path to output file")
def convert_Data_for_LaTeX_OCR(prefix_dir, with_print, input_match_index_dir, input_images_dir, input_label_dir, output_index_fp):
    # 应用于数据集：Data-for-LaTeX_OCR
    output_pairs = []
    for data_type in ('train', 'val', 'test'):
        input_label_fp = os.path.join(input_label_dir, '{}.formulas.norm.txt'.format(data_type))
        if not os.path.exists(input_label_fp):
            input_label_fp = os.path.join(input_label_dir, 'formulas.norm.txt')

        input_match_index_fp = os.path.join(input_match_index_dir, '{}.matching.txt'.format(data_type))

        pairs = open(input_match_index_fp, 'r').read().strip().split('\n')
        for pair in pairs:
            eles = pair.split(' ')
            if len(eles) != 2:
                breakpoint()
        ori_pairs = [pair.split(' ') for pair in pairs]

        latex_labels = open(input_label_fp, 'r').read().split('\n')

        image_suffix_dir = ''
        cand_img_dir = os.path.join(input_images_dir, 'images_{}'.format(data_type))
        if with_print:
            cand_img_dir += '_print'
        if os.path.exists(cand_img_dir) and os.path.isdir(cand_img_dir):
            image_suffix_dir = 'images_{}'.format(data_type)

        for img_fp, line_idx in ori_pairs:
            img_fp = os.path.join(image_suffix_dir, img_fp) if image_suffix_dir else img_fp
            line_idx = int(line_idx)
            label = latex_labels[line_idx].strip().replace('\t', ' ')
            output_pairs.append([img_fp, label])

    save_pairs_to_file(output_pairs, output_index_fp, prefix_dir)


if __name__ == "__main__":
    cli()
