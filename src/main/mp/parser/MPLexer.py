# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25")
        buf.write("\u009b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\6")
        buf.write("\16L\n\16\r\16\16\16M\3\16\3\16\3\17\3\17\3\20\3\20\3")
        buf.write("\21\3\21\3\21\7\21Y\n\21\f\21\16\21\\\13\21\3\22\7\22")
        buf.write("_\n\22\f\22\16\22b\13\22\3\22\3\22\6\22f\n\22\r\22\16")
        buf.write("\22g\3\22\7\22k\n\22\f\22\16\22n\13\22\3\22\3\22\6\22")
        buf.write("r\n\22\r\22\16\22s\5\22v\n\22\3\22\3\22\5\22z\n\22\3\22")
        buf.write("\6\22}\n\22\r\22\16\22~\5\22\u0081\n\22\3\23\6\23\u0084")
        buf.write("\n\23\r\23\16\23\u0085\3\24\3\24\3\24\3\24\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\6\26\u0096\n\26")
        buf.write("\r\26\16\26\u0097\3\26\3\26\2\2\27\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\2\37\2")
        buf.write("!\20#\21%\22\'\23)\24+\25\3\2\6\5\2\13\f\17\17\"\"\3\2")
        buf.write("c|\3\2\62;\3\2))\2\u00a6\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\3-\3\2\2\2\5")
        buf.write("/\3\2\2\2\7\61\3\2\2\2\t\63\3\2\2\2\13\65\3\2\2\2\r\67")
        buf.write("\3\2\2\2\179\3\2\2\2\21;\3\2\2\2\23B\3\2\2\2\25D\3\2\2")
        buf.write("\2\27F\3\2\2\2\31H\3\2\2\2\33K\3\2\2\2\35Q\3\2\2\2\37")
        buf.write("S\3\2\2\2!U\3\2\2\2#\u0080\3\2\2\2%\u0083\3\2\2\2\'\u0087")
        buf.write("\3\2\2\2)\u008b\3\2\2\2+\u0091\3\2\2\2-.\7*\2\2.\4\3\2")
        buf.write("\2\2/\60\7+\2\2\60\6\3\2\2\2\61\62\7}\2\2\62\b\3\2\2\2")
        buf.write("\63\64\7\177\2\2\64\n\3\2\2\2\65\66\7=\2\2\66\f\3\2\2")
        buf.write("\2\678\7.\2\28\16\3\2\2\29:\7?\2\2:\20\3\2\2\2;<\7t\2")
        buf.write("\2<=\7g\2\2=>\7v\2\2>?\7w\2\2?@\7t\2\2@A\7p\2\2A\22\3")
        buf.write("\2\2\2BC\7-\2\2C\24\3\2\2\2DE\7/\2\2E\26\3\2\2\2FG\7,")
        buf.write("\2\2G\30\3\2\2\2HI\7\61\2\2I\32\3\2\2\2JL\t\2\2\2KJ\3")
        buf.write("\2\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2NO\3\2\2\2OP\b\16")
        buf.write("\2\2P\34\3\2\2\2QR\t\3\2\2R\36\3\2\2\2ST\t\4\2\2T \3\2")
        buf.write("\2\2UZ\5\35\17\2VY\5\35\17\2WY\5\37\20\2XV\3\2\2\2XW\3")
        buf.write("\2\2\2Y\\\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[\"\3\2\2\2\\Z\3")
        buf.write("\2\2\2]_\5\37\20\2^]\3\2\2\2_b\3\2\2\2`^\3\2\2\2`a\3\2")
        buf.write("\2\2ac\3\2\2\2b`\3\2\2\2ce\7\60\2\2df\5\37\20\2ed\3\2")
        buf.write("\2\2fg\3\2\2\2ge\3\2\2\2gh\3\2\2\2h\u0081\3\2\2\2ik\5")
        buf.write("\37\20\2ji\3\2\2\2kn\3\2\2\2lj\3\2\2\2lm\3\2\2\2mu\3\2")
        buf.write("\2\2nl\3\2\2\2oq\7\60\2\2pr\5\37\20\2qp\3\2\2\2rs\3\2")
        buf.write("\2\2sq\3\2\2\2st\3\2\2\2tv\3\2\2\2uo\3\2\2\2uv\3\2\2\2")
        buf.write("vw\3\2\2\2wy\7g\2\2xz\7/\2\2yx\3\2\2\2yz\3\2\2\2z|\3\2")
        buf.write("\2\2{}\5\37\20\2|{\3\2\2\2}~\3\2\2\2~|\3\2\2\2~\177\3")
        buf.write("\2\2\2\177\u0081\3\2\2\2\u0080`\3\2\2\2\u0080l\3\2\2\2")
        buf.write("\u0081$\3\2\2\2\u0082\u0084\t\4\2\2\u0083\u0082\3\2\2")
        buf.write("\2\u0084\u0085\3\2\2\2\u0085\u0083\3\2\2\2\u0085\u0086")
        buf.write("\3\2\2\2\u0086&\3\2\2\2\u0087\u0088\7k\2\2\u0088\u0089")
        buf.write("\7p\2\2\u0089\u008a\7v\2\2\u008a(\3\2\2\2\u008b\u008c")
        buf.write("\7h\2\2\u008c\u008d\7n\2\2\u008d\u008e\7q\2\2\u008e\u008f")
        buf.write("\7c\2\2\u008f\u0090\7v\2\2\u0090*\3\2\2\2\u0091\u0095")
        buf.write("\7)\2\2\u0092\u0096\n\5\2\2\u0093\u0094\7)\2\2\u0094\u0096")
        buf.write("\7)\2\2\u0095\u0092\3\2\2\2\u0095\u0093\3\2\2\2\u0096")
        buf.write("\u0097\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098\3\2\2\2")
        buf.write("\u0098\u0099\3\2\2\2\u0099\u009a\7)\2\2\u009a,\3\2\2\2")
        buf.write("\21\2MXZ`glsuy~\u0080\u0085\u0095\u0097\3\b\2\2")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    LP = 1
    RP = 2
    LB = 3
    RB = 4
    SM = 5
    CM = 6
    EQ = 7
    RETURN = 8
    ADD = 9
    SUB = 10
    MUL = 11
    DIV = 12
    WS = 13
    ID = 14
    FLOATLIT = 15
    INTLIT = 16
    INT = 17
    FLOAT = 18
    STRING = 19

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "';'", "','", "'='", "'return'", 
            "'+'", "'-'", "'*'", "'/'", "'int'", "'float'" ]

    symbolicNames = [ "<INVALID>",
            "LP", "RP", "LB", "RB", "SM", "CM", "EQ", "RETURN", "ADD", "SUB", 
            "MUL", "DIV", "WS", "ID", "FLOATLIT", "INTLIT", "INT", "FLOAT", 
            "STRING" ]

    ruleNames = [ "LP", "RP", "LB", "RB", "SM", "CM", "EQ", "RETURN", "ADD", 
                  "SUB", "MUL", "DIV", "WS", "LETTER", "DIGIT", "ID", "FLOATLIT", 
                  "INTLIT", "INT", "FLOAT", "STRING" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


