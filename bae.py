#!/usr/bin/env python
# coding: utf8

from gimpfu import *

# 肌用レイヤーの追加
def plugin_skin_texture(image, layer, angle):
    # レイヤーのコピー
    new_layer = pdb.gimp_layer_copy(layer, 1)
    image.add_layer(new_layer, 0)

    # ガウシアンブラー
    pdb.plug_in_gauss_rle(image, new_layer, angle, 1, 0)
    pdb.plug_in_gauss_rle(image, new_layer, angle, 0, 1)

    # 完全透明黒でマスクを作成する
    mask = pdb.gimp_layer_create_mask(new_layer, ADD_BLACK_MASK)

    # マスクをレイヤーに追加する
    pdb.gimp_layer_add_mask(new_layer, mask)

    # ブラシをアクティブに
    pdb.gimp_context_set_brush("2. Hardness 075")

    return 0


# フィルターに登録
register(
        "add_skin_texture_layer",           #プロシージャの名前
        "add skin texture layer",           #プラグインの情報
        "help",                             #詳しいプラグインの情報
        "doyaken",                          #プラグインの著者
        "doyaken",                          #コピーライト
        "Jan 2023",                         #日付
        "skin texture layer",               #メニューに表示するプラグイン名
        "",                                 #画像タイプ
        [
            (PF_IMAGE, "image", "Input image", None),
            (PF_DRAWABLE, "drawable", "Drawable", None),
            (PF_SLIDER, "opacity",  "Skin Level", 20, (0, 100, 1)),
         ],                      #引数
        [],                      #戻り値
        plugin_skin_texture,             # main 関数名
        menu="<Image>/PyPlgin"   #プラグインの登録場所
        )

# 露出補正レイヤーの追加
def plugin_skin_exposure(image, layer, exposure):
    # レイヤーのコピー
    new_layer = pdb.gimp_layer_copy(layer, 1)
    image.add_layer(new_layer, 0)

    # 露出補正
    pdb.gimp_dodgeburn(new_layer, exposure, 1, 0)

    # 完全透明黒でマスクを作成する
    mask = pdb.gimp_layer_create_mask(new_layer, ADD_BLACK_MASK)

    # マスクをレイヤーに追加する
    pdb.gimp_layer_add_mask(new_layer, mask)

    # ブラシをアクティブに
    pdb.gimp_context_set_brush("2. Hardness 075")

    return 0

# フィルターに登録
register(
        "add_skin_exposure_layer",          #プロシージャの名前
        "add skin exposure layer",          #プラグインの情報
        "help",                             #詳しいプラグインの情報
        "doyaken",                          #プラグインの著者
        "doyaken",                          #コピーライト
        "Jan 2023",                         #日付
        "skin exposure layer",              #メニューに表示するプラグイン名
        "",                                 #画像タイプ
        [
            (PF_IMAGE, "image", "Input image", None),
            (PF_DRAWABLE, "drawable", "Drawable", None),
            (PF_SLIDER, "opacity",  "Op_acity", 20, (0, 100, 1)),
         ],                      #引数
        [],                      #戻り値
        plugin_skin_exposure,             # main 関数名
        menu="<Image>/PyPlgin"   #プラグインの登録場所
        )

main()
