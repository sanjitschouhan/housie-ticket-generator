import pandas as pd

codes = dict()


def get_filled(code):
    return codes.get(code, set())


def add_value(code, num):
    codes[code] = codes.get(code, set())
    codes[code].add(int(num))


def format_filled(val, code):
    filled = get_filled(code)
    if val in filled:
        return "background: red;"
    else:
        return ""


def get_matrix(code):
    matrix = pd.DataFrame([[j for j in range(i, i + 10)] for i in range(1, 90, 10)])
    return (matrix.style
            .applymap(format_filled, code=code)
            .set_table_styles(
        [
            {
                'selector': 'th', 'props': [('display', 'None')]
            },
            {
                'selector': 'td', 'props': [('padding', '10px')]
            },
        ])
            .set_table_attributes("border=1")
            .render())
