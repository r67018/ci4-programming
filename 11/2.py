import random
random.seed(8)

class kSAT:
    @classmethod
    def generate(cls, k, var_num, clause_num):
        ksat = cls()
        var_list = list(range(var_num))
        res = []
        while len(res) < clause_num:
            clause = []
            clause_size = random.randint(1, k)
            for i in random.sample(var_list, clause_size):
                prefix = random.choice((0, 1))
                clause.append((prefix, i))
            clause.sort(key=lambda x: x[1])
            if clause not in res:
                res.append(clause)
        ksat.body = res
        return ksat

    def test(self, var_list):
        res = []
        for clause in self.body:
            clause_data = [not var_list[i] if p else var_list[i] for p, i in clause]
            res.append(any(clause_data))
        return all(res)

    def __str__(self):
        res = []
        for clause in self.body:
            clause_str = [f'¬x{i}' if p else f'x{i}' for p, i in clause]
            res.append('(' + ' ∨ '.join(clause_str) + ')')
        return ' ∧ '.join(res)

ksat = kSAT.generate(3, 4, 3)
print(ksat)

while True:
    cand = random.choices([True, False], k=4)
    if ksat.test(cand):
        print(cand)
        break