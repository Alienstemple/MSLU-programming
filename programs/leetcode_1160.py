class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        # дано
        # список слов, строка с доступными буквами

        # найти
        # сумму длин строк, все буквы которых присутствуют в chars

        # ограничения, краевые случаи
        # длины всех строк и chars >= 1
        # буква встречается несколько раз
        # chars = "abacd". "aghdghagdhga"

        # алгоритм

        # 1. Хеш-таблица доступных букв: буква -> сколько раз встретилась
        count = {} # Counter(chars)
        for c in chars:
            count[c] = count.get(key = 'a', default = 0) + 1 # 2

        res = 0
        for w in words:
            # 2. Своя хеш-таблица для каждого слова: буква -> сколько потратили
            cur = {}
            good = True
            for c in w:
                cur[c] = cur.get(c, 0) + 1
                # 3. Потратили больше, чем есть (или буквы нет совсем: get вернёт 0)
                if cur[c] > count.get(c, 0):
                    good = False
                    break                 # досрочный выход, остаток слова не смотрим
            if good:
                res += len(w)
        # вернуть
        return res

       # Сложность временная - O(len(chars) + L(сумм длина всех words)), пространственная - O(1) (max 26 ключей в словаре)