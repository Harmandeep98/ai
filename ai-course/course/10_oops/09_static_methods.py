class Chai_utils:

    @staticmethod
    def clean_ings(text):
        return [item.strip() for item in text.split(",")];

raw = " Water, Milk, Cardmom";

cleaned = Chai_utils.clean_ings(raw)
print(cleaned)
