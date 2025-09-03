# 🧘 Zen of Python Explorer

zen_principles = [
    ("Beautiful is better than ugly.", "Write clean, readable code. Use meaningful variable names."),
    ("Explicit is better than implicit.", "Avoid magic. Make your code's behavior clear."),
    ("Simple is better than complex.", "Favor straightforward solutions over clever hacks."),
    ("Complex is better than complicated.", "If complexity is necessary, don't make it convoluted."),
    ("Flat is better than nested.", "Avoid deep nesting. Use flat structures when possible."),
    ("Sparse is better than dense.", "Leave breathing room in your code. Don't cram logic."),
    ("Readability counts.", "Code is read more than it's written. Make it easy to follow."),
    ("Special cases aren't special enough to break the rules.", "Stick to conventions—even for edge cases."),
    ("Although practicality beats purity.", "Be pragmatic. Don't chase perfection at the cost of usability."),
    ("Errors should never pass silently.", "Handle exceptions. Don't ignore them."),
    ("Unless explicitly silenced.", "Use try/except wisely when you *do* want silence."),
    ("In the face of ambiguity, refuse the temptation to guess.", "Be precise. Don't assume."),
    ("There should be one-- and preferably only one --obvious way to do it.", "Stick to the Pythonic way."),
    ("Although that way may not be obvious at first unless you're Dutch.", "A nod to Guido van Rossum, Python’s creator."),
    ("Now is better than never.", "Don’t procrastinate. Ship it."),
    ("Although never is often better than *right* now.", "Don’t rush bad code. Think it through."),
    ("If the implementation is hard to explain, it's a bad idea.", "Clarity is a design test."),
    ("If the implementation is easy to explain, it may be a good idea.", "Good ideas are simple to communicate."),
    ("Namespaces are one honking great idea -- let's do more of those!", "Use modules and packages to organize code.")
]

# 🎓 Interactive Zen Guide
for principle, explanation in zen_principles:
    print(f"\n🧘 Principle: {principle}")
    print(f"💡 Explanation: {explanation}")
    input("Press Enter to continue...")
