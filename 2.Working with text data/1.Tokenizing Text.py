







## 2.2 Tokenizing text




import urllib.request
import pandas as pd

text_verdict = open("/Users/benjaminbrooke/PycharmProjects/Blue-Ocean/Data/The Verdict.txt","r",encoding="utf-8")
raw_txt = text_verdict.read()


print(len(raw_txt))
#20479


import re

text = "Hello world. This is a test."
result = re.split(r'(\s)',text)
print(result)
#['Hello', ' ', 'world.', ' ', 'This', ' ', 'is', ' ', 'a', ' ', 'test.']



result = re.split(r'([,.:;?_!"()\']|--|\s)', text)
result = [item.strip() for item in result if item.strip()]
print(result)
#['Hello', 'world', '.', 'This', 'is', 'a', 'test', '.']















## 2.3 Converting tokens into token IDs




result = re.split(r'([,.:;?_!"()\']|--|\s)', raw_txt)
result = [item.strip() for item in result if item.strip()]
print(len(result))
#4690


all_words = sorted(set(result))
print(all_words)
#['!', '"', "'", '(', ')', ',', '--', '.', ':', ';', '?', 'A', 'Ah', 'Among', 'And', 'Are', 'Arrt', 'As', 'At', 'Be', 'Begin', 'Burlington', 'But', 'By', 'Carlo', 'Chicago', 'Claude', 'Come', 'Croft', 'Destroyed', 'Devonshire', 'Don', 'Dubarry', 'Emperors', 'Florence', 'For', 'Gallery', 'Gideon', 'Gisburn', 'Gisburns', 'Grafton', 'Greek', 'Grindle', 'Grindles', 'HAD', 'Had', 'Hang', 'Has', 'He', 'Her', 'Hermia', 'His', 'How', 'I', 'If', 'In', 'It', 'Jack', 'Jove', 'Just', 'Lord', 'Made', 'Miss', 'Money', 'Monte', 'Moon-dancers', 'Mr', 'Mrs', 'My', 'Never', 'No', 'Now', 'Nutley', 'Of', 'Oh', 'On', 'Once', 'Only', 'Or', 'Perhaps', 'Poor', 'Professional', 'Renaissance', 'Rickham', 'Riviera', 'Rome', 'Russian', 'Sevres', 'She', 'Stroud', 'Strouds', 'Suddenly', 'That', 'The', 'Then', 'There', 'They', 'This', 'Those', 'Though', 'Thwing', 'Thwings', 'To', 'Usually', 'Venetian', 'Victor', 'Was', 'We', 'Well', 'What', 'When', 'Why', 'Yes', 'You', '_', 'a', 'abdication', 'able', 'about', 'above', 'abruptly', 'absolute', 'absorbed', 'absurdity', 'academic', 'accuse', 'accustomed', 'across', 'activity', 'add', 'added', 'admirers', 'adopted', 'adulation', 'advance', 'aesthetic', 'affect', 'afraid', 'after', 'afterward', 'again', 'ago', 'ah', 'air', 'alive', 'all', 'almost', 'alone', 'along', 'always', 'am', 'amazement', 'amid', 'among', 'amplest', 'amusing', 'an', 'and', 'another', 'answer', 'answered', 'any', 'anything', 'anywhere', 'apparent', 'apparently', 'appearance', 'appeared', 'appointed', 'are', 'arm', 'arm-chair', 'arm-chairs', 'arms', 'art', 'articles', 'artist', 'as', 'aside', 'asked', 'at', 'atmosphere', 'atom', 'attack', 'attention', 'attitude', 'audacities', 'away', 'awful', 'axioms', 'azaleas', 'back', 'background', 'balance', 'balancing', 'balustraded', 'basking', 'bath-rooms', 'be', 'beaming', 'bean-stalk', 'bear', 'beard', 'beauty', 'became', 'because', 'becoming', 'bed', 'been', 'before', 'began', 'begun', 'behind', 'being', 'believed', 'beneath', 'bespoke', 'better', 'between', 'big', 'bits', 'bitterness', 'blocked', 'born', 'borne', 'boudoir', 'bravura', 'break', 'breaking', 'breathing', 'bric-a-brac', 'briefly', 'brings', 'bronzes', 'brought', 'brown', 'brush', 'bull', 'business', 'but', 'buying', 'by', 'called', 'came', 'can', 'canvas', 'canvases', 'cards', 'care', 'career', 'caught', 'central', 'chair', 'chap', 'characteristic', 'charming', 'cheap', 'check', 'cheeks', 'chest', 'chimney-piece', 'chucked', 'cigar', 'cigarette', 'cigars', 'circulation', 'circumstance', 'circus-clown', 'claimed', 'clasping', 'clear', 'cleverer', 'close', 'clue', 'coat', 'collapsed', 'colour', 'come', 'comfortable', 'coming', 'companion', 'compared', 'complex', 'confident', 'congesting', 'conjugal', 'constraint', 'consummate', 'contended', 'continued', 'corner', 'corrected', 'could', 'couldn', 'count', 'countenance', 'couple', 'course', 'covered', 'craft', 'cried', 'crossed', 'crowned', 'crumbled', 'cry', 'cured', 'curiosity', 'curious', 'current', 'curtains', 'd', 'dabble', 'damask', 'dark', 'dashed', 'day', 'days', 'dead', 'deadening', 'dear', 'deep', 'deerhound', 'degree', 'delicate', 'demand', 'denied', 'deploring', 'deprecating', 'deprecatingly', 'desire', 'destroyed', 'destruction', 'desultory', 'detail', 'diagnosis', 'did', 'didn', 'died', 'dim', 'dimmest', 'dingy', 'dining-room', 'disarming', 'discovery', 'discrimination', 'discussion', 'disdain', 'disdained', 'disease', 'disguised', 'display', 'dissatisfied', 'distinguished', 'distract', 'divert', 'do', 'doesn', 'doing', 'domestic', 'don', 'done', 'donkey', 'down', 'dozen', 'dragged', 'drawing-room', 'drawing-rooms', 'drawn', 'dress-closets', 'drew', 'dropped', 'each', 'earth', 'ease', 'easel', 'easy', 'echoed', 'economy', 'effect', 'effects', 'efforts', 'egregious', 'eighteenth-century', 'elbow', 'elegant', 'else', 'embarrassed', 'enabled', 'end', 'endless', 'enjoy', 'enlightenment', 'enough', 'ensuing', 'equally', 'equanimity', 'escape', 'established', 'etching', 'even', 'event', 'ever', 'everlasting', 'every', 'exasperated', 'except', 'excuse', 'excusing', 'existed', 'expected', 'exquisite', 'exquisitely', 'extenuation', 'exterminating', 'extracting', 'eye', 'eyebrows', 'eyes', 'face', 'faces', 'fact', 'faded', 'failed', 'failure', 'fair', 'faith', 'false', 'familiar', 'famille-verte', 'fancy', 'fashionable', 'fate', 'feather', 'feet', 'fell', 'fellow', 'felt', 'few', 'fewer', 'finality', 'find', 'fingers', 'first', 'fit', 'fitting', 'five', 'flash', 'flashed', 'florid', 'flowers', 'fluently', 'flung', 'follow', 'followed', 'fond', 'footstep', 'for', 'forced', 'forcing', 'forehead', 'foreign', 'foreseen', 'forgive', 'forgotten', 'form', 'formed', 'forming', 'forward', 'fostered', 'found', 'foundations', 'fragment', 'fragments', 'frame', 'frames', 'frequently', 'friend', 'from', 'full', 'fullest', 'furiously', 'furrowed', 'garlanded', 'garlands', 'gave', 'genial', 'genius', 'gesture', 'get', 'getting', 'give', 'given', 'glad', 'glanced', 'glimpse', 'gloried', 'glory', 'go', 'going', 'gone', 'good', 'good-breeding', 'good-humoured', 'got', 'grace', 'gradually', 'gray', 'grayish', 'great', 'greatest', 'greatness', 'grew', 'groping', 'growing', 'had', 'hadn', 'hair', 'half', 'half-light', 'half-mechanically', 'hall', 'hand', 'hands', 'handsome', 'hanging', 'happen', 'happened', 'hard', 'hardly', 'has', 'have', 'haven', 'having', 'he', 'head', 'hear', 'heard', 'heart', 'height', 'her', 'here', 'hermit', 'herself', 'hesitations', 'hide', 'high', 'him', 'himself', 'hint', 'his', 'history', 'holding', 'home', 'honour', 'hooded', 'hostess', 'hot-house', 'hour', 'hours', 'house', 'how', 'hung', 'husband', 'idea', 'idle', 'idling', 'if', 'immediately', 'in', 'incense', 'indifferent', 'inevitable', 'inevitably', 'inflexible', 'insensible', 'insignificant', 'instinctively', 'instructive', 'interesting', 'into', 'ironic', 'irony', 'irrelevance', 'irrevocable', 'is', 'it', 'its', 'itself', 'jardiniere', 'jealousy', 'just', 'keep', 'kept', 'kind', 'knees', 'knew', 'know', 'known', 'laid', 'lair', 'landing', 'language', 'last', 'late', 'later', 'latter', 'laugh', 'laughed', 'lay', 'leading', 'lean', 'learned', 'least', 'leathery', 'leave', 'led', 'left', 'leisure', 'lends', 'lent', 'let', 'lies', 'life', 'life-likeness', 'lift', 'lifted', 'light', 'lightly', 'like', 'liked', 'line', 'lines', 'lingered', 'lips', 'lit', 'little', 'live', 'll', 'loathing', 'long', 'longed', 'longer', 'look', 'looked', 'looking', 'lose', 'loss', 'lounging', 'lovely', 'lucky', 'lump', 'luncheon-table', 'luxury', 'lying', 'made', 'make', 'man', 'manage', 'managed', 'mantel-piece', 'marble', 'married', 'may', 'me', 'meant', 'mediocrity', 'medium', 'mentioned', 'mere', 'merely', 'met', 'might', 'mighty', 'millionaire', 'mine', 'minute', 'minutes', 'mirrors', 'modest', 'modesty', 'moment', 'money', 'monumental', 'mood', 'morbidly', 'more', 'most', 'mourn', 'mourned', 'moustache', 'moved', 'much', 'muddling', 'multiplied', 'murmur', 'muscles', 'must', 'my', 'myself', 'mysterious', 'naive', 'near', 'nearly', 'negatived', 'nervous', 'nervousness', 'neutral', 'never', 'next', 'no', 'none', 'not', 'note', 'nothing', 'now', 'nymphs', 'oak', 'obituary', 'object', 'objects', 'occurred', 'oddly', 'of', 'off', 'often', 'oh', 'old', 'on', 'once', 'one', 'ones', 'only', 'onto', 'open', 'or', 'other', 'our', 'ourselves', 'out', 'outline', 'oval', 'over', 'own', 'packed', 'paid', 'paint', 'painted', 'painter', 'painting', 'pale', 'paled', 'palm-trees', 'panel', 'panelling', 'pardonable', 'pardoned', 'part', 'passages', 'passing', 'past', 'pastels', 'pathos', 'patient', 'people', 'perceptible', 'perfect', 'persistence', 'persuasively', 'phrase', 'picture', 'pictures', 'pines', 'pink', 'place', 'placed', 'plain', 'platitudes', 'pleased', 'pockets', 'point', 'poised', 'poor', 'portrait', 'posing', 'possessed', 'poverty', 'predicted', 'preliminary', 'presenting', 'prestidigitation', 'pretty', 'previous', 'price', 'pride', 'princely', 'prism', 'problem', 'proclaiming', 'prodigious', 'profusion', 'protest', 'prove', 'public', 'purblind', 'purely', 'pushed', 'put', 'qualities', 'quality', 'queerly', 'question', 'quickly', 'quietly', 'quite', 'quote', 'rain', 'raised', 'random', 'rather', 're', 'real', 'really', 'reared', 'reason', 'reassurance', 'recovering', 'recreated', 'reflected', 'reflection', 'regrets', 'relatively', 'remained', 'remember', 'reminded', 'repeating', 'represented', 'reproduction', 'resented', 'resolve', 'resources', 'rest', 'rich', 'ridiculous', 'robbed', 'romantic', 'room', 'rose', 'rs', 'rule', 'run', 's', 'said', 'same', 'satisfaction', 'savour', 'saw', 'say', 'saying', 'says', 'scorn', 'scornful', 'secret', 'see', 'seemed', 'seen', 'self-confident', 'send', 'sensation', 'sensitive', 'sent', 'serious', 'set', 'sex', 'shade', 'shaking', 'shall', 'she', 'shirked', 'short', 'should', 'shoulder', 'shoulders', 'show', 'showed', 'showy', 'shrug', 'shrugged', 'sight', 'sign', 'silent', 'silver', 'similar', 'simpleton', 'simplifications', 'simply', 'since', 'single', 'sitter', 'sitters', 'sketch', 'skill', 'slight', 'slightly', 'slowly', 'small', 'smile', 'smiling', 'sneer', 'so', 'solace', 'some', 'somebody', 'something', 'spacious', 'spaniel', 'speaking-tubes', 'speculations', 'spite', 'splash', 'square', 'stairs', 'stammer', 'stand', 'standing', 'started', 'stay', 'still', 'stocked', 'stood', 'stopped', 'stopping', 'straddling', 'straight', 'strain', 'straining', 'strange', 'straw', 'stream', 'stroke', 'strokes', 'strolled', 'strongest', 'strongly', 'struck', 'studio', 'stuff', 'subject', 'substantial', 'suburban', 'such', 'suddenly', 'suffered', 'sugar', 'suggested', 'sunburn', 'sunburnt', 'sunlit', 'superb', 'sure', 'surest', 'surface', 'surprise', 'surprised', 'surrounded', 'suspected', 'sweetly', 'sweetness', 'swelling', 'swept', 'swum', 't', 'table', 'take', 'taken', 'talking', 'tea', 'tears', 'technicalities', 'technique', 'tell', 'tells', 'tempting', 'terra-cotta', 'terrace', 'terraces', 'terribly', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'therefore', 'they', 'thin', 'thing', 'things', 'think', 'this', 'thither', 'those', 'though', 'thought', 'three', 'threshold', 'threw', 'through', 'throwing', 'tie', 'till', 'time', 'timorously', 'tinge', 'tips', 'tired', 'to', 'told', 'tone', 'tones', 'too', 'took', 'tottering', 'touched', 'toward', 'trace', 'trade', 'transmute', 'traps', 'travelled', 'tribute', 'tributes', 'tricks', 'tried', 'trouser-presses', 'true', 'truth', 'turned', 'twenty', 'twenty-four', 'twice', 'twirling', 'unaccountable', 'uncertain', 'under', 'underlay', 'underneath', 'understand', 'unexpected', 'untouched', 'unusual', 'up', 'up-stream', 'upon', 'upset', 'upstairs', 'us', 'used', 'usual', 'value', 'varnishing', 'vases', 've', 'veins', 'velveteen', 'very', 'villa', 'vindicated', 'virtuosity', 'vista', 'vocation', 'voice', 'wall', 'wander', 'want', 'wanted', 'wants', 'was', 'wasn', 'watched', 'watching', 'water-colour', 'waves', 'way', 'weekly', 'weeks', 'welcome', 'went', 'were', 'what', 'when', 'whenever', 'where', 'which', 'while', 'white', 'white-panelled', 'who', 'whole', 'whom', 'why', 'wide', 'widow', 'wife', 'wild', 'wincing', 'window-curtains', 'wish', 'with', 'without', 'wits', 'woman', 'women', 'won', 'wonder', 'wondered', 'word', 'work', 'working', 'worth', 'would', 'wouldn', 'year', 'years', 'yellow', 'yet', 'you', 'younger', 'your', 'yourself']




