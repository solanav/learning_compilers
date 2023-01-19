from typing import List, Tuple

Grammar = List[Tuple[str, str]]

NONTERMINAL = ["S", "F"]
TERMINAL = ["(", ")", "a", "+", "$"]

PARSE_TABLE = [
    [2, None, 1, None, None],
    [None, None, 3, None, None],
]

def index_parse_table(c1: str, c2: str):
    print(f"INDEXES: {c1}, {c2}")
    
    if c1 in TERMINAL:
        terminal = TERMINAL.index(c1)
        nonterminal = NONTERMINAL.index(c2)
    else:
        terminal = TERMINAL.index(c2)
        nonterminal = NONTERMINAL.index(c1)
    
    return PARSE_TABLE[nonterminal][terminal]

def parse(grammar: Grammar, instream: str):
    stack = ["S", "$"]
    
    while len(instream) > 0:
        print(f"INPUT:   {instream}")

        c = instream[0]
        head = stack[0]
        
        # If head and input are the same, discard them
        if c == head:
            instream = instream[1:]
            stack.pop(0)
            continue
        
        # Get the rule to apply
        rule_index = index_parse_table(c, head)
        rule = grammar[rule_index - 1]
        print(f"RULE:    {rule_index} || {rule}")
        
        # Update the stack with the rule
        stack.pop(0)
        for rc in reversed(rule[1]):
            if rc != " ":
                stack.insert(0, rc)
            
        print(f"STACK:   {stack}\n")
    
    # Return true if only $ is left in the stack
    return stack == ["$"]


def parse_grammar(grammar: str) -> Grammar:
    return [tuple(l.split(" -> ")) for l in grammar.splitlines(False)]

if __name__ == "__main__":
    with open("data/grammar.txt") as f:
        grammar = parse_grammar(f.read())
        print(f"GRAMMAR: {grammar}")

    with open("data/input.txt") as f:
        instream = f.read().replace(" ", "")
        print(f"INPUT:   {instream}")
        
    print()
    parsable = parse(grammar, instream)
    print(f"\nPARSABLE? {parsable}")