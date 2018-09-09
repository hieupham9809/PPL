# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u0249\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3")
        buf.write("\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22")
        buf.write("\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27")
        buf.write("\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3")
        buf.write("$\3$\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)")
        buf.write("\3*\3*\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3")
        buf.write(",\3,\3-\3-\3-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3/\3/\3/\3\60")
        buf.write("\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\67\3\67\3\67\3\67\38\38\3")
        buf.write("8\38\39\39\39\39\39\39\39\39\39\39\39\39\39\39\39\39\3")
        buf.write("9\39\39\39\39\39\39\39\39\39\59\u019e\n9\3:\3:\5:\u01a2")
        buf.write("\n:\3:\3:\7:\u01a6\n:\f:\16:\u01a9\13:\3;\3;\3<\3<\3=")
        buf.write("\3=\3=\3>\3>\3?\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3")
        buf.write("D\3E\3E\3F\6F\u01c5\nF\rF\16F\u01c6\3G\3G\6G\u01cb\nG")
        buf.write("\rG\16G\u01cc\5G\u01cf\nG\3G\3G\3G\5G\u01d4\nG\3H\3H\7")
        buf.write("H\u01d8\nH\fH\16H\u01db\13H\3H\3H\3H\3I\7I\u01e1\nI\f")
        buf.write("I\16I\u01e4\13I\3I\3I\6I\u01e8\nI\rI\16I\u01e9\3I\6I\u01ed")
        buf.write("\nI\rI\16I\u01ee\3I\3I\7I\u01f3\nI\fI\16I\u01f6\13I\5")
        buf.write("I\u01f8\nI\3J\3J\5J\u01fc\nJ\3J\6J\u01ff\nJ\rJ\16J\u0200")
        buf.write("\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3P\3P\3Q\3Q\3R\3R\3R\3")
        buf.write("S\6S\u0215\nS\rS\16S\u0216\3S\3S\3T\3T\3T\3T\7T\u021f")
        buf.write("\nT\fT\16T\u0222\13T\3T\3T\3T\3T\3T\3U\3U\7U\u022b\nU")
        buf.write("\fU\16U\u022e\13U\3U\3U\3U\3U\3V\3V\3V\3V\7V\u0238\nV")
        buf.write("\fV\16V\u023b\13V\3V\3V\3W\3W\3X\3X\7X\u0243\nX\fX\16")
        buf.write("X\u0246\13X\3X\3X\4\u0220\u022c\2Y\3\2\5\2\7\2\t\2\13")
        buf.write("\2\r\2\17\2\21\2\23\2\25\2\27\2\31\2\33\2\35\2\37\2!\2")
        buf.write("#\2%\2\'\2)\2+\2-\2/\2\61\2\63\2\65\2\67\39\4;\5=\6?\7")
        buf.write("A\bC\tE\nG\13I\fK\rM\16O\17Q\20S\21U\22W\23Y\24[\25]\26")
        buf.write("_\27a\30c\31e\32g\33i\34k\35m\36o\37q\2s u!w\"y#{$}%\177")
        buf.write("&\u0081\'\u0083(\u0085)\u0087*\u0089\2\u008b+\u008d,\u008f")
        buf.write("-\u0091\2\u0093\2\u0095.\u0097/\u0099\60\u009b\61\u009d")
        buf.write("\62\u009f\63\u00a1\64\u00a3\65\u00a5\66\u00a7\67\u00a9")
        buf.write("8\u00ab9\u00ad:\u00af;\3\2\"\4\2CCcc\4\2DDdd\4\2EEee\4")
        buf.write("\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLl")
        buf.write("l\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2")
        buf.write("SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4")
        buf.write("\2ZZzz\4\2[[{{\4\2\\\\||\4\2\62;aa\3\2\62;\4\2\n\f\16")
        buf.write("\17\5\2\13\f\17\17\"\"\4\2\f\f\17\17\3\2$$\2\u0257\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2s")
        buf.write("\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2")
        buf.write("}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2")
        buf.write("\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2")
        buf.write("\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad")
        buf.write("\3\2\2\2\2\u00af\3\2\2\2\3\u00b1\3\2\2\2\5\u00b3\3\2\2")
        buf.write("\2\7\u00b5\3\2\2\2\t\u00b7\3\2\2\2\13\u00b9\3\2\2\2\r")
        buf.write("\u00bb\3\2\2\2\17\u00bd\3\2\2\2\21\u00bf\3\2\2\2\23\u00c1")
        buf.write("\3\2\2\2\25\u00c3\3\2\2\2\27\u00c5\3\2\2\2\31\u00c7\3")
        buf.write("\2\2\2\33\u00c9\3\2\2\2\35\u00cb\3\2\2\2\37\u00cd\3\2")
        buf.write("\2\2!\u00cf\3\2\2\2#\u00d1\3\2\2\2%\u00d3\3\2\2\2\'\u00d5")
        buf.write("\3\2\2\2)\u00d7\3\2\2\2+\u00d9\3\2\2\2-\u00db\3\2\2\2")
        buf.write("/\u00dd\3\2\2\2\61\u00df\3\2\2\2\63\u00e1\3\2\2\2\65\u00e3")
        buf.write("\3\2\2\2\67\u00e5\3\2\2\29\u00eb\3\2\2\2;\u00f4\3\2\2")
        buf.write("\2=\u00f8\3\2\2\2?\u00fb\3\2\2\2A\u0102\3\2\2\2C\u0105")
        buf.write("\3\2\2\2E\u0108\3\2\2\2G\u010d\3\2\2\2I\u0112\3\2\2\2")
        buf.write("K\u0119\3\2\2\2M\u011f\3\2\2\2O\u0125\3\2\2\2Q\u0129\3")
        buf.write("\2\2\2S\u0132\3\2\2\2U\u013c\3\2\2\2W\u0140\3\2\2\2Y\u0145")
        buf.write("\3\2\2\2[\u014b\3\2\2\2]\u0151\3\2\2\2_\u0154\3\2\2\2")
        buf.write("a\u0159\3\2\2\2c\u0161\3\2\2\2e\u0169\3\2\2\2g\u0170\3")
        buf.write("\2\2\2i\u0174\3\2\2\2k\u0178\3\2\2\2m\u017b\3\2\2\2o\u017f")
        buf.write("\3\2\2\2q\u019d\3\2\2\2s\u01a1\3\2\2\2u\u01aa\3\2\2\2")
        buf.write("w\u01ac\3\2\2\2y\u01ae\3\2\2\2{\u01b1\3\2\2\2}\u01b3\3")
        buf.write("\2\2\2\177\u01b6\3\2\2\2\u0081\u01b8\3\2\2\2\u0083\u01ba")
        buf.write("\3\2\2\2\u0085\u01bc\3\2\2\2\u0087\u01be\3\2\2\2\u0089")
        buf.write("\u01c1\3\2\2\2\u008b\u01c4\3\2\2\2\u008d\u01d3\3\2\2\2")
        buf.write("\u008f\u01d5\3\2\2\2\u0091\u01f7\3\2\2\2\u0093\u01f9\3")
        buf.write("\2\2\2\u0095\u0202\3\2\2\2\u0097\u0204\3\2\2\2\u0099\u0206")
        buf.write("\3\2\2\2\u009b\u0208\3\2\2\2\u009d\u020a\3\2\2\2\u009f")
        buf.write("\u020c\3\2\2\2\u00a1\u020e\3\2\2\2\u00a3\u0210\3\2\2\2")
        buf.write("\u00a5\u0214\3\2\2\2\u00a7\u021a\3\2\2\2\u00a9\u0228\3")
        buf.write("\2\2\2\u00ab\u0233\3\2\2\2\u00ad\u023e\3\2\2\2\u00af\u0240")
        buf.write("\3\2\2\2\u00b1\u00b2\t\2\2\2\u00b2\4\3\2\2\2\u00b3\u00b4")
        buf.write("\t\3\2\2\u00b4\6\3\2\2\2\u00b5\u00b6\t\4\2\2\u00b6\b\3")
        buf.write("\2\2\2\u00b7\u00b8\t\5\2\2\u00b8\n\3\2\2\2\u00b9\u00ba")
        buf.write("\t\6\2\2\u00ba\f\3\2\2\2\u00bb\u00bc\t\7\2\2\u00bc\16")
        buf.write("\3\2\2\2\u00bd\u00be\t\b\2\2\u00be\20\3\2\2\2\u00bf\u00c0")
        buf.write("\t\t\2\2\u00c0\22\3\2\2\2\u00c1\u00c2\t\n\2\2\u00c2\24")
        buf.write("\3\2\2\2\u00c3\u00c4\t\13\2\2\u00c4\26\3\2\2\2\u00c5\u00c6")
        buf.write("\t\f\2\2\u00c6\30\3\2\2\2\u00c7\u00c8\t\r\2\2\u00c8\32")
        buf.write("\3\2\2\2\u00c9\u00ca\t\16\2\2\u00ca\34\3\2\2\2\u00cb\u00cc")
        buf.write("\t\17\2\2\u00cc\36\3\2\2\2\u00cd\u00ce\t\20\2\2\u00ce")
        buf.write(" \3\2\2\2\u00cf\u00d0\t\21\2\2\u00d0\"\3\2\2\2\u00d1\u00d2")
        buf.write("\t\22\2\2\u00d2$\3\2\2\2\u00d3\u00d4\t\23\2\2\u00d4&\3")
        buf.write("\2\2\2\u00d5\u00d6\t\24\2\2\u00d6(\3\2\2\2\u00d7\u00d8")
        buf.write("\t\25\2\2\u00d8*\3\2\2\2\u00d9\u00da\t\26\2\2\u00da,\3")
        buf.write("\2\2\2\u00db\u00dc\t\27\2\2\u00dc.\3\2\2\2\u00dd\u00de")
        buf.write("\t\30\2\2\u00de\60\3\2\2\2\u00df\u00e0\t\31\2\2\u00e0")
        buf.write("\62\3\2\2\2\u00e1\u00e2\t\32\2\2\u00e2\64\3\2\2\2\u00e3")
        buf.write("\u00e4\t\33\2\2\u00e4\66\3\2\2\2\u00e5\u00e6\5\5\3\2\u00e6")
        buf.write("\u00e7\5%\23\2\u00e7\u00e8\5\13\6\2\u00e8\u00e9\5\3\2")
        buf.write("\2\u00e9\u00ea\5\27\f\2\u00ea8\3\2\2\2\u00eb\u00ec\5\7")
        buf.write("\4\2\u00ec\u00ed\5\37\20\2\u00ed\u00ee\5\35\17\2\u00ee")
        buf.write("\u00ef\5)\25\2\u00ef\u00f0\5\23\n\2\u00f0\u00f1\5\35\17")
        buf.write("\2\u00f1\u00f2\5+\26\2\u00f2\u00f3\5\13\6\2\u00f3:\3\2")
        buf.write("\2\2\u00f4\u00f5\5\r\7\2\u00f5\u00f6\5\37\20\2\u00f6\u00f7")
        buf.write("\5%\23\2\u00f7<\3\2\2\2\u00f8\u00f9\5)\25\2\u00f9\u00fa")
        buf.write("\5\37\20\2\u00fa>\3\2\2\2\u00fb\u00fc\5\t\5\2\u00fc\u00fd")
        buf.write("\5\37\20\2\u00fd\u00fe\5/\30\2\u00fe\u00ff\5\35\17\2\u00ff")
        buf.write("\u0100\5)\25\2\u0100\u0101\5\37\20\2\u0101@\3\2\2\2\u0102")
        buf.write("\u0103\5\t\5\2\u0103\u0104\5\37\20\2\u0104B\3\2\2\2\u0105")
        buf.write("\u0106\5\23\n\2\u0106\u0107\5\r\7\2\u0107D\3\2\2\2\u0108")
        buf.write("\u0109\5)\25\2\u0109\u010a\5\21\t\2\u010a\u010b\5\13\6")
        buf.write("\2\u010b\u010c\5\35\17\2\u010cF\3\2\2\2\u010d\u010e\5")
        buf.write("\13\6\2\u010e\u010f\5\31\r\2\u010f\u0110\5\'\24\2\u0110")
        buf.write("\u0111\5\13\6\2\u0111H\3\2\2\2\u0112\u0113\5%\23\2\u0113")
        buf.write("\u0114\5\13\6\2\u0114\u0115\5)\25\2\u0115\u0116\5+\26")
        buf.write("\2\u0116\u0117\5%\23\2\u0117\u0118\5\35\17\2\u0118J\3")
        buf.write("\2\2\2\u0119\u011a\5/\30\2\u011a\u011b\5\21\t\2\u011b")
        buf.write("\u011c\5\23\n\2\u011c\u011d\5\31\r\2\u011d\u011e\5\13")
        buf.write("\6\2\u011eL\3\2\2\2\u011f\u0120\5\5\3\2\u0120\u0121\5")
        buf.write("\13\6\2\u0121\u0122\5\17\b\2\u0122\u0123\5\23\n\2\u0123")
        buf.write("\u0124\5\35\17\2\u0124N\3\2\2\2\u0125\u0126\5\13\6\2\u0126")
        buf.write("\u0127\5\35\17\2\u0127\u0128\5\t\5\2\u0128P\3\2\2\2\u0129")
        buf.write("\u012a\5\r\7\2\u012a\u012b\5+\26\2\u012b\u012c\5\35\17")
        buf.write("\2\u012c\u012d\5\7\4\2\u012d\u012e\5)\25\2\u012e\u012f")
        buf.write("\5\23\n\2\u012f\u0130\5\37\20\2\u0130\u0131\5\35\17\2")
        buf.write("\u0131R\3\2\2\2\u0132\u0133\5!\21\2\u0133\u0134\5%\23")
        buf.write("\2\u0134\u0135\5\37\20\2\u0135\u0136\5\7\4\2\u0136\u0137")
        buf.write("\5\13\6\2\u0137\u0138\5\t\5\2\u0138\u0139\5+\26\2\u0139")
        buf.write("\u013a\5%\23\2\u013a\u013b\5\13\6\2\u013bT\3\2\2\2\u013c")
        buf.write("\u013d\5-\27\2\u013d\u013e\5\3\2\2\u013e\u013f\5%\23\2")
        buf.write("\u013fV\3\2\2\2\u0140\u0141\5)\25\2\u0141\u0142\5%\23")
        buf.write("\2\u0142\u0143\5+\26\2\u0143\u0144\5\13\6\2\u0144X\3\2")
        buf.write("\2\2\u0145\u0146\5\r\7\2\u0146\u0147\5\3\2\2\u0147\u0148")
        buf.write("\5\31\r\2\u0148\u0149\5\'\24\2\u0149\u014a\5\13\6\2\u014a")
        buf.write("Z\3\2\2\2\u014b\u014c\5\3\2\2\u014c\u014d\5%\23\2\u014d")
        buf.write("\u014e\5%\23\2\u014e\u014f\5\3\2\2\u014f\u0150\5\63\32")
        buf.write("\2\u0150\\\3\2\2\2\u0151\u0152\5\37\20\2\u0152\u0153\5")
        buf.write("\r\7\2\u0153^\3\2\2\2\u0154\u0155\5%\23\2\u0155\u0156")
        buf.write("\5\13\6\2\u0156\u0157\5\3\2\2\u0157\u0158\5\31\r\2\u0158")
        buf.write("`\3\2\2\2\u0159\u015a\5\5\3\2\u015a\u015b\5\37\20\2\u015b")
        buf.write("\u015c\5\37\20\2\u015c\u015d\5\31\r\2\u015d\u015e\5\13")
        buf.write("\6\2\u015e\u015f\5\3\2\2\u015f\u0160\5\35\17\2\u0160b")
        buf.write("\3\2\2\2\u0161\u0162\5\23\n\2\u0162\u0163\5\35\17\2\u0163")
        buf.write("\u0164\5)\25\2\u0164\u0165\5\13\6\2\u0165\u0166\5\17\b")
        buf.write("\2\u0166\u0167\5\13\6\2\u0167\u0168\5%\23\2\u0168d\3\2")
        buf.write("\2\2\u0169\u016a\5\'\24\2\u016a\u016b\5)\25\2\u016b\u016c")
        buf.write("\5%\23\2\u016c\u016d\5\23\n\2\u016d\u016e\5\35\17\2\u016e")
        buf.write("\u016f\5\17\b\2\u016ff\3\2\2\2\u0170\u0171\5\35\17\2\u0171")
        buf.write("\u0172\5\37\20\2\u0172\u0173\5)\25\2\u0173h\3\2\2\2\u0174")
        buf.write("\u0175\5\3\2\2\u0175\u0176\5\35\17\2\u0176\u0177\5\t\5")
        buf.write("\2\u0177j\3\2\2\2\u0178\u0179\5\37\20\2\u0179\u017a\5")
        buf.write("%\23\2\u017al\3\2\2\2\u017b\u017c\5\t\5\2\u017c\u017d")
        buf.write("\5\23\n\2\u017d\u017e\5-\27\2\u017en\3\2\2\2\u017f\u0180")
        buf.write("\5\33\16\2\u0180\u0181\5\37\20\2\u0181\u0182\5\t\5\2\u0182")
        buf.write("p\3\2\2\2\u0183\u019e\5\3\2\2\u0184\u019e\5\5\3\2\u0185")
        buf.write("\u019e\5\7\4\2\u0186\u019e\5\t\5\2\u0187\u019e\5\13\6")
        buf.write("\2\u0188\u019e\5\r\7\2\u0189\u019e\5\17\b\2\u018a\u019e")
        buf.write("\5\21\t\2\u018b\u019e\5\23\n\2\u018c\u019e\5\25\13\2\u018d")
        buf.write("\u019e\5\27\f\2\u018e\u019e\5\31\r\2\u018f\u019e\5\33")
        buf.write("\16\2\u0190\u019e\5\35\17\2\u0191\u019e\5\37\20\2\u0192")
        buf.write("\u019e\5!\21\2\u0193\u019e\5#\22\2\u0194\u019e\5%\23\2")
        buf.write("\u0195\u019e\5\'\24\2\u0196\u019e\5)\25\2\u0197\u019e")
        buf.write("\5+\26\2\u0198\u019e\5-\27\2\u0199\u019e\5/\30\2\u019a")
        buf.write("\u019e\5\61\31\2\u019b\u019e\5\63\32\2\u019c\u019e\5\65")
        buf.write("\33\2\u019d\u0183\3\2\2\2\u019d\u0184\3\2\2\2\u019d\u0185")
        buf.write("\3\2\2\2\u019d\u0186\3\2\2\2\u019d\u0187\3\2\2\2\u019d")
        buf.write("\u0188\3\2\2\2\u019d\u0189\3\2\2\2\u019d\u018a\3\2\2\2")
        buf.write("\u019d\u018b\3\2\2\2\u019d\u018c\3\2\2\2\u019d\u018d\3")
        buf.write("\2\2\2\u019d\u018e\3\2\2\2\u019d\u018f\3\2\2\2\u019d\u0190")
        buf.write("\3\2\2\2\u019d\u0191\3\2\2\2\u019d\u0192\3\2\2\2\u019d")
        buf.write("\u0193\3\2\2\2\u019d\u0194\3\2\2\2\u019d\u0195\3\2\2\2")
        buf.write("\u019d\u0196\3\2\2\2\u019d\u0197\3\2\2\2\u019d\u0198\3")
        buf.write("\2\2\2\u019d\u0199\3\2\2\2\u019d\u019a\3\2\2\2\u019d\u019b")
        buf.write("\3\2\2\2\u019d\u019c\3\2\2\2\u019er\3\2\2\2\u019f\u01a2")
        buf.write("\5q9\2\u01a0\u01a2\7a\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a0")
        buf.write("\3\2\2\2\u01a2\u01a7\3\2\2\2\u01a3\u01a6\5q9\2\u01a4\u01a6")
        buf.write("\t\34\2\2\u01a5\u01a3\3\2\2\2\u01a5\u01a4\3\2\2\2\u01a6")
        buf.write("\u01a9\3\2\2\2\u01a7\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2")
        buf.write("\u01a8t\3\2\2\2\u01a9\u01a7\3\2\2\2\u01aa\u01ab\7-\2\2")
        buf.write("\u01abv\3\2\2\2\u01ac\u01ad\7,\2\2\u01adx\3\2\2\2\u01ae")
        buf.write("\u01af\7>\2\2\u01af\u01b0\7@\2\2\u01b0z\3\2\2\2\u01b1")
        buf.write("\u01b2\7>\2\2\u01b2|\3\2\2\2\u01b3\u01b4\7>\2\2\u01b4")
        buf.write("\u01b5\7?\2\2\u01b5~\3\2\2\2\u01b6\u01b7\7/\2\2\u01b7")
        buf.write("\u0080\3\2\2\2\u01b8\u01b9\7\61\2\2\u01b9\u0082\3\2\2")
        buf.write("\2\u01ba\u01bb\7?\2\2\u01bb\u0084\3\2\2\2\u01bc\u01bd")
        buf.write("\7@\2\2\u01bd\u0086\3\2\2\2\u01be\u01bf\7@\2\2\u01bf\u01c0")
        buf.write("\7?\2\2\u01c0\u0088\3\2\2\2\u01c1\u01c2\t\35\2\2\u01c2")
        buf.write("\u008a\3\2\2\2\u01c3\u01c5\5\u0089E\2\u01c4\u01c3\3\2")
        buf.write("\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c7")
        buf.write("\3\2\2\2\u01c7\u008c\3\2\2\2\u01c8\u01cf\5\u0091I\2\u01c9")
        buf.write("\u01cb\5\u0089E\2\u01ca\u01c9\3\2\2\2\u01cb\u01cc\3\2")
        buf.write("\2\2\u01cc\u01ca\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01cf")
        buf.write("\3\2\2\2\u01ce\u01c8\3\2\2\2\u01ce\u01ca\3\2\2\2\u01cf")
        buf.write("\u01d0\3\2\2\2\u01d0\u01d1\5\u0093J\2\u01d1\u01d4\3\2")
        buf.write("\2\2\u01d2\u01d4\5\u0091I\2\u01d3\u01ce\3\2\2\2\u01d3")
        buf.write("\u01d2\3\2\2\2\u01d4\u008e\3\2\2\2\u01d5\u01d9\7$\2\2")
        buf.write("\u01d6\u01d8\n\36\2\2\u01d7\u01d6\3\2\2\2\u01d8\u01db")
        buf.write("\3\2\2\2\u01d9\u01d7\3\2\2\2\u01d9\u01da\3\2\2\2\u01da")
        buf.write("\u01dc\3\2\2\2\u01db\u01d9\3\2\2\2\u01dc\u01dd\7$\2\2")
        buf.write("\u01dd\u01de\bH\2\2\u01de\u0090\3\2\2\2\u01df\u01e1\5")
        buf.write("\u0089E\2\u01e0\u01df\3\2\2\2\u01e1\u01e4\3\2\2\2\u01e2")
        buf.write("\u01e0\3\2\2\2\u01e2\u01e3\3\2\2\2\u01e3\u01e5\3\2\2\2")
        buf.write("\u01e4\u01e2\3\2\2\2\u01e5\u01e7\7\60\2\2\u01e6\u01e8")
        buf.write("\5\u0089E\2\u01e7\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9")
        buf.write("\u01e7\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u01f8\3\2\2\2")
        buf.write("\u01eb\u01ed\5\u0089E\2\u01ec\u01eb\3\2\2\2\u01ed\u01ee")
        buf.write("\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef")
        buf.write("\u01f0\3\2\2\2\u01f0\u01f4\7\60\2\2\u01f1\u01f3\5\u0089")
        buf.write("E\2\u01f2\u01f1\3\2\2\2\u01f3\u01f6\3\2\2\2\u01f4\u01f2")
        buf.write("\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f8\3\2\2\2\u01f6")
        buf.write("\u01f4\3\2\2\2\u01f7\u01e2\3\2\2\2\u01f7\u01ec\3\2\2\2")
        buf.write("\u01f8\u0092\3\2\2\2\u01f9\u01fb\5\13\6\2\u01fa\u01fc")
        buf.write("\7/\2\2\u01fb\u01fa\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc")
        buf.write("\u01fe\3\2\2\2\u01fd\u01ff\5\u0089E\2\u01fe\u01fd\3\2")
        buf.write("\2\2\u01ff\u0200\3\2\2\2\u0200\u01fe\3\2\2\2\u0200\u0201")
        buf.write("\3\2\2\2\u0201\u0094\3\2\2\2\u0202\u0203\7*\2\2\u0203")
        buf.write("\u0096\3\2\2\2\u0204\u0205\7+\2\2\u0205\u0098\3\2\2\2")
        buf.write("\u0206\u0207\7=\2\2\u0207\u009a\3\2\2\2\u0208\u0209\7")
        buf.write(".\2\2\u0209\u009c\3\2\2\2\u020a\u020b\7]\2\2\u020b\u009e")
        buf.write("\3\2\2\2\u020c\u020d\7_\2\2\u020d\u00a0\3\2\2\2\u020e")
        buf.write("\u020f\7<\2\2\u020f\u00a2\3\2\2\2\u0210\u0211\7\60\2\2")
        buf.write("\u0211\u0212\7\60\2\2\u0212\u00a4\3\2\2\2\u0213\u0215")
        buf.write("\t\37\2\2\u0214\u0213\3\2\2\2\u0215\u0216\3\2\2\2\u0216")
        buf.write("\u0214\3\2\2\2\u0216\u0217\3\2\2\2\u0217\u0218\3\2\2\2")
        buf.write("\u0218\u0219\bS\3\2\u0219\u00a6\3\2\2\2\u021a\u021b\7")
        buf.write("*\2\2\u021b\u021c\7,\2\2\u021c\u0220\3\2\2\2\u021d\u021f")
        buf.write("\13\2\2\2\u021e\u021d\3\2\2\2\u021f\u0222\3\2\2\2\u0220")
        buf.write("\u0221\3\2\2\2\u0220\u021e\3\2\2\2\u0221\u0223\3\2\2\2")
        buf.write("\u0222\u0220\3\2\2\2\u0223\u0224\7,\2\2\u0224\u0225\7")
        buf.write("+\2\2\u0225\u0226\3\2\2\2\u0226\u0227\bT\3\2\u0227\u00a8")
        buf.write("\3\2\2\2\u0228\u022c\7}\2\2\u0229\u022b\13\2\2\2\u022a")
        buf.write("\u0229\3\2\2\2\u022b\u022e\3\2\2\2\u022c\u022d\3\2\2\2")
        buf.write("\u022c\u022a\3\2\2\2\u022d\u022f\3\2\2\2\u022e\u022c\3")
        buf.write("\2\2\2\u022f\u0230\7\177\2\2\u0230\u0231\3\2\2\2\u0231")
        buf.write("\u0232\bU\3\2\u0232\u00aa\3\2\2\2\u0233\u0234\7\61\2\2")
        buf.write("\u0234\u0235\7\61\2\2\u0235\u0239\3\2\2\2\u0236\u0238")
        buf.write("\n \2\2\u0237\u0236\3\2\2\2\u0238\u023b\3\2\2\2\u0239")
        buf.write("\u0237\3\2\2\2\u0239\u023a\3\2\2\2\u023a\u023c\3\2\2\2")
        buf.write("\u023b\u0239\3\2\2\2\u023c\u023d\bV\3\2\u023d\u00ac\3")
        buf.write("\2\2\2\u023e\u023f\13\2\2\2\u023f\u00ae\3\2\2\2\u0240")
        buf.write("\u0244\7$\2\2\u0241\u0243\n!\2\2\u0242\u0241\3\2\2\2\u0243")
        buf.write("\u0246\3\2\2\2\u0244\u0242\3\2\2\2\u0244\u0245\3\2\2\2")
        buf.write("\u0245\u0247\3\2\2\2\u0246\u0244\3\2\2\2\u0247\u0248\b")
        buf.write("X\4\2\u0248\u00b0\3\2\2\2\30\2\u019d\u01a1\u01a5\u01a7")
        buf.write("\u01c6\u01cc\u01ce\u01d3\u01d9\u01e2\u01e9\u01ee\u01f4")
        buf.write("\u01f7\u01fb\u0200\u0216\u0220\u022c\u0239\u0244\5\3H")
        buf.write("\2\b\2\2\3X\3")
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
    REALIT = 42
    STRLIT = 43
    LB = 44
    RB = 45
    SEMI = 46
    COMMA = 47
    LSB = 48
    RSB = 49
    COLON = 50
    DDOT = 51
    WS = 52
    BLOCKCOM_B = 53
    BLOCKCOM_P = 54
    LINECOM = 55
    ERROR_CHAR = 56
    UNCLOSE_STRING = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'*'", "'<>'", "'<'", "'<='", "'-'", "'/'", "'='", "'>'", 
            "'>='", "'('", "')'", "';'", "','", "'['", "']'", "':'", "'..'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", 
            "ELSE", "RETURNS", "WHILE", "BEGIN", "END", "FUNCTION", "PROCEDURE", 
            "VAR", "TRUE", "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", 
            "STRING", "NOT", "AND", "OR", "DIV", "MOD", "ID", "ADDOP", "MULOP", 
            "NEQOP", "LTOP", "LTEOP", "SUBOP", "DIVOP", "EQOP", "GTOP", 
            "GTEOP", "INTLIT", "REALIT", "STRLIT", "LB", "RB", "SEMI", "COMMA", 
            "LSB", "RSB", "COLON", "DDOT", "WS", "BLOCKCOM_B", "BLOCKCOM_P", 
            "LINECOM", "ERROR_CHAR", "UNCLOSE_STRING" ]

    ruleNames = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                  "W", "X", "Y", "Z", "BREAK", "CONTINUE", "FOR", "TO", 
                  "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURNS", "WHILE", 
                  "BEGIN", "END", "FUNCTION", "PROCEDURE", "VAR", "TRUE", 
                  "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", 
                  "STRING", "NOT", "AND", "OR", "DIV", "MOD", "IDCHAR", 
                  "ID", "ADDOP", "MULOP", "NEQOP", "LTOP", "LTEOP", "SUBOP", 
                  "DIVOP", "EQOP", "GTOP", "GTEOP", "DIGIT", "INTLIT", "REALIT", 
                  "STRLIT", "NUM_HAS_P", "EXPN", "LB", "RB", "SEMI", "COMMA", 
                  "LSB", "RSB", "COLON", "DDOT", "WS", "BLOCKCOM_B", "BLOCKCOM_P", 
                  "LINECOM", "ERROR_CHAR", "UNCLOSE_STRING" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[70] = self.STRLIT_action 
            actions[86] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                                        self.text = self.text[1:len(self.text)-1]
                                    
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                            self.text = self.text[1:]        
                        
     