vocab = {token:integer for integer,token in enumerate(all_words)}
print(vocab)
#{'!': 0, '"': 1, "'": 2, '(': 3, ')': 4, ',': 5, '--': 6, '.': 7, ':': 8, ';': 9, '?': 10, 'A': 11, 'Ah': 12, 'Among': 13, 'And': 14, 'Are': 15, 'Arrt': 16, 'As': 17, 'At': 18, 'Be': 19, 'Begin': 20, 'Burlington': 21, 'But': 22, 'By': 23, 'Carlo': 24, 'Chicago': 25, 'Claude': 26, 'Come': 27, 'Croft': 28, 'Destroyed': 29, 'Devonshire': 30, 'Don': 31, 'Dubarry': 32, 'Emperors': 33, 'Florence': 34, 'For': 35, 'Gallery': 36, 'Gideon': 37, 'Gisburn': 38, 'Gisburns': 39, 'Grafton': 40, 'Greek': 41, 'Grindle': 42, 'Grindles': 43, 'HAD': 44, 'Had': 45, 'Hang': 46, 'Has': 47, 'He': 48, 'Her': 49, 'Hermia': 50, 'His': 51, 'How': 52, 'I': 53, 'If': 54, 'In': 55, 'It': 56, 'Jack': 57, 'Jove': 58, 'Just': 59, 'Lord': 60, 'Made': 61, 'Miss': 62, 'Money': 63, 'Monte': 64, 'Moon-dancers': 65, 'Mr': 66, 'Mrs': 67, 'My': 68, 'Never': 69, 'No': 70, 'Now': 71, 'Nutley': 72, 'Of': 73, 'Oh': 74, 'On': 75, 'Once': 76, 'Only': 77, 'Or': 78, 'Perhaps': 79, 'Poor': 80, 'Professional': 81, 'Renaissance': 82, 'Rickham': 83, 'Riviera': 84, 'Rome': 85, 'Russian': 86, 'Sevres': 87, 'She': 88, 'Stroud': 89, 'Strouds': 90, 'Suddenly': 91, 'That': 92, 'The': 93, 'Then': 94, 'There': 95, 'They': 96, 'This': 97, 'Those': 98, 'Though': 99, 'Thwing': 100, 'Thwings': 101, 'To': 102, 'Usually': 103, 'Venetian': 104, 'Victor': 105, 'Was': 106, 'We': 107, 'Well': 108, 'What': 109, 'When': 110, 'Why': 111, 'Yes': 112, 'You': 113, '_': 114, 'a': 115, 'abdication': 116, 'able': 117, 'about': 118, 'above': 119, 'abruptly': 120, 'absolute': 121, 'absorbed': 122, 'absurdity': 123, 'academic': 124, 'accuse': 125, 'accustomed': 126, 'across': 127, 'activity': 128, 'add': 129, 'added': 130, 'admirers': 131, 'adopted': 132, 'adulation': 133, 'advance': 134, 'aesthetic': 135, 'affect': 136, 'afraid': 137, 'after': 138, 'afterward': 139, 'again': 140, 'ago': 141, 'ah': 142, 'air': 143, 'alive': 144, 'all': 145, 'almost': 146, 'alone': 147, 'along': 148, 'always': 149, 'am': 150, 'amazement': 151, 'amid': 152, 'among': 153, 'amplest': 154, 'amusing': 155, 'an': 156, 'and': 157, 'another': 158, 'answer': 159, 'answered': 160, 'any': 161, 'anything': 162, 'anywhere': 163, 'apparent': 164, 'apparently': 165, 'appearance': 166, 'appeared': 167, 'appointed': 168, 'are': 169, 'arm': 170, 'arm-chair': 171, 'arm-chairs': 172, 'arms': 173, 'art': 174, 'articles': 175, 'artist': 176, 'as': 177, 'aside': 178, 'asked': 179, 'at': 180, 'atmosphere': 181, 'atom': 182, 'attack': 183, 'attention': 184, 'attitude': 185, 'audacities': 186, 'away': 187, 'awful': 188, 'axioms': 189, 'azaleas': 190, 'back': 191, 'background': 192, 'balance': 193, 'balancing': 194, 'balustraded': 195, 'basking': 196, 'bath-rooms': 197, 'be': 198, 'beaming': 199, 'bean-stalk': 200, 'bear': 201, 'beard': 202, 'beauty': 203, 'became': 204, 'because': 205, 'becoming': 206, 'bed': 207, 'been': 208, 'before': 209, 'began': 210, 'begun': 211, 'behind': 212, 'being': 213, 'believed': 214, 'beneath': 215, 'bespoke': 216, 'better': 217, 'between': 218, 'big': 219, 'bits': 220, 'bitterness': 221, 'blocked': 222, 'born': 223, 'borne': 224, 'boudoir': 225, 'bravura': 226, 'break': 227, 'breaking': 228, 'breathing': 229, 'bric-a-brac': 230, 'briefly': 231, 'brings': 232, 'bronzes': 233, 'brought': 234, 'brown': 235, 'brush': 236, 'bull': 237, 'business': 238, 'but': 239, 'buying': 240, 'by': 241, 'called': 242, 'came': 243, 'can': 244, 'canvas': 245, 'canvases': 246, 'cards': 247, 'care': 248, 'career': 249, 'caught': 250, 'central': 251, 'chair': 252, 'chap': 253, 'characteristic': 254, 'charming': 255, 'cheap': 256, 'check': 257, 'cheeks': 258, 'chest': 259, 'chimney-piece': 260, 'chucked': 261, 'cigar': 262, 'cigarette': 263, 'cigars': 264, 'circulation': 265, 'circumstance': 266, 'circus-clown': 267, 'claimed': 268, 'clasping': 269, 'clear': 270, 'cleverer': 271, 'close': 272, 'clue': 273, 'coat': 274, 'collapsed': 275, 'colour': 276, 'come': 277, 'comfortable': 278, 'coming': 279, 'companion': 280, 'compared': 281, 'complex': 282, 'confident': 283, 'congesting': 284, 'conjugal': 285, 'constraint': 286, 'consummate': 287, 'contended': 288, 'continued': 289, 'corner': 290, 'corrected': 291, 'could': 292, 'couldn': 293, 'count': 294, 'countenance': 295, 'couple': 296, 'course': 297, 'covered': 298, 'craft': 299, 'cried': 300, 'crossed': 301, 'crowned': 302, 'crumbled': 303, 'cry': 304, 'cured': 305, 'curiosity': 306, 'curious': 307, 'current': 308, 'curtains': 309, 'd': 310, 'dabble': 311, 'damask': 312, 'dark': 313, 'dashed': 314, 'day': 315, 'days': 316, 'dead': 317, 'deadening': 318, 'dear': 319, 'deep': 320, 'deerhound': 321, 'degree': 322, 'delicate': 323, 'demand': 324, 'denied': 325, 'deploring': 326, 'deprecating': 327, 'deprecatingly': 328, 'desire': 329, 'destroyed': 330, 'destruction': 331, 'desultory': 332, 'detail': 333, 'diagnosis': 334, 'did': 335, 'didn': 336, 'died': 337, 'dim': 338, 'dimmest': 339, 'dingy': 340, 'dining-room': 341, 'disarming': 342, 'discovery': 343, 'discrimination': 344, 'discussion': 345, 'disdain': 346, 'disdained': 347, 'disease': 348, 'disguised': 349, 'display': 350, 'dissatisfied': 351, 'distinguished': 352, 'distract': 353, 'divert': 354, 'do': 355, 'doesn': 356, 'doing': 357, 'domestic': 358, 'don': 359, 'done': 360, 'donkey': 361, 'down': 362, 'dozen': 363, 'dragged': 364, 'drawing-room': 365, 'drawing-rooms': 366, 'drawn': 367, 'dress-closets': 368, 'drew': 369, 'dropped': 370, 'each': 371, 'earth': 372, 'ease': 373, 'easel': 374, 'easy': 375, 'echoed': 376, 'economy': 377, 'effect': 378, 'effects': 379, 'efforts': 380, 'egregious': 381, 'eighteenth-century': 382, 'elbow': 383, 'elegant': 384, 'else': 385, 'embarrassed': 386, 'enabled': 387, 'end': 388, 'endless': 389, 'enjoy': 390, 'enlightenment': 391, 'enough': 392, 'ensuing': 393, 'equally': 394, 'equanimity': 395, 'escape': 396, 'established': 397, 'etching': 398, 'even': 399, 'event': 400, 'ever': 401, 'everlasting': 402, 'every': 403, 'exasperated': 404, 'except': 405, 'excuse': 406, 'excusing': 407, 'existed': 408, 'expected': 409, 'exquisite': 410, 'exquisitely': 411, 'extenuation': 412, 'exterminating': 413, 'extracting': 414, 'eye': 415, 'eyebrows': 416, 'eyes': 417, 'face': 418, 'faces': 419, 'fact': 420, 'faded': 421, 'failed': 422, 'failure': 423, 'fair': 424, 'faith': 425, 'false': 426, 'familiar': 427, 'famille-verte': 428, 'fancy': 429, 'fashionable': 430, 'fate': 431, 'feather': 432, 'feet': 433, 'fell': 434, 'fellow': 435, 'felt': 436, 'few': 437, 'fewer': 438, 'finality': 439, 'find': 440, 'fingers': 441, 'first': 442, 'fit': 443, 'fitting': 444, 'five': 445, 'flash': 446, 'flashed': 447, 'florid': 448, 'flowers': 449, 'fluently': 450, 'flung': 451, 'follow': 452, 'followed': 453, 'fond': 454, 'footstep': 455, 'for': 456, 'forced': 457, 'forcing': 458, 'forehead': 459, 'foreign': 460, 'foreseen': 461, 'forgive': 462, 'forgotten': 463, 'form': 464, 'formed': 465, 'forming': 466, 'forward': 467, 'fostered': 468, 'found': 469, 'foundations': 470, 'fragment': 471, 'fragments': 472, 'frame': 473, 'frames': 474, 'frequently': 475, 'friend': 476, 'from': 477, 'full': 478, 'fullest': 479, 'furiously': 480, 'furrowed': 481, 'garlanded': 482, 'garlands': 483, 'gave': 484, 'genial': 485, 'genius': 486, 'gesture': 487, 'get': 488, 'getting': 489, 'give': 490, 'given': 491, 'glad': 492, 'glanced': 493, 'glimpse': 494, 'gloried': 495, 'glory': 496, 'go': 497, 'going': 498, 'gone': 499, 'good': 500, 'good-breeding': 501, 'good-humoured': 502, 'got': 503, 'grace': 504, 'gradually': 505, 'gray': 506, 'grayish': 507, 'great': 508, 'greatest': 509, 'greatness': 510, 'grew': 511, 'groping': 512, 'growing': 513, 'had': 514, 'hadn': 515, 'hair': 516, 'half': 517, 'half-light': 518, 'half-mechanically': 519, 'hall': 520, 'hand': 521, 'hands': 522, 'handsome': 523, 'hanging': 524, 'happen': 525, 'happened': 526, 'hard': 527, 'hardly': 528, 'has': 529, 'have': 530, 'haven': 531, 'having': 532, 'he': 533, 'head': 534, 'hear': 535, 'heard': 536, 'heart': 537, 'height': 538, 'her': 539, 'here': 540, 'hermit': 541, 'herself': 542, 'hesitations': 543, 'hide': 544, 'high': 545, 'him': 546, 'himself': 547, 'hint': 548, 'his': 549, 'history': 550, 'holding': 551, 'home': 552, 'honour': 553, 'hooded': 554, 'hostess': 555, 'hot-house': 556, 'hour': 557, 'hours': 558, 'house': 559, 'how': 560, 'hung': 561, 'husband': 562, 'idea': 563, 'idle': 564, 'idling': 565, 'if': 566, 'immediately': 567, 'in': 568, 'incense': 569, 'indifferent': 570, 'inevitable': 571, 'inevitably': 572, 'inflexible': 573, 'insensible': 574, 'insignificant': 575, 'instinctively': 576, 'instructive': 577, 'interesting': 578, 'into': 579, 'ironic': 580, 'irony': 581, 'irrelevance': 582, 'irrevocable': 583, 'is': 584, 'it': 585, 'its': 586, 'itself': 587, 'jardiniere': 588, 'jealousy': 589, 'just': 590, 'keep': 591, 'kept': 592, 'kind': 593, 'knees': 594, 'knew': 595, 'know': 596, 'known': 597, 'laid': 598, 'lair': 599, 'landing': 600, 'language': 601, 'last': 602, 'late': 603, 'later': 604, 'latter': 605, 'laugh': 606, 'laughed': 607, 'lay': 608, 'leading': 609, 'lean': 610, 'learned': 611, 'least': 612, 'leathery': 613, 'leave': 614, 'led': 615, 'left': 616, 'leisure': 617, 'lends': 618, 'lent': 619, 'let': 620, 'lies': 621, 'life': 622, 'life-likeness': 623, 'lift': 624, 'lifted': 625, 'light': 626, 'lightly': 627, 'like': 628, 'liked': 629, 'line': 630, 'lines': 631, 'lingered': 632, 'lips': 633, 'lit': 634, 'little': 635, 'live': 636, 'll': 637, 'loathing': 638, 'long': 639, 'longed': 640, 'longer': 641, 'look': 642, 'looked': 643, 'looking': 644, 'lose': 645, 'loss': 646, 'lounging': 647, 'lovely': 648, 'lucky': 649, 'lump': 650, 'luncheon-table': 651, 'luxury': 652, 'lying': 653, 'made': 654, 'make': 655, 'man': 656, 'manage': 657, 'managed': 658, 'mantel-piece': 659, 'marble': 660, 'married': 661, 'may': 662, 'me': 663, 'meant': 664, 'mediocrity': 665, 'medium': 666, 'mentioned': 667, 'mere': 668, 'merely': 669, 'met': 670, 'might': 671, 'mighty': 672, 'millionaire': 673, 'mine': 674, 'minute': 675, 'minutes': 676, 'mirrors': 677, 'modest': 678, 'modesty': 679, 'moment': 680, 'money': 681, 'monumental': 682, 'mood': 683, 'morbidly': 684, 'more': 685, 'most': 686, 'mourn': 687, 'mourned': 688, 'moustache': 689, 'moved': 690, 'much': 691, 'muddling': 692, 'multiplied': 693, 'murmur': 694, 'muscles': 695, 'must': 696, 'my': 697, 'myself': 698, 'mysterious': 699, 'naive': 700, 'near': 701, 'nearly': 702, 'negatived': 703, 'nervous': 704, 'nervousness': 705, 'neutral': 706, 'never': 707, 'next': 708, 'no': 709, 'none': 710, 'not': 711, 'note': 712, 'nothing': 713, 'now': 714, 'nymphs': 715, 'oak': 716, 'obituary': 717, 'object': 718, 'objects': 719, 'occurred': 720, 'oddly': 721, 'of': 722, 'off': 723, 'often': 724, 'oh': 725, 'old': 726, 'on': 727, 'once': 728, 'one': 729, 'ones': 730, 'only': 731, 'onto': 732, 'open': 733, 'or': 734, 'other': 735, 'our': 736, 'ourselves': 737, 'out': 738, 'outline': 739, 'oval': 740, 'over': 741, 'own': 742, 'packed': 743, 'paid': 744, 'paint': 745, 'painted': 746, 'painter': 747, 'painting': 748, 'pale': 749, 'paled': 750, 'palm-trees': 751, 'panel': 752, 'panelling': 753, 'pardonable': 754, 'pardoned': 755, 'part': 756, 'passages': 757, 'passing': 758, 'past': 759, 'pastels': 760, 'pathos': 761, 'patient': 762, 'people': 763, 'perceptible': 764, 'perfect': 765, 'persistence': 766, 'persuasively': 767, 'phrase': 768, 'picture': 769, 'pictures': 770, 'pines': 771, 'pink': 772, 'place': 773, 'placed': 774, 'plain': 775, 'platitudes': 776, 'pleased': 777, 'pockets': 778, 'point': 779, 'poised': 780, 'poor': 781, 'portrait': 782, 'posing': 783, 'possessed': 784, 'poverty': 785, 'predicted': 786, 'preliminary': 787, 'presenting': 788, 'prestidigitation': 789, 'pretty': 790, 'previous': 791, 'price': 792, 'pride': 793, 'princely': 794, 'prism': 795, 'problem': 796, 'proclaiming': 797, 'prodigious': 798, 'profusion': 799, 'protest': 800, 'prove': 801, 'public': 802, 'purblind': 803, 'purely': 804, 'pushed': 805, 'put': 806, 'qualities': 807, 'quality': 808, 'queerly': 809, 'question': 810, 'quickly': 811, 'quietly': 812, 'quite': 813, 'quote': 814, 'rain': 815, 'raised': 816, 'random': 817, 'rather': 818, 're': 819, 'real': 820, 'really': 821, 'reared': 822, 'reason': 823, 'reassurance': 824, 'recovering': 825, 'recreated': 826, 'reflected': 827, 'reflection': 828, 'regrets': 829, 'relatively': 830, 'remained': 831, 'remember': 832, 'reminded': 833, 'repeating': 834, 'represented': 835, 'reproduction': 836, 'resented': 837, 'resolve': 838, 'resources': 839, 'rest': 840, 'rich': 841, 'ridiculous': 842, 'robbed': 843, 'romantic': 844, 'room': 845, 'rose': 846, 'rs': 847, 'rule': 848, 'run': 849, 's': 850, 'said': 851, 'same': 852, 'satisfaction': 853, 'savour': 854, 'saw': 855, 'say': 856, 'saying': 857, 'says': 858, 'scorn': 859, 'scornful': 860, 'secret': 861, 'see': 862, 'seemed': 863, 'seen': 864, 'self-confident': 865, 'send': 866, 'sensation': 867, 'sensitive': 868, 'sent': 869, 'serious': 870, 'set': 871, 'sex': 872, 'shade': 873, 'shaking': 874, 'shall': 875, 'she': 876, 'shirked': 877, 'short': 878, 'should': 879, 'shoulder': 880, 'shoulders': 881, 'show': 882, 'showed': 883, 'showy': 884, 'shrug': 885, 'shrugged': 886, 'sight': 887, 'sign': 888, 'silent': 889, 'silver': 890, 'similar': 891, 'simpleton': 892, 'simplifications': 893, 'simply': 894, 'since': 895, 'single': 896, 'sitter': 897, 'sitters': 898, 'sketch': 899, 'skill': 900, 'slight': 901, 'slightly': 902, 'slowly': 903, 'small': 904, 'smile': 905, 'smiling': 906, 'sneer': 907, 'so': 908, 'solace': 909, 'some': 910, 'somebody': 911, 'something': 912, 'spacious': 913, 'spaniel': 914, 'speaking-tubes': 915, 'speculations': 916, 'spite': 917, 'splash': 918, 'square': 919, 'stairs': 920, 'stammer': 921, 'stand': 922, 'standing': 923, 'started': 924, 'stay': 925, 'still': 926, 'stocked': 927, 'stood': 928, 'stopped': 929, 'stopping': 930, 'straddling': 931, 'straight': 932, 'strain': 933, 'straining': 934, 'strange': 935, 'straw': 936, 'stream': 937, 'stroke': 938, 'strokes': 939, 'strolled': 940, 'strongest': 941, 'strongly': 942, 'struck': 943, 'studio': 944, 'stuff': 945, 'subject': 946, 'substantial': 947, 'suburban': 948, 'such': 949, 'suddenly': 950, 'suffered': 951, 'sugar': 952, 'suggested': 953, 'sunburn': 954, 'sunburnt': 955, 'sunlit': 956, 'superb': 957, 'sure': 958, 'surest': 959, 'surface': 960, 'surprise': 961, 'surprised': 962, 'surrounded': 963, 'suspected': 964, 'sweetly': 965, 'sweetness': 966, 'swelling': 967, 'swept': 968, 'swum': 969, 't': 970, 'table': 971, 'take': 972, 'taken': 973, 'talking': 974, 'tea': 975, 'tears': 976, 'technicalities': 977, 'technique': 978, 'tell': 979, 'tells': 980, 'tempting': 981, 'terra-cotta': 982, 'terrace': 983, 'terraces': 984, 'terribly': 985, 'than': 986, 'that': 987, 'the': 988, 'their': 989, 'them': 990, 'then': 991, 'there': 992, 'therefore': 993, 'they': 994, 'thin': 995, 'thing': 996, 'things': 997, 'think': 998, 'this': 999, 'thither': 1000, 'those': 1001, 'though': 1002, 'thought': 1003, 'three': 1004, 'threshold': 1005, 'threw': 1006, 'through': 1007, 'throwing': 1008, 'tie': 1009, 'till': 1010, 'time': 1011, 'timorously': 1012, 'tinge': 1013, 'tips': 1014, 'tired': 1015, 'to': 1016, 'told': 1017, 'tone': 1018, 'tones': 1019, 'too': 1020, 'took': 1021, 'tottering': 1022, 'touched': 1023, 'toward': 1024, 'trace': 1025, 'trade': 1026, 'transmute': 1027, 'traps': 1028, 'travelled': 1029, 'tribute': 1030, 'tributes': 1031, 'tricks': 1032, 'tried': 1033, 'trouser-presses': 1034, 'true': 1035, 'truth': 1036, 'turned': 1037, 'twenty': 1038, 'twenty-four': 1039, 'twice': 1040, 'twirling': 1041, 'unaccountable': 1042, 'uncertain': 1043, 'under': 1044, 'underlay': 1045, 'underneath': 1046, 'understand': 1047, 'unexpected': 1048, 'untouched': 1049, 'unusual': 1050, 'up': 1051, 'up-stream': 1052, 'upon': 1053, 'upset': 1054, 'upstairs': 1055, 'us': 1056, 'used': 1057, 'usual': 1058, 'value': 1059, 'varnishing': 1060, 'vases': 1061, 've': 1062, 'veins': 1063, 'velveteen': 1064, 'very': 1065, 'villa': 1066, 'vindicated': 1067, 'virtuosity': 1068, 'vista': 1069, 'vocation': 1070, 'voice': 1071, 'wall': 1072, 'wander': 1073, 'want': 1074, 'wanted': 1075, 'wants': 1076, 'was': 1077, 'wasn': 1078, 'watched': 1079, 'watching': 1080, 'water-colour': 1081, 'waves': 1082, 'way': 1083, 'weekly': 1084, 'weeks': 1085, 'welcome': 1086, 'went': 1087, 'were': 1088, 'what': 1089, 'when': 1090, 'whenever': 1091, 'where': 1092, 'which': 1093, 'while': 1094, 'white': 1095, 'white-panelled': 1096, 'who': 1097, 'whole': 1098, 'whom': 1099, 'why': 1100, 'wide': 1101, 'widow': 1102, 'wife': 1103, 'wild': 1104, 'wincing': 1105, 'window-curtains': 1106, 'wish': 1107, 'with': 1108, 'without': 1109, 'wits': 1110, 'woman': 1111, 'women': 1112, 'won': 1113, 'wonder': 1114, 'wondered': 1115, 'word': 1116, 'work': 1117, 'working': 1118, 'worth': 1119, 'would': 1120, 'wouldn': 1121, 'year': 1122, 'years': 1123, 'yellow': 1124, 'yet': 1125, 'you': 1126, 'younger': 1127, 'your': 1128, 'yourself': 1129}



