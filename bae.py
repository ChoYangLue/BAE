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
    pdb.gimp_brushes_set_opacity(45)
    pdb.gimp_context_set_brush_size(60)

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

    # 露出補正はなんかうまくいかない
    #pdb.gimp_dodgeburn(new_layer, exposure, 0, 1, 4,(0,0, 0,1000, 1000,0, 1000,1000))

    pdb.gimp_brightness_contrast(new_layer, exposure, exposure-10)

    # 完全透明黒でマスクを作成する
    mask = pdb.gimp_layer_create_mask(new_layer, ADD_BLACK_MASK)

    # マスクをレイヤーに追加する
    pdb.gimp_layer_add_mask(new_layer, mask)

    # ブラシをアクティブに
    pdb.gimp_context_set_brush("2. Hardness 075")
    pdb.gimp_brushes_set_opacity(19)
    pdb.gimp_context_set_brush_size(400)

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
            (PF_SLIDER, "opacity",  "Exposure Level", 20, (0, 100, 1)),
         ],                      #引数
        [],                      #戻り値
        plugin_skin_exposure,             # main 関数名
        menu="<Image>/PyPlgin"   #プラグインの登録場所
        )

main()
