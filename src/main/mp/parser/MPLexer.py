# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\30")
        buf.write("\u00a7\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\7")
        buf.write("\7L\n\7\f\7\16\7O\13\7\3\b\7\bR\n\b\f\b\16\bU\13\b\3\b")
        buf.write("\3\b\6\bY\n\b\r\b\16\bZ\3\b\7\b^\n\b\f\b\16\ba\13\b\3")
        buf.write("\b\3\b\6\be\n\b\r\b\16\bf\5\bi\n\b\3\b\3\b\5\bm\n\b\3")
        buf.write("\b\6\bp\n\b\r\b\16\bq\5\bt\n\b\3\t\6\tw\n\t\r\t\16\tx")
        buf.write("\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17")
        buf.write("\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\6\25\u0095\n\25\r\25\16\25\u0096\3\25")
        buf.write("\3\25\3\26\6\26\u009c\n\26\r\26\16\26\u009d\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\2\2\32\3\3\5\4\7\5\t\2")
        buf.write("\13\2\r\6\17\7\21\b\23\t\25\n\27\13\31\f\33\r\35\16\37")
        buf.write("\17!\20#\21%\22\'\23)\24+\25-\26/\27\61\30\3\2\6\4\2C")
        buf.write("\\c|\3\2\62;\3\2))\5\2\13\f\17\17\"\"\2\u00b2\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\3\63\3")
        buf.write("\2\2\2\5\67\3\2\2\2\7=\3\2\2\2\tD\3\2\2\2\13F\3\2\2\2")
        buf.write("\rH\3\2\2\2\17s\3\2\2\2\21v\3\2\2\2\23z\3\2\2\2\25|\3")
        buf.write("\2\2\2\27~\3\2\2\2\31\u0080\3\2\2\2\33\u0082\3\2\2\2\35")
        buf.write("\u0084\3\2\2\2\37\u0086\3\2\2\2!\u0088\3\2\2\2#\u008a")
        buf.write("\3\2\2\2%\u008c\3\2\2\2\'\u008e\3\2\2\2)\u0090\3\2\2\2")
        buf.write("+\u009b\3\2\2\2-\u00a1\3\2\2\2/\u00a3\3\2\2\2\61\u00a5")
        buf.write("\3\2\2\2\63\64\7k\2\2\64\65\7p\2\2\65\66\7v\2\2\66\4\3")
        buf.write("\2\2\2\678\7h\2\289\7n\2\29:\7q\2\2:;\7c\2\2;<\7v\2\2")
        buf.write("<\6\3\2\2\2=>\7t\2\2>?\7g\2\2?@\7v\2\2@A\7w\2\2AB\7t\2")
        buf.write("\2BC\7p\2\2C\b\3\2\2\2DE\t\2\2\2E\n\3\2\2\2FG\t\3\2\2")
        buf.write("G\f\3\2\2\2HM\5\t\5\2IL\5\t\5\2JL\5\13\6\2KI\3\2\2\2K")
        buf.write("J\3\2\2\2LO\3\2\2\2MK\3\2\2\2MN\3\2\2\2N\16\3\2\2\2OM")
        buf.write("\3\2\2\2PR\5\13\6\2QP\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3")
        buf.write("\2\2\2TV\3\2\2\2US\3\2\2\2VX\7\60\2\2WY\5\13\6\2XW\3\2")
        buf.write("\2\2YZ\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[t\3\2\2\2\\^\5\13\6")
        buf.write("\2]\\\3\2\2\2^a\3\2\2\2_]\3\2\2\2_`\3\2\2\2`h\3\2\2\2")
        buf.write("a_\3\2\2\2bd\7\60\2\2ce\5\13\6\2dc\3\2\2\2ef\3\2\2\2f")
        buf.write("d\3\2\2\2fg\3\2\2\2gi\3\2\2\2hb\3\2\2\2hi\3\2\2\2ij\3")
        buf.write("\2\2\2jl\7g\2\2km\7/\2\2lk\3\2\2\2lm\3\2\2\2mo\3\2\2\2")
        buf.write("np\5\13\6\2on\3\2\2\2pq\3\2\2\2qo\3\2\2\2qr\3\2\2\2rt")
        buf.write("\3\2\2\2sS\3\2\2\2s_\3\2\2\2t\20\3\2\2\2uw\5\13\6\2vu")
        buf.write("\3\2\2\2wx\3\2\2\2xv\3\2\2\2xy\3\2\2\2y\22\3\2\2\2z{\7")
        buf.write("*\2\2{\24\3\2\2\2|}\7+\2\2}\26\3\2\2\2~\177\7}\2\2\177")
        buf.write("\30\3\2\2\2\u0080\u0081\7\177\2\2\u0081\32\3\2\2\2\u0082")
        buf.write("\u0083\7=\2\2\u0083\34\3\2\2\2\u0084\u0085\7.\2\2\u0085")
        buf.write("\36\3\2\2\2\u0086\u0087\7?\2\2\u0087 \3\2\2\2\u0088\u0089")
        buf.write("\7-\2\2\u0089\"\3\2\2\2\u008a\u008b\7/\2\2\u008b$\3\2")
        buf.write("\2\2\u008c\u008d\7,\2\2\u008d&\3\2\2\2\u008e\u008f\7\61")
        buf.write("\2\2\u008f(\3\2\2\2\u0090\u0094\7)\2\2\u0091\u0095\n\4")
        buf.write("\2\2\u0092\u0093\7)\2\2\u0093\u0095\7)\2\2\u0094\u0091")
        buf.write("\3\2\2\2\u0094\u0092\3\2\2\2\u0095\u0096\3\2\2\2\u0096")
        buf.write("\u0094\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u0098\3\2\2\2")
        buf.write("\u0098\u0099\7)\2\2\u0099*\3\2\2\2\u009a\u009c\t\5\2\2")
        buf.write("\u009b\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009b\3")
        buf.write("\2\2\2\u009d\u009e\3\2\2\2\u009e\u009f\3\2\2\2\u009f\u00a0")
        buf.write("\b\26\2\2\u00a0,\3\2\2\2\u00a1\u00a2\13\2\2\2\u00a2.\3")
        buf.write("\2\2\2\u00a3\u00a4\13\2\2\2\u00a4\60\3\2\2\2\u00a5\u00a6")
        buf.write("\13\2\2\2\u00a6\62\3\2\2\2\21\2KMSZ_fhlqsx\u0094\u0096")
        buf.write("\u009d\3\b\2\2")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    FLOAT = 2
    RETURNS = 3
    ID = 4
    FLOATLIT = 5
    INTLIT = 6
    LP = 7
    RP = 8
    LB = 9
    RB = 10
    SM = 11
    CM = 12
    EQ = 13
    ADD = 14
    SUB = 15
    MUL = 16
    DIV = 17
    STRING = 18
    WS = 19
    ERROR_CHAR = 20
    UNCLOSE_STRING = 21
    ILLEGAL_ESCAPE = 22

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'return'", "'('", "')'", "'{'", "'}'", 
            "';'", "','", "'='", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "RETURNS", "ID", "FLOATLIT", "INTLIT", "LP", 
            "RP", "LB", "RB", "SM", "CM", "EQ", "ADD", "SUB", "MUL", "DIV", 
            "STRING", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INT", "FLOAT", "RETURNS", "LETTER", "DIGIT", "ID", "FLOATLIT", 
                  "INTLIT", "LP", "RP", "LB", "RB", "SM", "CM", "EQ", "ADD", 
                  "SUB", "MUL", "DIV", "STRING", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