class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i: s for s, i in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)

        preprocessed = [
            item.strip() for item in preprocessed if item.strip()]

        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        # Replace spaces before the specified punctuations
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
        return text



token = SimpleTokenizerV1(vocab)

text = """This is a to to how to word,
            " There", said"""

ids = token.encode(text)
print(ids)
#[97, 584, 115, 1016, 1016, 560, 1016, 1116, 5, 1, 95, 1, 5, 851]


ids_2 = token.decode(ids)
print(ids_2)
#This is a to to how to word," There", said















## 2.4 Adding special context tokens


preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_txt)
preprocessed = [item.strip() for item in preprocessed if item.strip()]

all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])


vocab = {token:integer for integer,token in enumerate(all_tokens)}
print(vocab)

print(len(vocab.items()))
#1132


class SimpleTokenizerV2:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i: s for s, i in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        preprocessed = [
            item if item in self.str_to_int
            else "<|unk|>" for item in preprocessed
        ]

        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        # Replace spaces before the specified punctuations
        text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text)
        return text



my_text = "Now this new sentence will be the reason why the new function works"

token_2 = SimpleTokenizerV2(vocab)

x = token_2.encode(my_text)
print(x)
#[71, 999, 1131, 1131, 1131, 198, 988, 823, 1100, 988, 1131, 1131, 1131]
















