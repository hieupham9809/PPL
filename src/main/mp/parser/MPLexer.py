# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\29")
        buf.write("\u0231\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\4V\tV\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3")
        buf.write("\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3")
        buf.write("\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3")
        buf.write("!\3!\3!\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3,\3-\3-\3")
        buf.write("-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\67\3\67\3\67\3\67\38\38\38\38\39\39")
        buf.write("\39\39\39\39\39\39\39\39\39\39\39\39\39\39\39\39\39\3")
        buf.write("9\39\39\39\39\39\39\59\u019a\n9\3:\3:\5:\u019e\n:\3:\3")
        buf.write(":\7:\u01a2\n:\f:\16:\u01a5\13:\3;\3;\3<\3<\3=\3=\3=\3")
        buf.write(">\3>\3?\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3D\3E\3E\3")
        buf.write("F\6F\u01c1\nF\rF\16F\u01c2\3G\3G\6G\u01c7\nG\rG\16G\u01c8")
        buf.write("\5G\u01cb\nG\3G\3G\3G\5G\u01d0\nG\3H\7H\u01d3\nH\fH\16")
        buf.write("H\u01d6\13H\3H\3H\6H\u01da\nH\rH\16H\u01db\3H\6H\u01df")
        buf.write("\nH\rH\16H\u01e0\3H\3H\7H\u01e5\nH\fH\16H\u01e8\13H\5")
        buf.write("H\u01ea\nH\3I\3I\5I\u01ee\nI\3I\6I\u01f1\nI\rI\16I\u01f2")
        buf.write("\3J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\3P\6P\u0202\nP\r")
        buf.write("P\16P\u0203\3P\3P\3Q\3Q\3Q\3Q\7Q\u020c\nQ\fQ\16Q\u020f")
        buf.write("\13Q\3Q\3Q\3Q\3Q\3Q\3R\3R\7R\u0218\nR\fR\16R\u021b\13")
        buf.write("R\3R\3R\3R\3R\3S\3S\3S\3S\7S\u0225\nS\fS\16S\u0228\13")
        buf.write("S\3S\3S\3T\3T\3U\3U\3V\3V\4\u020d\u0219\2W\3\2\5\2\7\2")
        buf.write("\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31\2\33\2\35\2")
        buf.write("\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63\2\65\2\67\39\4")
        buf.write(";\5=\6?\7A\bC\tE\nG\13I\fK\rM\16O\17Q\20S\21U\22W\23Y")
        buf.write("\24[\25]\26_\27a\30c\31e\32g\33i\34k\35m\36o\37q\2s u")
        buf.write("!w\"y#{$}%\177&\u0081\'\u0083(\u0085)\u0087*\u0089\2\u008b")
        buf.write("+\u008d,\u008f\2\u0091\2\u0093-\u0095.\u0097/\u0099\60")
        buf.write("\u009b\61\u009d\62\u009f\63\u00a1\64\u00a3\65\u00a5\66")
        buf.write("\u00a7\67\u00a98\u00ab9\3\2 \4\2CCcc\4\2DDdd\4\2EEee\4")
        buf.write("\2FFff\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLl")
        buf.write("l\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2")
        buf.write("SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4")
        buf.write("\2ZZzz\4\2[[{{\4\2\\\\||\4\2\62;aa\3\2\62;\5\2\13\f\17")
        buf.write("\17\"\"\4\2\f\f\17\17\2\u023d\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2")
        buf.write("\u0087\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2")
        buf.write("\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1")
        buf.write("\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2")
        buf.write("\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\3\u00ad\3\2\2\2\5\u00af")
        buf.write("\3\2\2\2\7\u00b1\3\2\2\2\t\u00b3\3\2\2\2\13\u00b5\3\2")
        buf.write("\2\2\r\u00b7\3\2\2\2\17\u00b9\3\2\2\2\21\u00bb\3\2\2\2")
        buf.write("\23\u00bd\3\2\2\2\25\u00bf\3\2\2\2\27\u00c1\3\2\2\2\31")
        buf.write("\u00c3\3\2\2\2\33\u00c5\3\2\2\2\35\u00c7\3\2\2\2\37\u00c9")
        buf.write("\3\2\2\2!\u00cb\3\2\2\2#\u00cd\3\2\2\2%\u00cf\3\2\2\2")
        buf.write("\'\u00d1\3\2\2\2)\u00d3\3\2\2\2+\u00d5\3\2\2\2-\u00d7")
        buf.write("\3\2\2\2/\u00d9\3\2\2\2\61\u00db\3\2\2\2\63\u00dd\3\2")
        buf.write("\2\2\65\u00df\3\2\2\2\67\u00e1\3\2\2\29\u00e7\3\2\2\2")
        buf.write(";\u00f0\3\2\2\2=\u00f4\3\2\2\2?\u00f7\3\2\2\2A\u00fe\3")
        buf.write("\2\2\2C\u0101\3\2\2\2E\u0104\3\2\2\2G\u0109\3\2\2\2I\u010e")
        buf.write("\3\2\2\2K\u0115\3\2\2\2M\u011b\3\2\2\2O\u0121\3\2\2\2")
        buf.write("Q\u0125\3\2\2\2S\u012e\3\2\2\2U\u0138\3\2\2\2W\u013c\3")
        buf.write("\2\2\2Y\u0141\3\2\2\2[\u0147\3\2\2\2]\u014d\3\2\2\2_\u0150")
        buf.write("\3\2\2\2a\u0155\3\2\2\2c\u015d\3\2\2\2e\u0165\3\2\2\2")
        buf.write("g\u016c\3\2\2\2i\u0170\3\2\2\2k\u0174\3\2\2\2m\u0177\3")
        buf.write("\2\2\2o\u017b\3\2\2\2q\u0199\3\2\2\2s\u019d\3\2\2\2u\u01a6")
        buf.write("\3\2\2\2w\u01a8\3\2\2\2y\u01aa\3\2\2\2{\u01ad\3\2\2\2")
        buf.write("}\u01af\3\2\2\2\177\u01b2\3\2\2\2\u0081\u01b4\3\2\2\2")
        buf.write("\u0083\u01b6\3\2\2\2\u0085\u01b8\3\2\2\2\u0087\u01ba\3")
        buf.write("\2\2\2\u0089\u01bd\3\2\2\2\u008b\u01c0\3\2\2\2\u008d\u01cf")
        buf.write("\3\2\2\2\u008f\u01e9\3\2\2\2\u0091\u01eb\3\2\2\2\u0093")
        buf.write("\u01f4\3\2\2\2\u0095\u01f6\3\2\2\2\u0097\u01f8\3\2\2\2")
        buf.write("\u0099\u01fa\3\2\2\2\u009b\u01fc\3\2\2\2\u009d\u01fe\3")
        buf.write("\2\2\2\u009f\u0201\3\2\2\2\u00a1\u0207\3\2\2\2\u00a3\u0215")
        buf.write("\3\2\2\2\u00a5\u0220\3\2\2\2\u00a7\u022b\3\2\2\2\u00a9")
        buf.write("\u022d\3\2\2\2\u00ab\u022f\3\2\2\2\u00ad\u00ae\t\2\2\2")
        buf.write("\u00ae\4\3\2\2\2\u00af\u00b0\t\3\2\2\u00b0\6\3\2\2\2\u00b1")
        buf.write("\u00b2\t\4\2\2\u00b2\b\3\2\2\2\u00b3\u00b4\t\5\2\2\u00b4")
        buf.write("\n\3\2\2\2\u00b5\u00b6\t\6\2\2\u00b6\f\3\2\2\2\u00b7\u00b8")
        buf.write("\t\7\2\2\u00b8\16\3\2\2\2\u00b9\u00ba\t\b\2\2\u00ba\20")
        buf.write("\3\2\2\2\u00bb\u00bc\t\t\2\2\u00bc\22\3\2\2\2\u00bd\u00be")
        buf.write("\t\n\2\2\u00be\24\3\2\2\2\u00bf\u00c0\t\13\2\2\u00c0\26")
        buf.write("\3\2\2\2\u00c1\u00c2\t\f\2\2\u00c2\30\3\2\2\2\u00c3\u00c4")
        buf.write("\t\r\2\2\u00c4\32\3\2\2\2\u00c5\u00c6\t\16\2\2\u00c6\34")
        buf.write("\3\2\2\2\u00c7\u00c8\t\17\2\2\u00c8\36\3\2\2\2\u00c9\u00ca")
        buf.write("\t\20\2\2\u00ca \3\2\2\2\u00cb\u00cc\t\21\2\2\u00cc\"")
        buf.write("\3\2\2\2\u00cd\u00ce\t\22\2\2\u00ce$\3\2\2\2\u00cf\u00d0")
        buf.write("\t\23\2\2\u00d0&\3\2\2\2\u00d1\u00d2\t\24\2\2\u00d2(\3")
        buf.write("\2\2\2\u00d3\u00d4\t\25\2\2\u00d4*\3\2\2\2\u00d5\u00d6")
        buf.write("\t\26\2\2\u00d6,\3\2\2\2\u00d7\u00d8\t\27\2\2\u00d8.\3")
        buf.write("\2\2\2\u00d9\u00da\t\30\2\2\u00da\60\3\2\2\2\u00db\u00dc")
        buf.write("\t\31\2\2\u00dc\62\3\2\2\2\u00dd\u00de\t\32\2\2\u00de")
        buf.write("\64\3\2\2\2\u00df\u00e0\t\33\2\2\u00e0\66\3\2\2\2\u00e1")
        buf.write("\u00e2\5\5\3\2\u00e2\u00e3\5%\23\2\u00e3\u00e4\5\13\6")
        buf.write("\2\u00e4\u00e5\5\3\2\2\u00e5\u00e6\5\27\f\2\u00e68\3\2")
        buf.write("\2\2\u00e7\u00e8\5\7\4\2\u00e8\u00e9\5\37\20\2\u00e9\u00ea")
        buf.write("\5\35\17\2\u00ea\u00eb\5)\25\2\u00eb\u00ec\5\23\n\2\u00ec")
        buf.write("\u00ed\5\35\17\2\u00ed\u00ee\5+\26\2\u00ee\u00ef\5\13")
        buf.write("\6\2\u00ef:\3\2\2\2\u00f0\u00f1\5\r\7\2\u00f1\u00f2\5")
        buf.write("\37\20\2\u00f2\u00f3\5%\23\2\u00f3<\3\2\2\2\u00f4\u00f5")
        buf.write("\5)\25\2\u00f5\u00f6\5\37\20\2\u00f6>\3\2\2\2\u00f7\u00f8")
        buf.write("\5\t\5\2\u00f8\u00f9\5\37\20\2\u00f9\u00fa\5/\30\2\u00fa")
        buf.write("\u00fb\5\35\17\2\u00fb\u00fc\5)\25\2\u00fc\u00fd\5\37")
        buf.write("\20\2\u00fd@\3\2\2\2\u00fe\u00ff\5\t\5\2\u00ff\u0100\5")
        buf.write("\37\20\2\u0100B\3\2\2\2\u0101\u0102\5\23\n\2\u0102\u0103")
        buf.write("\5\r\7\2\u0103D\3\2\2\2\u0104\u0105\5)\25\2\u0105\u0106")
        buf.write("\5\21\t\2\u0106\u0107\5\13\6\2\u0107\u0108\5\35\17\2\u0108")
        buf.write("F\3\2\2\2\u0109\u010a\5\13\6\2\u010a\u010b\5\31\r\2\u010b")
        buf.write("\u010c\5\'\24\2\u010c\u010d\5\13\6\2\u010dH\3\2\2\2\u010e")
        buf.write("\u010f\5%\23\2\u010f\u0110\5\13\6\2\u0110\u0111\5)\25")
        buf.write("\2\u0111\u0112\5+\26\2\u0112\u0113\5%\23\2\u0113\u0114")
        buf.write("\5\35\17\2\u0114J\3\2\2\2\u0115\u0116\5/\30\2\u0116\u0117")
        buf.write("\5\21\t\2\u0117\u0118\5\23\n\2\u0118\u0119\5\31\r\2\u0119")
        buf.write("\u011a\5\13\6\2\u011aL\3\2\2\2\u011b\u011c\5\5\3\2\u011c")
        buf.write("\u011d\5\13\6\2\u011d\u011e\5\17\b\2\u011e\u011f\5\23")
        buf.write("\n\2\u011f\u0120\5\35\17\2\u0120N\3\2\2\2\u0121\u0122")
        buf.write("\5\13\6\2\u0122\u0123\5\35\17\2\u0123\u0124\5\t\5\2\u0124")
        buf.write("P\3\2\2\2\u0125\u0126\5\r\7\2\u0126\u0127\5+\26\2\u0127")
        buf.write("\u0128\5\35\17\2\u0128\u0129\5\7\4\2\u0129\u012a\5)\25")
        buf.write("\2\u012a\u012b\5\23\n\2\u012b\u012c\5\37\20\2\u012c\u012d")
        buf.write("\5\35\17\2\u012dR\3\2\2\2\u012e\u012f\5!\21\2\u012f\u0130")
        buf.write("\5%\23\2\u0130\u0131\5\37\20\2\u0131\u0132\5\7\4\2\u0132")
        buf.write("\u0133\5\13\6\2\u0133\u0134\5\t\5\2\u0134\u0135\5+\26")
        buf.write("\2\u0135\u0136\5%\23\2\u0136\u0137\5\13\6\2\u0137T\3\2")
        buf.write("\2\2\u0138\u0139\5-\27\2\u0139\u013a\5\3\2\2\u013a\u013b")
        buf.write("\5%\23\2\u013bV\3\2\2\2\u013c\u013d\5)\25\2\u013d\u013e")
        buf.write("\5%\23\2\u013e\u013f\5+\26\2\u013f\u0140\5\13\6\2\u0140")
        buf.write("X\3\2\2\2\u0141\u0142\5\r\7\2\u0142\u0143\5\3\2\2\u0143")
        buf.write("\u0144\5\31\r\2\u0144\u0145\5\'\24\2\u0145\u0146\5\13")
        buf.write("\6\2\u0146Z\3\2\2\2\u0147\u0148\5\3\2\2\u0148\u0149\5")
        buf.write("%\23\2\u0149\u014a\5%\23\2\u014a\u014b\5\3\2\2\u014b\u014c")
        buf.write("\5\63\32\2\u014c\\\3\2\2\2\u014d\u014e\5\37\20\2\u014e")
        buf.write("\u014f\5\r\7\2\u014f^\3\2\2\2\u0150\u0151\5%\23\2\u0151")
        buf.write("\u0152\5\13\6\2\u0152\u0153\5\3\2\2\u0153\u0154\5\31\r")
        buf.write("\2\u0154`\3\2\2\2\u0155\u0156\5\5\3\2\u0156\u0157\5\37")
        buf.write("\20\2\u0157\u0158\5\37\20\2\u0158\u0159\5\31\r\2\u0159")
        buf.write("\u015a\5\13\6\2\u015a\u015b\5\3\2\2\u015b\u015c\5\35\17")
        buf.write("\2\u015cb\3\2\2\2\u015d\u015e\5\23\n\2\u015e\u015f\5\35")
        buf.write("\17\2\u015f\u0160\5)\25\2\u0160\u0161\5\13\6\2\u0161\u0162")
        buf.write("\5\17\b\2\u0162\u0163\5\13\6\2\u0163\u0164\5%\23\2\u0164")
        buf.write("d\3\2\2\2\u0165\u0166\5\'\24\2\u0166\u0167\5)\25\2\u0167")
        buf.write("\u0168\5%\23\2\u0168\u0169\5\23\n\2\u0169\u016a\5\35\17")
        buf.write("\2\u016a\u016b\5\17\b\2\u016bf\3\2\2\2\u016c\u016d\5\35")
        buf.write("\17\2\u016d\u016e\5\37\20\2\u016e\u016f\5)\25\2\u016f")
        buf.write("h\3\2\2\2\u0170\u0171\5\3\2\2\u0171\u0172\5\35\17\2\u0172")
        buf.write("\u0173\5\t\5\2\u0173j\3\2\2\2\u0174\u0175\5\37\20\2\u0175")
        buf.write("\u0176\5%\23\2\u0176l\3\2\2\2\u0177\u0178\5\t\5\2\u0178")
        buf.write("\u0179\5\23\n\2\u0179\u017a\5-\27\2\u017an\3\2\2\2\u017b")
        buf.write("\u017c\5\33\16\2\u017c\u017d\5\37\20\2\u017d\u017e\5\t")
        buf.write("\5\2\u017ep\3\2\2\2\u017f\u019a\5\3\2\2\u0180\u019a\5")
        buf.write("\5\3\2\u0181\u019a\5\7\4\2\u0182\u019a\5\t\5\2\u0183\u019a")
        buf.write("\5\13\6\2\u0184\u019a\5\r\7\2\u0185\u019a\5\17\b\2\u0186")
        buf.write("\u019a\5\21\t\2\u0187\u019a\5\23\n\2\u0188\u019a\5\25")
        buf.write("\13\2\u0189\u019a\5\27\f\2\u018a\u019a\5\31\r\2\u018b")
        buf.write("\u019a\5\33\16\2\u018c\u019a\5\35\17\2\u018d\u019a\5\37")
        buf.write("\20\2\u018e\u019a\5!\21\2\u018f\u019a\5#\22\2\u0190\u019a")
        buf.write("\5%\23\2\u0191\u019a\5\'\24\2\u0192\u019a\5)\25\2\u0193")
        buf.write("\u019a\5+\26\2\u0194\u019a\5-\27\2\u0195\u019a\5/\30\2")
        buf.write("\u0196\u019a\5\61\31\2\u0197\u019a\5\63\32\2\u0198\u019a")
        buf.write("\5\65\33\2\u0199\u017f\3\2\2\2\u0199\u0180\3\2\2\2\u0199")
        buf.write("\u0181\3\2\2\2\u0199\u0182\3\2\2\2\u0199\u0183\3\2\2\2")
        buf.write("\u0199\u0184\3\2\2\2\u0199\u0185\3\2\2\2\u0199\u0186\3")
        buf.write("\2\2\2\u0199\u0187\3\2\2\2\u0199\u0188\3\2\2\2\u0199\u0189")
        buf.write("\3\2\2\2\u0199\u018a\3\2\2\2\u0199\u018b\3\2\2\2\u0199")
        buf.write("\u018c\3\2\2\2\u0199\u018d\3\2\2\2\u0199\u018e\3\2\2\2")
        buf.write("\u0199\u018f\3\2\2\2\u0199\u0190\3\2\2\2\u0199\u0191\3")
        buf.write("\2\2\2\u0199\u0192\3\2\2\2\u0199\u0193\3\2\2\2\u0199\u0194")
        buf.write("\3\2\2\2\u0199\u0195\3\2\2\2\u0199\u0196\3\2\2\2\u0199")
        buf.write("\u0197\3\2\2\2\u0199\u0198\3\2\2\2\u019ar\3\2\2\2\u019b")
        buf.write("\u019e\5q9\2\u019c\u019e\7a\2\2\u019d\u019b\3\2\2\2\u019d")
        buf.write("\u019c\3\2\2\2\u019e\u01a3\3\2\2\2\u019f\u01a2\5q9\2\u01a0")
        buf.write("\u01a2\t\34\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a0\3\2\2")
        buf.write("\2\u01a2\u01a5\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4")
        buf.write("\3\2\2\2\u01a4t\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a6\u01a7")
        buf.write("\7-\2\2\u01a7v\3\2\2\2\u01a8\u01a9\7,\2\2\u01a9x\3\2\2")
        buf.write("\2\u01aa\u01ab\7>\2\2\u01ab\u01ac\7@\2\2\u01acz\3\2\2")
        buf.write("\2\u01ad\u01ae\7>\2\2\u01ae|\3\2\2\2\u01af\u01b0\7>\2")
        buf.write("\2\u01b0\u01b1\7?\2\2\u01b1~\3\2\2\2\u01b2\u01b3\7/\2")
        buf.write("\2\u01b3\u0080\3\2\2\2\u01b4\u01b5\7\61\2\2\u01b5\u0082")
        buf.write("\3\2\2\2\u01b6\u01b7\7?\2\2\u01b7\u0084\3\2\2\2\u01b8")
        buf.write("\u01b9\7@\2\2\u01b9\u0086\3\2\2\2\u01ba\u01bb\7@\2\2\u01bb")
        buf.write("\u01bc\7?\2\2\u01bc\u0088\3\2\2\2\u01bd\u01be\t\35\2\2")
        buf.write("\u01be\u008a\3\2\2\2\u01bf\u01c1\5\u0089E\2\u01c0\u01bf")
        buf.write("\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2")
        buf.write("\u01c3\3\2\2\2\u01c3\u008c\3\2\2\2\u01c4\u01cb\5\u008f")
        buf.write("H\2\u01c5\u01c7\5\u0089E\2\u01c6\u01c5\3\2\2\2\u01c7\u01c8")
        buf.write("\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9")
        buf.write("\u01cb\3\2\2\2\u01ca\u01c4\3\2\2\2\u01ca\u01c6\3\2\2\2")
        buf.write("\u01cb\u01cc\3\2\2\2\u01cc\u01cd\5\u0091I\2\u01cd\u01d0")
        buf.write("\3\2\2\2\u01ce\u01d0\5\u008fH\2\u01cf\u01ca\3\2\2\2\u01cf")
        buf.write("\u01ce\3\2\2\2\u01d0\u008e\3\2\2\2\u01d1\u01d3\5\u0089")
        buf.write("E\2\u01d2\u01d1\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2")
        buf.write("\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d7\3\2\2\2\u01d6")
        buf.write("\u01d4\3\2\2\2\u01d7\u01d9\7\60\2\2\u01d8\u01da\5\u0089")
        buf.write("E\2\u01d9\u01d8\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u01d9")
        buf.write("\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01ea\3\2\2\2\u01dd")
        buf.write("\u01df\5\u0089E\2\u01de\u01dd\3\2\2\2\u01df\u01e0\3\2")
        buf.write("\2\2\u01e0\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1\u01e2")
        buf.write("\3\2\2\2\u01e2\u01e6\7\60\2\2\u01e3\u01e5\5\u0089E\2\u01e4")
        buf.write("\u01e3\3\2\2\2\u01e5\u01e8\3\2\2\2\u01e6\u01e4\3\2\2\2")
        buf.write("\u01e6\u01e7\3\2\2\2\u01e7\u01ea\3\2\2\2\u01e8\u01e6\3")
        buf.write("\2\2\2\u01e9\u01d4\3\2\2\2\u01e9\u01de\3\2\2\2\u01ea\u0090")
        buf.write("\3\2\2\2\u01eb\u01ed\5\13\6\2\u01ec\u01ee\7/\2\2\u01ed")
        buf.write("\u01ec\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01f0\3\2\2\2")
        buf.write("\u01ef\u01f1\5\u0089E\2\u01f0\u01ef\3\2\2\2\u01f1\u01f2")
        buf.write("\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3")
        buf.write("\u0092\3\2\2\2\u01f4\u01f5\7*\2\2\u01f5\u0094\3\2\2\2")
        buf.write("\u01f6\u01f7\7+\2\2\u01f7\u0096\3\2\2\2\u01f8\u01f9\7")
        buf.write("}\2\2\u01f9\u0098\3\2\2\2\u01fa\u01fb\7\177\2\2\u01fb")
        buf.write("\u009a\3\2\2\2\u01fc\u01fd\7=\2\2\u01fd\u009c\3\2\2\2")
        buf.write("\u01fe\u01ff\7.\2\2\u01ff\u009e\3\2\2\2\u0200\u0202\t")
        buf.write("\36\2\2\u0201\u0200\3\2\2\2\u0202\u0203\3\2\2\2\u0203")
        buf.write("\u0201\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0205\3\2\2\2")
        buf.write("\u0205\u0206\bP\2\2\u0206\u00a0\3\2\2\2\u0207\u0208\7")
        buf.write("*\2\2\u0208\u0209\7,\2\2\u0209\u020d\3\2\2\2\u020a\u020c")
        buf.write("\13\2\2\2\u020b\u020a\3\2\2\2\u020c\u020f\3\2\2\2\u020d")
        buf.write("\u020e\3\2\2\2\u020d\u020b\3\2\2\2\u020e\u0210\3\2\2\2")
        buf.write("\u020f\u020d\3\2\2\2\u0210\u0211\7,\2\2\u0211\u0212\7")
        buf.write("+\2\2\u0212\u0213\3\2\2\2\u0213\u0214\bQ\2\2\u0214\u00a2")
        buf.write("\3\2\2\2\u0215\u0219\7}\2\2\u0216\u0218\13\2\2\2\u0217")
        buf.write("\u0216\3\2\2\2\u0218\u021b\3\2\2\2\u0219\u021a\3\2\2\2")
        buf.write("\u0219\u0217\3\2\2\2\u021a\u021c\3\2\2\2\u021b\u0219\3")
        buf.write("\2\2\2\u021c\u021d\7\177\2\2\u021d\u021e\3\2\2\2\u021e")
        buf.write("\u021f\bR\2\2\u021f\u00a4\3\2\2\2\u0220\u0221\7\61\2\2")
        buf.write("\u0221\u0222\7\61\2\2\u0222\u0226\3\2\2\2\u0223\u0225")
        buf.write("\n\37\2\2\u0224\u0223\3\2\2\2\u0225\u0228\3\2\2\2\u0226")
        buf.write("\u0224\3\2\2\2\u0226\u0227\3\2\2\2\u0227\u0229\3\2\2\2")
        buf.write("\u0228\u0226\3\2\2\2\u0229\u022a\bS\2\2\u022a\u00a6\3")
        buf.write("\2\2\2\u022b\u022c\13\2\2\2\u022c\u00a8\3\2\2\2\u022d")
        buf.write("\u022e\13\2\2\2\u022e\u00aa\3\2\2\2\u022f\u0230\13\2\2")
        buf.write("\2\u0230\u00ac\3\2\2\2\26\2\u0199\u019d\u01a1\u01a3\u01c2")
        buf.write("\u01c8\u01ca\u01cf\u01d4\u01db\u01e0\u01e6\u01e9\u01ed")
        buf.write("\u01f2\u0203\u020d\u0219\u0226\3\b\2\2")
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
    LB = 43
    RB = 44
    LP = 45
    RP = 46
    SEMI = 47
    COMMA = 48
    WS = 49
    BLOCKCOM_B = 50
    BLOCKCOM_P = 51
    LINECOM = 52
    ERROR_CHAR = 53
    UNCLOSE_STRING = 54
    ILLEGAL_ESCAPE = 55

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'*'", "'<>'", "'<'", "'<='", "'-'", "'/'", "'='", "'>'", 
            "'>='", "'('", "')'", "'{'", "'}'", "';'", "','" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", 
            "ELSE", "RETURNS", "WHILE", "BEGIN", "END", "FUNCTION", "PROCEDURE", 
            "VAR", "TRUE", "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", 
            "STRING", "NOT", "AND", "OR", "DIV", "MOD", "ID", "ADDOP", "MULOP", 
            "NEQOP", "LTOP", "LTEOP", "SUBOP", "DIVOP", "EQOP", "GTOP", 
            "GTEOP", "INTLIT", "REALIT", "LB", "RB", "LP", "RP", "SEMI", 
            "COMMA", "WS", "BLOCKCOM_B", "BLOCKCOM_P", "LINECOM", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
                  "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
                  "W", "X", "Y", "Z", "BREAK", "CONTINUE", "FOR", "TO", 
                  "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURNS", "WHILE", 
                  "BEGIN", "END", "FUNCTION", "PROCEDURE", "VAR", "TRUE", 
                  "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", 
                  "STRING", "NOT", "AND", "OR", "DIV", "MOD", "IDCHAR", 
                  "ID", "ADDOP", "MULOP", "NEQOP", "LTOP", "LTEOP", "SUBOP", 
                  "DIVOP", "EQOP", "GTOP", "GTEOP", "DIGIT", "INTLIT", "REALIT", 
                  "NUM_HAS_P", "EXPN", "LB", "RB", "LP", "RP", "SEMI", "COMMA", 
                  "WS", "BLOCKCOM_B", "BLOCKCOM_P", "LINECOM", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


