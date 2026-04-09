import random
from flask import Flask, render_template, request

app = Flask(__name__)

normal_fortunes = [
    "오늘은 작은 기회가 큰 결과로 이어질 수 있어요.",
    "뜻밖의 만남이 기다리고 있습니다.",
    "지갑을 조심하세요.",
    "오늘은 무리하지 않는 것이 중요합니다.",
    "작은 선택이 하루를 바꿉니다.",
    "친구와의 시간이 행운을 불러옵니다.",
    "조금만 더 노력하면 결과가 따라옵니다.",
    "오늘은 집중력이 중요한 날입니다.",
    "예상치 못한 지출이 생길 수 있어요.",
    "새로운 도전을 해보세요.",
    "좋은 소식이 들려올 수 있습니다.",
    "평소보다 신중하게 행동하세요.",
    "운이 서서히 따라오는 날입니다.",
    "사소한 실수를 조심하세요.",
    "오늘은 여유를 가지는 것이 좋습니다.",
    "감정 조절이 중요한 하루입니다.",
    "작은 행운이 숨어 있습니다.",
    "주변 사람을 잘 챙겨보세요.",
    "뜻밖의 기회가 찾아옵니다.",
    "지금 선택이 중요합니다.",
    "오늘은 조용히 보내는 게 좋습니다.",
    "계획대로 일이 풀릴 가능성이 높아요.",
    "새로운 아이디어가 떠오릅니다.",
    "도움을 받게 되는 날입니다.",
    "기다리던 일이 진행됩니다.",
    "오늘은 타이밍이 중요합니다.",
    "무리하지 않으면 좋은 결과가 있습니다.",
    "행동보다 생각이 필요한 날입니다.",
    "오늘은 평온한 하루가 될 것입니다.",
    "작은 용기가 큰 변화를 만듭니다."
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fortune', methods=['POST'])
def fortune():
    name = request.form['name']
    return render_template('fortune.html', name=name)

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']

    r = random.randint(1, 100)

    if r <= 4:
        fortune_title = "💀 최악의 운세"
        fortune_text = "오늘은 모든 선택을 조심하세요. 특히 돈과 인간관계 주의."
        stars = 1

    elif r <= 8:
        fortune_title = "🌟 최고의 운세"
        fortune_text = "오늘은 무엇을 해도 잘 풀리는 날! 기회를 놓치지 마세요."
        stars = 5

    else:
        fortune_title = "🔮 오늘의 운세"
        fortune_text = random.choice(normal_fortunes)
        stars = random.randint(2, 4)

    return render_template('result.html',
                           name=name,
                           fortune_title=fortune_title,
                           fortune_text=fortune_text,
                           stars=stars)

if __name__ == '__main__':
    app.run(debug=True)