## 2.5 BytePair encoding

import tiktoken


print(tiktoken.__version__)
#0.9.0

tokenizer = tiktoken.get_encoding("gpt2")
# SAME AS ids = token.encode(text)



one = tokenizer.encode("Hello, world!")
print(one)
#[15496, 11, 995, 0]



text = ("hello, do you like tea? <|endoftext|> In the sunlit terraces"
        "This is a new line")
#two = tokenizer.encode(text)
#print(two)


two = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
print(two)
#[31373, 11, 466, 345, 588, 8887, 30, 220, 50256, 554, 262, 4252, 18250, 8812, 2114, 1212, 318, 257, 649, 1627]















## 2.6 Data sampling with a sliding window


text_verdict = open("/Users/benjaminbrooke/PycharmProjects/Blue-Ocean/Data/The Verdict.txt","r",encoding="utf-8")
raw_txt = text_verdict.read()

enc_text = tokenizer.encode(raw_txt)
print(len(enc_text))
#5145

enc_sample = enc_text[50:]

context_size = 4

x = enc_sample[:context_size]
y = enc_sample[1:context_size+1]

print(f"x: {x}")
print(f"y:      {y}")
#x: [290, 4920, 2241, 287]
#y:      [4920, 2241, 287, 257]





for i in range(1, context_size+1):
    context = enc_sample[:i]
    desired = enc_sample[i]

    print(context, "---->", desired)

