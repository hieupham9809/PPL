# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\67")
        buf.write("\u01f3\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\3\2\3\2\3\3\3\3\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3")
        buf.write("\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26")
        buf.write("\3\26\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3")
        buf.write("&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3")
        buf.write("+\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3")
        buf.write("/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67")
        buf.write("\3\67\38\38\38\38\39\39\39\39\39\39\39\39\39\39\39\39")
        buf.write("\39\39\39\39\39\39\39\39\39\39\39\39\39\39\59\u0190\n")
        buf.write("9\3:\3:\5:\u0194\n:\3:\3:\7:\u0198\n:\f:\16:\u019b\13")
        buf.write(":\3;\3;\3<\3<\3=\3=\3=\3>\3>\3?\3?\3?\3@\3@\3A\3A\3B\3")
        buf.write("B\3C\3C\3D\3D\3D\3E\6E\u01b5\nE\rE\16E\u01b6\3F\3F\3G")
        buf.write("\3G\3H\3H\3I\3I\3J\3J\3K\6K\u01c4\nK\rK\16K\u01c5\3K\3")
        buf.write("K\3L\3L\3L\3L\7L\u01ce\nL\fL\16L\u01d1\13L\3L\3L\3L\3")
        buf.write("L\3L\3M\3M\7M\u01da\nM\fM\16M\u01dd\13M\3M\3M\3M\3M\3")
        buf.write("N\3N\3N\3N\7N\u01e7\nN\fN\16N\u01ea\13N\3N\3N\3O\3O\3")
        buf.write("P\3P\3Q\3Q\4\u01cf\u01db\2R\3\2\5\2\7\2\t\2\13\2\r\2\17")
        buf.write("\2\21\2\23\2\25\2\27\2\31\2\33\2\35\2\37\2!\2#\2%\2\'")
        buf.write("\2)\2+\2-\2/\2\61\2\63\2\65\2\67\39\4;\5=\6?\7A\bC\tE")
        buf.write("\nG\13I\fK\rM\16O\17Q\20S\21U\22W\23Y\24[\25]\26_\27a")
        buf.write("\30c\31e\32g\33i\34k\35m\36o\37q\2s u!w\"y#{$}%\177&\u0081")
        buf.write("\'\u0083(\u0085)\u0087*\u0089+\u008b,\u008d-\u008f.\u0091")
        buf.write("/\u0093\60\u0095\61\u0097\62\u0099\63\u009b\64\u009d\65")
        buf.write("\u009f\66\u00a1\67\3\2 \4\2CCcc\4\2DDdd\4\2EEee\4\2FF")
        buf.write("ff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2")
        buf.write("MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4")
        buf.write("\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZz")
        buf.write("z\4\2[[{{\4\2\\\\||\4\2\62;aa\3\2\62;\5\2\13\f\17\17\"")
        buf.write("\"\4\2\f\f\17\17\2\u01f8\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3")
        buf.write("\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2")
        buf.write("\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2")
        buf.write("\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\3\u00a3")
        buf.write("\3\2\2\2\5\u00a5\3\2\2\2\7\u00a7\3\2\2\2\t\u00a9\3\2\2")
        buf.write("\2\13\u00ab\3\2\2\2\r\u00ad\3\2\2\2\17\u00af\3\2\2\2\21")
        buf.write("\u00b1\3\2\2\2\23\u00b3\3\2\2\2\25\u00b5\3\2\2\2\27\u00b7")
        buf.write("\3\2\2\2\31\u00b9\3\2\2\2\33\u00bb\3\2\2\2\35\u00bd\3")
        buf.write("\2\2\2\37\u00bf\3\2\2\2!\u00c1\3\2\2\2#\u00c3\3\2\2\2")
        buf.write("%\u00c5\3\2\2\2\'\u00c7\3\2\2\2)\u00c9\3\2\2\2+\u00cb")
        buf.write("\3\2\2\2-\u00cd\3\2\2\2/\u00cf\3\2\2\2\61\u00d1\3\2\2")
        buf.write("\2\63\u00d3\3\2\2\2\65\u00d5\3\2\2\2\67\u00d7\3\2\2\2")
        buf.write("9\u00dd\3\2\2\2;\u00e6\3\2\2\2=\u00ea\3\2\2\2?\u00ed\3")
        buf.write("\2\2\2A\u00f4\3\2\2\2C\u00f7\3\2\2\2E\u00fa\3\2\2\2G\u00ff")
        buf.write("\3\2\2\2I\u0104\3\2\2\2K\u010b\3\2\2\2M\u0111\3\2\2\2")
        buf.write("O\u0117\3\2\2\2Q\u011b\3\2\2\2S\u0124\3\2\2\2U\u012e\3")
        buf.write("\2\2\2W\u0132\3\2\2\2Y\u0137\3\2\2\2[\u013d\3\2\2\2]\u0143")
        buf.write("\3\2\2\2_\u0146\3\2\2\2a\u014b\3\2\2\2c\u0153\3\2\2\2")
        buf.write("e\u015b\3\2\2\2g\u0162\3\2\2\2i\u0166\3\2\2\2k\u016a\3")
        buf.write("\2\2\2m\u016d\3\2\2\2o\u0171\3\2\2\2q\u018f\3\2\2\2s\u0193")
        buf.write("\3\2\2\2u\u019c\3\2\2\2w\u019e\3\2\2\2y\u01a0\3\2\2\2")
        buf.write("{\u01a3\3\2\2\2}\u01a5\3\2\2\2\177\u01a8\3\2\2\2\u0081")
        buf.write("\u01aa\3\2\2\2\u0083\u01ac\3\2\2\2\u0085\u01ae\3\2\2\2")
        buf.write("\u0087\u01b0\3\2\2\2\u0089\u01b4\3\2\2\2\u008b\u01b8\3")
        buf.write("\2\2\2\u008d\u01ba\3\2\2\2\u008f\u01bc\3\2\2\2\u0091\u01be")
        buf.write("\3\2\2\2\u0093\u01c0\3\2\2\2\u0095\u01c3\3\2\2\2\u0097")
        buf.write("\u01c9\3\2\2\2\u0099\u01d7\3\2\2\2\u009b\u01e2\3\2\2\2")
        buf.write("\u009d\u01ed\3\2\2\2\u009f\u01ef\3\2\2\2\u00a1\u01f1\3")
        buf.write("\2\2\2\u00a3\u00a4\t\2\2\2\u00a4\4\3\2\2\2\u00a5\u00a6")
        buf.write("\t\3\2\2\u00a6\6\3\2\2\2\u00a7\u00a8\t\4\2\2\u00a8\b\3")
        buf.write("\2\2\2\u00a9\u00aa\t\5\2\2\u00aa\n\3\2\2\2\u00ab\u00ac")
        buf.write("\t\6\2\2\u00ac\f\3\2\2\2\u00ad\u00ae\t\7\2\2\u00ae\16")
        buf.write("\3\2\2\2\u00af\u00b0\t\b\2\2\u00b0\20\3\2\2\2\u00b1\u00b2")
        buf.write("\t\t\2\2\u00b2\22\3\2\2\2\u00b3\u00b4\t\n\2\2\u00b4\24")
        buf.write("\3\2\2\2\u00b5\u00b6\t\13\2\2\u00b6\26\3\2\2\2\u00b7\u00b8")
        buf.write("\t\f\2\2\u00b8\30\3\2\2\2\u00b9\u00ba\t\r\2\2\u00ba\32")
        buf.write("\3\2\2\2\u00bb\u00bc\t\16\2\2\u00bc\34\3\2\2\2\u00bd\u00be")
        buf.write("\t\17\2\2\u00be\36\3\2\2\2\u00bf\u00c0\t\20\2\2\u00c0")
        buf.write(" \3\2\2\2\u00c1\u00c2\t\21\2\2\u00c2\"\3\2\2\2\u00c3\u00c4")
        buf.write("\t\22\2\2\u00c4$\3\2\2\2\u00c5\u00c6\t\23\2\2\u00c6&\3")
        buf.write("\2\2\2\u00c7\u00c8\t\24\2\2\u00c8(\3\2\2\2\u00c9\u00ca")
        buf.write("\t\25\2\2\u00ca*\3\2\2\2\u00cb\u00cc\t\26\2\2\u00cc,\3")
        buf.write("\2\2\2\u00cd\u00ce\t\27\2\2\u00ce.\3\2\2\2\u00cf\u00d0")
        buf.write("\t\30\2\2\u00d0\60\3\2\2\2\u00d1\u00d2\t\31\2\2\u00d2")
        buf.write("\62\3\2\2\2\u00d3\u00d4\t\32\2\2\u00d4\64\3\2\2\2\u00d5")
        buf.write("\u00d6\t\33\2\2\u00d6\66\3\2\2\2\u00d7\u00d8\5\5\3\2\u00d8")
        buf.write("\u00d9\5%\23\2\u00d9\u00da\5\13\6\2\u00da\u00db\5\3\2")
        buf.write("\2\u00db\u00dc\5\27\f\2\u00dc8\3\2\2\2\u00dd\u00de\5\7")
        buf.write("\4\2\u00de\u00df\5\37\20\2\u00df\u00e0\5\35\17\2\u00e0")
        buf.write("\u00e1\5)\25\2\u00e1\u00e2\5\23\n\2\u00e2\u00e3\5\35\17")
        buf.write("\2\u00e3\u00e4\5+\26\2\u00e4\u00e5\5\13\6\2\u00e5:\3\2")
        buf.write("\2\2\u00e6\u00e7\5\r\7\2\u00e7\u00e8\5\37\20\2\u00e8\u00e9")
        buf.write("\5%\23\2\u00e9<\3\2\2\2\u00ea\u00eb\5)\25\2\u00eb\u00ec")
        buf.write("\5\37\20\2\u00ec>\3\2\2\2\u00ed\u00ee\5\t\5\2\u00ee\u00ef")
        buf.write("\5\37\20\2\u00ef\u00f0\5/\30\2\u00f0\u00f1\5\35\17\2\u00f1")
        buf.write("\u00f2\5)\25\2\u00f2\u00f3\5\37\20\2\u00f3@\3\2\2\2\u00f4")
        buf.write("\u00f5\5\t\5\2\u00f5\u00f6\5\37\20\2\u00f6B\3\2\2\2\u00f7")
        buf.write("\u00f8\5\23\n\2\u00f8\u00f9\5\r\7\2\u00f9D\3\2\2\2\u00fa")
        buf.write("\u00fb\5)\25\2\u00fb\u00fc\5\21\t\2\u00fc\u00fd\5\13\6")
        buf.write("\2\u00fd\u00fe\5\35\17\2\u00feF\3\2\2\2\u00ff\u0100\5")
        buf.write("\13\6\2\u0100\u0101\5\31\r\2\u0101\u0102\5\'\24\2\u0102")
        buf.write("\u0103\5\13\6\2\u0103H\3\2\2\2\u0104\u0105\5%\23\2\u0105")
        buf.write("\u0106\5\13\6\2\u0106\u0107\5)\25\2\u0107\u0108\5+\26")
        buf.write("\2\u0108\u0109\5%\23\2\u0109\u010a\5\35\17\2\u010aJ\3")
        buf.write("\2\2\2\u010b\u010c\5/\30\2\u010c\u010d\5\21\t\2\u010d")
        buf.write("\u010e\5\23\n\2\u010e\u010f\5\31\r\2\u010f\u0110\5\13")
        buf.write("\6\2\u0110L\3\2\2\2\u0111\u0112\5\5\3\2\u0112\u0113\5")
        buf.write("\13\6\2\u0113\u0114\5\17\b\2\u0114\u0115\5\23\n\2\u0115")
        buf.write("\u0116\5\35\17\2\u0116N\3\2\2\2\u0117\u0118\5\13\6\2\u0118")
        buf.write("\u0119\5\35\17\2\u0119\u011a\5\t\5\2\u011aP\3\2\2\2\u011b")
        buf.write("\u011c\5\r\7\2\u011c\u011d\5+\26\2\u011d\u011e\5\35\17")
        buf.write("\2\u011e\u011f\5\7\4\2\u011f\u0120\5)\25\2\u0120\u0121")
        buf.write("\5\23\n\2\u0121\u0122\5\37\20\2\u0122\u0123\5\35\17\2")
        buf.write("\u0123R\3\2\2\2\u0124\u0125\5!\21\2\u0125\u0126\5%\23")
        buf.write("\2\u0126\u0127\5\37\20\2\u0127\u0128\5\7\4\2\u0128\u0129")
        buf.write("\5\13\6\2\u0129\u012a\5\t\5\2\u012a\u012b\5+\26\2\u012b")
        buf.write("\u012c\5%\23\2\u012c\u012d\5\13\6\2\u012dT\3\2\2\2\u012e")
        buf.write("\u012f\5-\27\2\u012f\u0130\5\3\2\2\u0130\u0131\5%\23\2")
        buf.write("\u0131V\3\2\2\2\u0132\u0133\5)\25\2\u0133\u0134\5%\23")
        buf.write("\2\u0134\u0135\5+\26\2\u0135\u0136\5\13\6\2\u0136X\3\2")
        buf.write("\2\2\u0137\u0138\5\r\7\2\u0138\u0139\5\3\2\2\u0139\u013a")
        buf.write("\5\31\r\2\u013a\u013b\5\'\24\2\u013b\u013c\5\13\6\2\u013c")
        buf.write("Z\3\2\2\2\u013d\u013e\5\3\2\2\u013e\u013f\5%\23\2\u013f")
        buf.write("\u0140\5%\23\2\u0140\u0141\5\3\2\2\u0141\u0142\5\63\32")
        buf.write("\2\u0142\\\3\2\2\2\u0143\u0144\5\37\20\2\u0144\u0145\5")
        buf.write("\r\7\2\u0145^\3\2\2\2\u0146\u0147\5%\23\2\u0147\u0148")
        buf.write("\5\13\6\2\u0148\u0149\5\3\2\2\u0149\u014a\5\31\r\2\u014a")
        buf.write("`\3\2\2\2\u014b\u014c\5\5\3\2\u014c\u014d\5\37\20\2\u014d")
        buf.write("\u014e\5\37\20\2\u014e\u014f\5\31\r\2\u014f\u0150\5\13")
        buf.write("\6\2\u0150\u0151\5\3\2\2\u0151\u0152\5\35\17\2\u0152b")
        buf.write("\3\2\2\2\u0153\u0154\5\23\n\2\u0154\u0155\5\35\17\2\u0155")
        buf.write("\u0156\5)\25\2\u0156\u0157\5\13\6\2\u0157\u0158\5\17\b")
        buf.write("\2\u0158\u0159\5\13\6\2\u0159\u015a\5%\23\2\u015ad\3\2")
        buf.write("\2\2\u015b\u015c\5\'\24\2\u015c\u015d\5)\25\2\u015d\u015e")
        buf.write("\5%\23\2\u015e\u015f\5\23\n\2\u015f\u0160\5\35\17\2\u0160")
        buf.write("\u0161\5\17\b\2\u0161f\3\2\2\2\u0162\u0163\5\35\17\2\u0163")
        buf.write("\u0164\5\37\20\2\u0164\u0165\5)\25\2\u0165h\3\2\2\2\u0166")
        buf.write("\u0167\5\3\2\2\u0167\u0168\5\35\17\2\u0168\u0169\5\t\5")
        buf.write("\2\u0169j\3\2\2\2\u016a\u016b\5\37\20\2\u016b\u016c\5")
        buf.write("%\23\2\u016cl\3\2\2\2\u016d\u016e\5\t\5\2\u016e\u016f")
        buf.write("\5\23\n\2\u016f\u0170\5-\27\2\u0170n\3\2\2\2\u0171\u0172")
        buf.write("\5\33\16\2\u0172\u0173\5\37\20\2\u0173\u0174\5\t\5\2\u0174")
        buf.write("p\3\2\2\2\u0175\u0190\5\3\2\2\u0176\u0190\5\5\3\2\u0177")
        buf.write("\u0190\5\7\4\2\u0178\u0190\5\t\5\2\u0179\u0190\5\13\6")
        buf.write("\2\u017a\u0190\5\r\7\2\u017b\u0190\5\17\b\2\u017c\u0190")
        buf.write("\5\21\t\2\u017d\u0190\5\23\n\2\u017e\u0190\5\25\13\2\u017f")
        buf.write("\u0190\5\27\f\2\u0180\u0190\5\31\r\2\u0181\u0190\5\33")
        buf.write("\16\2\u0182\u0190\5\35\17\2\u0183\u0190\5\37\20\2\u0184")
        buf.write("\u0190\5!\21\2\u0185\u0190\5#\22\2\u0186\u0190\5%\23\2")
        buf.write("\u0187\u0190\5\'\24\2\u0188\u0190\5)\25\2\u0189\u0190")
        buf.write("\5+\26\2\u018a\u0190\5-\27\2\u018b\u0190\5/\30\2\u018c")
        buf.write("\u0190\5\61\31\2\u018d\u0190\5\63\32\2\u018e\u0190\5\65")
        buf.write("\33\2\u018f\u0175\3\2\2\2\u018f\u0176\3\2\2\2\u018f\u0177")
        buf.write("\3\2\2\2\u018f\u0178\3\2\2\2\u018f\u0179\3\2\2\2\u018f")
        buf.write("\u017a\3\2\2\2\u018f\u017b\3\2\2\2\u018f\u017c\3\2\2\2")
        buf.write("\u018f\u017d\3\2\2\2\u018f\u017e\3\2\2\2\u018f\u017f\3")
        buf.write("\2\2\2\u018f\u0180\3\2\2\2\u018f\u0181\3\2\2\2\u018f\u0182")
        buf.write("\3\2\2\2\u018f\u0183\3\2\2\2\u018f\u0184\3\2\2\2\u018f")
        buf.write("\u0185\3\2\2\2\u018f\u0186\3\2\2\2\u018f\u0187\3\2\2\2")
        buf.write("\u018f\u0188\3\2\2\2\u018f\u0189\3\2\2\2\u018f\u018a\3")
        buf.write("\2\2\2\u018f\u018b\3\2\2\2\u018f\u018c\3\2\2\2\u018f\u018d")
        buf.write("\3\2\2\2\u018f\u018e\3\2\2\2\u0190r\3\2\2\2\u0191\u0194")
        buf.write("\5q9\2\u0192\u0194\7a\2\2\u0193\u0191\3\2\2\2\u0193\u0192")
        buf.write("\3\2\2\2\u0194\u0199\3\2\2\2\u0195\u0198\5q9\2\u0196\u0198")
        buf.write("\t\34\2\2\u0197\u0195\3\2\2\2\u0197\u0196\3\2\2\2\u0198")
        buf.write("\u019b\3\2\2\2\u0199\u0197\3\2\2\2\u0199\u019a\3\2\2\2")
        buf.write("\u019at\3\2\2\2\u019b\u0199\3\2\2\2\u019c\u019d\7-\2\2")
        buf.write("\u019dv\3\2\2\2\u019e\u019f\7,\2\2\u019fx\3\2\2\2\u01a0")
        buf.write("\u01a1\7>\2\2\u01a1\u01a2\7@\2\2\u01a2z\3\2\2\2\u01a3")
        buf.write("\u01a4\7>\2\2\u01a4|\3\2\2\2\u01a5\u01a6\7>\2\2\u01a6")
        buf.write("\u01a7\7?\2\2\u01a7~\3\2\2\2\u01a8\u01a9\7/\2\2\u01a9")
        buf.write("\u0080\3\2\2\2\u01aa\u01ab\7\61\2\2\u01ab\u0082\3\2\2")
        buf.write("\2\u01ac\u01ad\7?\2\2\u01ad\u0084\3\2\2\2\u01ae\u01af")
        buf.write("\7@\2\2\u01af\u0086\3\2\2\2\u01b0\u01b1\7@\2\2\u01b1\u01b2")
        buf.write("\7?\2\2\u01b2\u0088\3\2\2\2\u01b3\u01b5\t\35\2\2\u01b4")
        buf.write("\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b4\3\2\2\2")
        buf.write("\u01b6\u01b7\3\2\2\2\u01b7\u008a\3\2\2\2\u01b8\u01b9\7")
        buf.write("*\2\2\u01b9\u008c\3\2\2\2\u01ba\u01bb\7+\2\2\u01bb\u008e")
        buf.write("\3\2\2\2\u01bc\u01bd\7}\2\2\u01bd\u0090\3\2\2\2\u01be")
        buf.write("\u01bf\7\177\2\2\u01bf\u0092\3\2\2\2\u01c0\u01c1\7=\2")
        buf.write("\2\u01c1\u0094\3\2\2\2\u01c2\u01c4\t\36\2\2\u01c3\u01c2")
        buf.write("\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5")
        buf.write("\u01c6\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c8\bK\2\2")
        buf.write("\u01c8\u0096\3\2\2\2\u01c9\u01ca\7*\2\2\u01ca\u01cb\7")
        buf.write(",\2\2\u01cb\u01cf\3\2\2\2\u01cc\u01ce\13\2\2\2\u01cd\u01cc")
        buf.write("\3\2\2\2\u01ce\u01d1\3\2\2\2\u01cf\u01d0\3\2\2\2\u01cf")
        buf.write("\u01cd\3\2\2\2\u01d0\u01d2\3\2\2\2\u01d1\u01cf\3\2\2\2")
        buf.write("\u01d2\u01d3\7,\2\2\u01d3\u01d4\7+\2\2\u01d4\u01d5\3\2")
        buf.write("\2\2\u01d5\u01d6\bL\2\2\u01d6\u0098\3\2\2\2\u01d7\u01db")
        buf.write("\7}\2\2\u01d8\u01da\13\2\2\2\u01d9\u01d8\3\2\2\2\u01da")
        buf.write("\u01dd\3\2\2\2\u01db\u01dc\3\2\2\2\u01db\u01d9\3\2\2\2")
        buf.write("\u01dc\u01de\3\2\2\2\u01dd\u01db\3\2\2\2\u01de\u01df\7")
        buf.write("\177\2\2\u01df\u01e0\3\2\2\2\u01e0\u01e1\bM\2\2\u01e1")
        buf.write("\u009a\3\2\2\2\u01e2\u01e3\7\61\2\2\u01e3\u01e4\7\61\2")
        buf.write("\2\u01e4\u01e8\3\2\2\2\u01e5\u01e7\n\37\2\2\u01e6\u01e5")
        buf.write("\3\2\2\2\u01e7\u01ea\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8")
        buf.write("\u01e9\3\2\2\2\u01e9\u01eb\3\2\2\2\u01ea\u01e8\3\2\2\2")
        buf.write("\u01eb\u01ec\bN\2\2\u01ec\u009c\3\2\2\2\u01ed\u01ee\13")
        buf.write("\2\2\2\u01ee\u009e\3\2\2\2\u01ef\u01f0\13\2\2\2\u01f0")
        buf.write("\u00a0\3\2\2\2\u01f1\u01f2\13\2\2\2\u01f2\u00a2\3\2\2")
        buf.write("\2\f\2\u018f\u0193\u0197\u0199\u01b6\u01c5\u01cf\u01db")
        buf.write("\u01e8\3\b\2\2")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BREAK = 1
    CONTINUE = 2
    FOR = 3
    TO = 4
    DOWNTO = 5
    DO = 6
    IF = 7
    THEN = 8
    ELSE = 9
    RETURNS = 10
    WHILE = 11
    BEGIN = 12
    END = 13
    FUNCTION = 14
    PROCEDURE = 15
    VAR = 16
    TRUE = 17
    FALSE = 18
    ARRAY = 19
    OF = 20
    REAL = 21
    BOOLEAN = 22
    INTEGER = 23
    STRING = 24
    NOT = 25
    AND = 26
    OR = 27
    DIV = 28
    MOD = 29
    ID = 30
    ADDOP = 31
    MULOP = 32
    NEQOP = 33
    LTOP = 34
    LTEOP = 35
    SUBOP = 36
    DIVOP = 37
    EQOP = 38
    GTOP = 39
    GTEOP = 40
    INTLIT = 41
    LB = 42
    RB = 43
    LP = 44
    RP = 45
    SEMI = 46
    WS = 47
    BLOCKCOM_B = 48
    BLOCKCOM_P = 49
    LINECOM = 50
    ERROR_CHAR = 51
    UNCLOSE_STRING = 52
    ILLEGAL_ESCAPE = 53

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'*'", "'<>'", "'<'", "'<='", "'-'", "'/'", "'='", "'>'", 
            "'>='", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", 
            "ELSE", "RETURNS", "WHILE", "BEGIN", "END", "FUNCTION", "PROCEDURE", 
            "VAR", "TRUE", "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", 
            "STRING", "NOT", "AND", "OR", "DIV", "MOD", "ID", "ADDOP", "MULOP", 
            "NEQOP", "LTOP", "LTEOP", "SUBOP", "DIVOP", "EQOP", "GTOP", 
            "GTEOP", "INTLIT", "LB", "RB", "LP", "RP", "SEMI", "WS", "BLOCKCOM_B", 
            "BLOCKCOM_P", "LINECOM", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                  "W", "X", "Y", "Z", "BREAK", "CONTINUE", "FOR", "TO", 
                  "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURNS", "WHILE", 
                  "BEGIN", "END", "FUNCTION", "PROCEDURE", "VAR", "TRUE", 
                  "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", 
                  "STRING", "NOT", "AND", "OR", "DIV", "MOD", "IDCHAR", 
                  "ID", "ADDOP", "MULOP", "NEQOP", "LTOP", "LTEOP", "SUBOP", 
                  "DIVOP", "EQOP", "GTOP", "GTEOP", "INTLIT", "LB", "RB", 
                  "LP", "RP", "SEMI", "WS", "BLOCKCOM_B", "BLOCKCOM_P", 
                  "LINECOM", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


