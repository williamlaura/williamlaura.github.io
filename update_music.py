import re

mapping = {
    'home.qmd': ('中岛美嘉 - 雪之花.mp3', '雪の華', '中岛美嘉'),
    'index.qmd': ('中岛美嘉 - 雪之花.mp3', '雪の華', '中岛美嘉'),
    'publications.qmd': ('滨崎步-my all.mp3', 'MY ALL', '滨崎步'),
    'xanadu.qmd': ('岚- 故乡.mp3', '故乡', '岚'),
    'foodmap.qmd': ('高桥优-ヤキモチ(吃醋)起风了.mp3', 'ヤキモチ', '高桥优'),
    'food/cuisine1.qmd': ('米津玄師-lemon.mp3', 'Lemon', '米津玄师'),
    'food/cuisine2.qmd': ('大黑摩季《空》.mp3', '空', '大黑摩季'),
    'food/cuisine3.qmd': ('WANDS-直到世界尽头.mp3', '直到世界尽头', 'WANDS'),
    'poems/poem1.qmd': ('菅田将晖-虹.mp3', '虹', '菅田将晖'),
    'poems/poem2.qmd': ('中孝介-各自远扬.mp3', 'それぞれに', '中孝介'),
    'poems/poem3.qmd': ('王菲-匆匆那年.mp3', '匆匆那年', '王菲'),
    'poems/poem4.qmd': ('中島美嘉-僕が死のうと思ったのは.mp3', '曾经我也想过一了百了', '中岛美嘉'),
    'poems/poem5.qmd': ('YOASOBI - 群青.mp3', '群青', 'YOASOBI'),
    'poems/poem6.qmd': ('王菲-催眠.mp3', '催眠', '王菲'),
    'poems/poem7.qmd': ('daoko&米津玄师-打上花火.mp3', '打上花火', '米津玄师'),
    'poems/poem8.qmd': ('许嵩-断桥残雪.mp3', '断桥残雪', '许嵩'),
}

pat = re.compile(r'<div class="music-meta"[^>]*></div>')

for path, (fname, title, artist) in mapping.items():
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    replacement = f'<div class="music-meta" data-src="music/{fname}" data-title="{title}" data-artist="{artist}" style="display:none;"></div>'
    new_content, count = pat.subn(replacement, content)
    
    if count == 0:
        print(f"WARNING: no match in {path}")
    else:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"OK: {path}")