#[290] ----> 4920
#[290, 4920] ----> 2241
#[290, 4920, 2241] ----> 287
#[290, 4920, 2241, 287] ----> 257





import torch
print(torch.__version__)
#2.7.1





from torch.utils.data import Dataset, DataLoader


class GPTDatasetV1(Dataset):
    def __init__(self, txt, tokenizer, max_length, stride):
        self.input_ids = []
        self.target_ids = []

        # Tokenize the entire text
        token_ids = tokenizer.encode(txt, allowed_special={"<|endoftext|>"})
        assert len(token_ids) > max_length, "Number of tokenized inputs must at least be equal to max_length+1"

        # Use a sliding window to chunk the book into overlapping sequences of max_length
        for i in range(0, len(token_ids) - max_length, stride):
            input_chunk = token_ids[i:i + max_length]
            target_chunk = token_ids[i + 1: i + max_length + 1]
            self.input_ids.append(torch.tensor(input_chunk))
            self.target_ids.append(torch.tensor(target_chunk))

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return self.input_ids[idx], self.target_ids[idx]






def create_dataloader_v1(txt, batch_size=4, max_length=256,
                         stride=128, shuffle=True, drop_last=True,
                         num_workers=0):

    # Initialize the tokenizer
    tokenizer = tiktoken.get_encoding("gpt2")

    # Create dataset
    dataset = GPTDatasetV1(txt, tokenizer, max_length, stride)

    # Create dataloader
    dataloader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        drop_last=drop_last,
        num_workers=num_workers
    )

    return dataloader









