# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\23")
        buf.write("~\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\6\b@\n\b")
        buf.write("\r\b\16\bA\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3")
        buf.write("\16\6\16O\n\16\r\16\16\16P\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\7\17Y\n\17\f\17\16\17\\\13\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\7\20e\n\20\f\20\16\20h\13\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\7\21r\n\21\f\21\16\21u")
        buf.write("\13\21\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\4Zf\2\25")
        buf.write("\3\3\5\2\7\2\t\4\13\5\r\6\17\7\21\b\23\t\25\n\27\13\31")
        buf.write("\f\33\r\35\16\37\17!\20#\21%\22\'\23\3\2\7\4\2CCcc\4\2")
        buf.write("DDdd\3\2\62;\5\2\13\f\17\17\"\"\4\2\f\f\17\17\2\u0080")
        buf.write("\2\3\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\3)\3")
        buf.write("\2\2\2\5.\3\2\2\2\7\60\3\2\2\2\t\62\3\2\2\2\13\65\3\2")
        buf.write("\2\2\r9\3\2\2\2\17?\3\2\2\2\21C\3\2\2\2\23E\3\2\2\2\25")
        buf.write("G\3\2\2\2\27I\3\2\2\2\31K\3\2\2\2\33N\3\2\2\2\35T\3\2")
        buf.write("\2\2\37b\3\2\2\2!m\3\2\2\2#x\3\2\2\2%z\3\2\2\2\'|\3\2")
        buf.write("\2\2)*\7o\2\2*+\7c\2\2+,\7k\2\2,-\7p\2\2-\4\3\2\2\2./")
        buf.write("\t\2\2\2/\6\3\2\2\2\60\61\t\3\2\2\61\b\3\2\2\2\62\63\5")
        buf.write("\5\3\2\63\64\5\7\4\2\64\n\3\2\2\2\65\66\7k\2\2\66\67\7")
        buf.write("p\2\2\678\7v\2\28\f\3\2\2\29:\7x\2\2:;\7q\2\2;<\7k\2\2")
        buf.write("<=\7f\2\2=\16\3\2\2\2>@\t\4\2\2?>\3\2\2\2@A\3\2\2\2A?")
        buf.write("\3\2\2\2AB\3\2\2\2B\20\3\2\2\2CD\7*\2\2D\22\3\2\2\2EF")
        buf.write("\7+\2\2F\24\3\2\2\2GH\7}\2\2H\26\3\2\2\2IJ\7\177\2\2J")
        buf.write("\30\3\2\2\2KL\7=\2\2L\32\3\2\2\2MO\t\5\2\2NM\3\2\2\2O")
        buf.write("P\3\2\2\2PN\3\2\2\2PQ\3\2\2\2QR\3\2\2\2RS\b\16\2\2S\34")
        buf.write("\3\2\2\2TU\7*\2\2UV\7,\2\2VZ\3\2\2\2WY\13\2\2\2XW\3\2")
        buf.write("\2\2Y\\\3\2\2\2Z[\3\2\2\2ZX\3\2\2\2[]\3\2\2\2\\Z\3\2\2")
        buf.write("\2]^\7,\2\2^_\7+\2\2_`\3\2\2\2`a\b\17\2\2a\36\3\2\2\2")
        buf.write("bf\7}\2\2ce\13\2\2\2dc\3\2\2\2eh\3\2\2\2fg\3\2\2\2fd\3")
        buf.write("\2\2\2gi\3\2\2\2hf\3\2\2\2ij\7\177\2\2jk\3\2\2\2kl\b\20")
        buf.write("\2\2l \3\2\2\2mn\7\61\2\2no\7\61\2\2os\3\2\2\2pr\n\6\2")
        buf.write("\2qp\3\2\2\2ru\3\2\2\2sq\3\2\2\2st\3\2\2\2tv\3\2\2\2u")
        buf.write("s\3\2\2\2vw\b\21\2\2w\"\3\2\2\2xy\13\2\2\2y$\3\2\2\2z")
        buf.write("{\13\2\2\2{&\3\2\2\2|}\13\2\2\2}(\3\2\2\2\b\2APZfs\3\b")
        buf.write("\2\2")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    AB = 2
    INTTYPE = 3
    VOIDTYPE = 4
    INTLIT = 5
    LB = 6
    RB = 7
    LP = 8
    RP = 9
    SEMI = 10
    WS = 11
    BLOCKCOM_B = 12
    BLOCKCOM_P = 13
    LINECOM = 14
    ERROR_CHAR = 15
    UNCLOSE_STRING = 16
    ILLEGAL_ESCAPE = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "AB", "INTTYPE", "VOIDTYPE", "INTLIT", "LB", "RB", "LP", "RP", 
            "SEMI", "WS", "BLOCKCOM_B", "BLOCKCOM_P", "LINECOM", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "A", "B", "AB", "INTTYPE", "VOIDTYPE", "INTLIT", 
                  "LB", "RB", "LP", "RP", "SEMI", "WS", "BLOCKCOM_B", "BLOCKCOM_P", 
                  "LINECOM", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


