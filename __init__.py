from grammar_macro import grammar
import openpyxl

if __name__ == '__main__':
    wb = openpyxl.load_workbook(
        '/Users/hyoseok/Desktop/WeeklySurvey_NeedCleaningUntil2022July31.xlsx')
    
    ws = wb.active
    spell = grammar()
    spell.open_grammar()

    for i in range(2, 20):
        str_before = ws.cell(row=i, column=5).value
        if str_before == 'NULL':
            continue
        else:
            ws.cell(row=i, column=8).value = spell.spell_check(str_before)

    wb.save(
        '/Users/hyoseok/Desktop/WeeklySurvey_NeedCleaningUntil2022July31.xlsx')