dataloader = create_dataloader_v1(
    raw_txt, batch_size=1, max_length=4, stride=1, shuffle=False
)

data_iter = iter(dataloader)
first_batch = next(data_iter)
print(first_batch)
#[tensor([[  40,  367, 2885, 1464]]), tensor([[ 367, 2885, 1464, 1807]])]



second_batch = next(data_iter)
print(second_batch)
#[tensor([[ 367, 2885, 1464, 1807]]), tensor([[2885, 1464, 1807, 3619]])]
















## 2.7 Creating token embeddings

inputs_ids = torch.tensor([2 , 3, 5 , 1])

vocab_size = 6
output_dim = 3

torch.manual_seed(123)
embedding_layer = torch.nn.Embedding(vocab_size,output_dim)

print(embedding_layer.weight)
"""
Parameter containing:
tensor([[ 0.3374, -0.1778, -0.1690],
        [ 0.9178,  1.5810,  1.3010],
        [ 1.2753, -0.2010, -0.1606],
        [-0.4015,  0.9666, -1.1481],
        [-1.1589,  0.3255, -0.6315],
        [-2.8400, -0.7849, -1.4096]], requires_grad=True)
"""

print(embedding_layer(torch.tensor([3])))
#tensor([[-0.4015,  0.9666, -1.1481]], grad_fn=<EmbeddingBackward0>)












## 2.8 Encoding word positions

vocab_size = 50257
output_dim = 256

token_embedding_layer = torch.nn.Embedding(vocab_size, output_dim)

max_length = 4
dataloader = create_dataloader_v1(
    raw_txt, batch_size=8, max_length=max_length,
    stride=max_length, shuffle=False
)
data_iter = iter(dataloader)
inputs, targets = next(data_iter)


context_length = max_length
pos_embedding_layer = torch.nn.Embedding(context_length, output_dim)

# uncomment & execute the following line to see how the embedding layer weights look like
# print(pos_embedding_layer.weight)


pos_embeddings = pos_embedding_layer(torch.arange(max_length))

print(pos_embeddings.shape)
#torch.Size([4, 256])











































