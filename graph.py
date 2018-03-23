
import pygame
import sys
import math
from typing import *


class CircleGraph:
    def __init__(self, categories: Dict[Any, List[Any]], elements: List)->None:
        """
        This should initiate an instance of the object. It has to take a
        dictionary of the attributes that each element can have, with the
        elements as values for the keys (attributes) they are associated with.
        Then the list of PCA sorted elements. In this case the attributes are
        the HPA classes (human protein atlas) the gene is in, from the
        2018-Challenge/Chr20GeneData.tsv on the uoftbiohacks github. The
        elements are the genes.

        """
        self.cat = categories
        self.el = elements
        self.num_el = len(elements)
        self.num_cat = len(categories)

    def draw_graph(self) -> None:
        """
        This should take the data and make the graph.
        """

        #different colors we will use:
        white = (255,255,255)
        pink = (255,200,200)
        darkBlue = (0,0,128)
        black = (0,0,0)

        #thickness of the arc
        thickness = 10

        #screen measurements and measurement of square that circle will be w/in
        # screen_w = (self.num_cat * thickness * 2) + 10
        # screen_h = (self.num_cat * thickness * 2) + 10
        screen_w = 1000
        screen_h = 1000
        square = screen_w / 2


        #inital circle radius for first ring
        ICR = 10

        #degrees per slice
        dps = (math.pi * 2) / (self.num_el + 1)
        #print(dps)


        #actual window, pygame style
        pygame.init()
        screen = pygame.display.set_mode((screen_w, screen_h))
        pygame.display.set_caption("Concentricgraf")
        clock = pygame.time.Clock()
        screen.fill(white)


        #distance from center, increased by thickness for each ring
        min = ICR

        #enclosing box coordinates, because of the way pygame does the arc draw
        eb = square/2 - min
        #also, this is one variable because since it is a circle it
        # will be the same for height and width like a square

        #each ring
        for w in self.cat:

            #each gene in the ring
            for k in range(len(self.el)):

                #if the element has that attribute
                #in this case if the gene is in that class
                if self.el[k] in self.cat[w]:
                    color = darkBlue
                #if it isn't in that class
                else:
                    color = pink

                #draw slice
                pygame.draw.arc(screen, color,
                                (eb,eb,min*2,min*2),
                                dps*k, (dps * (k + 1)) + .1, thickness)
                print(str(dps*k) + " " + str(dps*(k+1)))
                #draw slice border
                # pygame.draw.arc(screen, black,
                #                 (eb,eb,min*2,min*2),
                #                 (dps * (k + 1)) - 1, (dps * (k + 1)), thickness)

            #
            min = min + thickness
            eb = eb - thickness
        pygame.display.update()
        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()






#this is presorted data that John, another group member, made.
with open ("sorted_pca.csv") as file:

    lst = []
    for line in file:
        row = line.split(",")[0]
        lst.append(row)

example = CircleGraph({"CD markers": ["CD40", "CD93", "JAG1", "PRNP", "PROCR",
"SIGLEC1", "SIRPA", "SIRPB1", "SIRPG", "THBD"], "Cancer-related genes":
["ADNP", "ASXL1", "AURKA", "BCL2L1", "BMP2", "CD40", "CDC25B", "CSE1L", "CST3",
"CTNNBL1", "E2F1", "EIF2S2", "FOXA2", "GNAS", "ID1", "MAFB", "MMP9", "MYBL2",
"NCOA3", "NFATC2", "PCNA", "PHF20", "PLCG1", "PMEPA1", "PTK6", "PTPRT", "RBL1",
"SALL4", "SDC4", "SLPI", "SRC", "SS18L1", "TOP1", "TPX2", "UBE2C", "WFDC2",
"YWHAB"], "Candidate cardiovascular disease genes": ["MMP9", "PROCR", "PYGB",
"THBD"], "Citric acid cycle related proteins": ["IDH3B", "PCK1"],
"Disease related genes": ["ABHD12", "ADA", "ADAM33", "ADNP", "AHCY", "ARFGEF2",
"ASXL1", "AVP", "BCAS4", "BFSP1", "CBFA2T2", "CD40", "CHD6", "CHMP4B", "CHRNA4",
 "COL9A3", "COX4I2", "CSNK2A1", "CST3", "CTSA", "CYP24A1", "DEFB126", "DNAJC5",
 "DNMT3B", "DPM1", "EDN3", "EEF1A2", "ELMO2", "EPB41L1", "FERMT1", "FLRT3",
 "GATA5", "GDF5", "GNAS", "GSS", "HCK", "HNF4A", "IDH3B", "IFT52", "ITCH",
 "ITPA", "JAG1", "JPH2", "KCNB1", "KCNQ2", "KIZ", "MAFB", "MCM8", "MGME1",
 "MKKS", "MMP9", "MYLK2", "NDUFAF5", "NOP56", "OSBPL2", "OVOL2", "PANK2",
 "PAX1", "PCK1", "PCNA", "PDYN", "PIGT", "PLCB1", "PLCB4", "POFUT1", "PRNP",
 "PROKR2", "PRPF6", "PTGIS", "RBCK1", "RIN2", "RSPO4", "RTEL1", "SALL4",
 "SAMHD1", "SEC23B", "SLC2A10", "SLC4A11", "SLC12A5", "SLC17A9", "SLC52A3",
 "SLX4IP", "SNAP25", "SNRPB", "SNTA1", "SOX18", "SRC", "STK4", "STX16",
 "SUN5", "TBC1D20", "TGM3", "TGM6", "THBD", "TOP1", "TUBB1", "VAPB",
 "VPS16", "VSX1", "ZNF335"], "Enzymes": ["ABHD12", "ACOT8", "ACSS1", "ACSS2",
 "ADA", "AHCY", "ATP9A", "AURKA", "BIRC7", "CDC25B", "CDS2", "CHD6", "CPXM1",
 "CRLS1", "CSNK2A1", "CTSA", "CTSZ", "CYP24A1", "DDX27", "DHX35", "DNMT3B",
 "DPM1", "DUSP15", "ENTPD6", "EYA2", "FKBP1A", "GGT7", "GPCPD1", "GSS", "HAO1",
 "HCK", "HM13", "IDH3B", "ITCH", "ITPA", "LPIN3", "MCM8", "MMP9", "MMP24",
 "MOCS3", "MYLK2", "NAA20", "NANP", "NCOA3", "NFS1", "NPEPL1", "PAK5", "PANK2",
 "PCK1", "PCSK2", "PLCB1", "PLCB4", "PLCG1", "POFUT1", "PSMA7", "PTGIS", "PTK6",
  "PTPN1", "PTPRA", "PTPRT", "PYGB", "RBCK1", "RNF114", "RTEL1", "SGK2", "SMOX",
   "SPO11", "SPTLC3", "SRC", "SRMS", "SRXN1", "STK4", "STK35", "TGM2", "TGM3",
   "TGM6", "TOP1", "TP53RK", "TRIB3", "UBE2C", "UBOX5", "UCKL1"],
   "FDA approved drug targets": ["ADA",
 "ADRA1D", "CHRNA4", "FKBP1A", "GSS", "HRH3", "KCNB1", "KCNQ2", "MMP9", "MMP24",
  "PTGIS", "SLC12A5", "SMOX", "SNAP25", "SRC", "TOP1", "TUBB1"],
  "G-protein coupled receptors": ["ADRA1D", "HRH3", "MC3R", "NPBWR2", "NTSR1",
  "OPRL1", "PROKR2", "SSTR4"], "NA": ["ATP5F1E", "C20orf203", "C20orf204",
  "MMP24OS", "RAB5IF", "RIPOR3", "RTF2", "SMIM26"], "Nuclear receptors":
  ["HNF4A"], "Plasma proteins": ["ABHD16B", "ACOT8", "ADA", "ADRA1D", "AHCY",
  "APMAP", "ARFGAP1", "ATRN", "AURKA", "BPIFA1", "BPIFB1", "BPIFB2", "BPIFB3",
  "CASS4", "CBLN4", "CCM2L", "CD93", "CDC25B", "CDH26", "CDS2", "CEP250",
  "CHD6", "CHGB", "CPNE1", "CRNKL1", "CSE1L", "CST1", "CST3", "CST5", "CST7",
  "CTSZ", "DHX35", "DIDO1", "DNTTIP1", "DPM1", "DSN1", "DSTN", "DYNLRB1",
  "E2F1", "EEF1A2", "EIF2S2", "EIF6", "EYA2", "FAM83C", "FKBP1A", "GDF5",
  "GSS", "HELZ2", "HM13", "HSPA12B", "ID1", "IDH3B", "JAG1", "KCNQ2", "KIF3B",
  "LAMA5", "LBP", "MAPRE1", "MATN4", "MCM8", "MMP9", "MRGBP", "MYLK2", "MYT1",
  "NCOA3", "NOP56", "NSFL1C", "OXT", "PAK5", "PANK2", "PCIF1", "PCNA", "PFDN4",
  "PHF20", "PI3", "PIGT", "PLCB1", "PLCG1", "PLTP", "PRNP", "PROCR", "PROKR2",
  "PRPF6", "PSMA7", "PTGIS", "PTPRA", "PYGB", "RAE1", "RALGAPB", "RALY",
  "RBCK1", "RBL1", "RBM39", "RPN2", "RPS21", "RRBP1", "RTEL1", "SAMHD1",
  "SCAND1", "SEC23B", "SEMG1", "SEMG2", "SIRPA", "SIRPB1", "SLA2", "SLC4A11",
  "SLC9A8", "SLC52A3", "SLPI", "SNRPB", "SNRPB2", "SOGA1", "SPO11", "SRC",
  "STAU1", "SULF2", "TGIF2", "TGM3", "TPD52L2", "TTPAL", "TUBB1", "UQCC1",
  "WISP2", "YWHAB", "ZHX3", "ZNF343", "ZNF512B", "ZNFX1"],
  "Potential drug targets": ["ABHD12", "AHCY", "CHD6", "COX4I2", "CSNK2A1",
  "CTSA", "CYP24A1", "DNMT3B", "DPM1", "HCK", "IDH3B", "ITCH", "ITPA", "MCM8",
  "MYLK2", "PANK2", "PCK1", "PDYN", "PLCB1", "PLCB4", "POFUT1", "PRNP",
  "PROKR2", "RBCK1", "RTEL1", "SLC2A10", "SLC4A11", "SLC17A9", "SLC52A3",
  "STK4", "TGM3", "TGM6", "VAPB"], "Predicted intracellular proteins":
  ["AAR2", "ABHD12", "ABHD16B", "ACOT8", "ACSS1", "ACSS2", "ACTR5", "ADA",
  "ADIG", "ADNP", "ADRM1", "AHCY", "ANKEF1", "AP5S1", "APCDD1L", "APMAP",
  "ARFGAP1", "ARFGEF2", "ARFRP1", "ARHGAP40", "ASXL1", "AURKA", "BANF2",
  "BCAS1", "BCAS4", "BCL2L1", "BFSP1", "BHLHE23", "BIRC7", "BLCAP", "BMP7",
  "BPI", "BTBD3", "C20orf27", "C20orf85", "C20orf96", "C20orf144", "C20orf173",
  "C20orf194", "C20orf196", "C20orf202", "CABLES2", "CASS4", "CBFA2T2",
  "CCM2L", "CDC25B", "CDH26", "CDK5RAP1", "CEBPB", "CENPB", "CEP250", "CFAP61",
  "CHD6", "CHGB", "CHMP4B", "CNBD2", "COL9A3", "COL20A1", "COMMD7", "CPNE1",
  "CRNKL1", "CSE1L", "CSNK2A1", "CSTF1", "CSTL1", "CTCFL", "CTNNBL1", "CTSA",
  "CYP24A1", "DBNDD2", "DDRGK1", "DDX27", "DHX35", "DIDO1", "DLGAP4", "DNMT3B",
  "DNTTIP1", "DOK5", "DPM1", "DSN1", "DSTN", "DTD1", "DUSP15", "DYNLRB1",
  "DZANK1", "E2F1", "EBF4", "EEF1A2", "EFCAB8", "EIF2S2", "EIF6", "ELMO2",
  "ENTPD6", "EPB41L1", "EPPIN", "ERGIC3", "ESF1", "EYA2", "FAM83C", "FAM83D",
  "FAM110A", "FAM210B", "FAM217B", "FASTKD5", "FERMT1", "FKBP1A", "FNDC11",
  "FOXA2", "FOXS1", "GATA5", "GCNT7", "GDAP1L1", "GDF5OS", "GGT7", "GGTLC1",
  "GID8", "GINS1", "GMEB2", "GNAS", "GPCPD1", "GSS", "GTSF1L", "GZF1",
  "HAO1", "HCK", "HELZ2", "HNF4A", "HSPA12B", "IDH3B", "IFT52", "INSM1",
  "ITCH", "ITPA", "JAG1", "JPH2", "KAT14", "KCNB1", "KCNG1", "KCNQ2",
  "KIAA1755", "KIF3B", "KIF16B", "KIZ", "L3MBTL1", "LAMA5", "LKAAEAR1",
  "LPIN3", "LSM14B", "LZTS3", "MACROD2", "MAFB", "MAP1LC3A", "MAPRE1",
  "MCM8", "MGME1", "MKKS", "MOCS3", "MRGBP", "MROH8", "MRPS26", "MTG2",
  "MTRNR2L3", "MYBL2", "MYH7B", "MYL9", "MYLK2", "MYT1", "NAA20", "NANP",
   "NAPB", "NCOA3", "NCOA5", "NCOA6", "NDRG3", "NDUFAF5", "NECAB3", "NELFCD",
   "NEURL2", "NFATC2", "NFS1", "NINL", "NKAIN4", "NKX2-2", "NKX2-4", "NOL4L",
   "NOP56", "NPEPL1", "NRSN2", "NSFL1C", "NXT1", "OGFR", "OSBPL2", "OSER1",
   "OVOL2", "PABPC1L", "PAK5", "PANK2", "PARD6B", "PAX1", "PCED1A", "PCIF1",
   "PCK1", "PCMTD2", "PCNA", "PCSK2", "PDRG1", "PFDN4", "PHACTR3", "PHF20",
   "PIGT", "PKIG", "PLAGL2", "PLCB1", "PLCB4", "PLCG1", "PLTP", "PMEPA1",
   "POLR3F", "PPDPF", "PPP1R3D", "PPP1R16B", "PRELID3B", "PREX1", "PROCR",
   "PRPF6", "PSMA7", "PSMF1", "PTK6", "PTPRT", "PXMP4", "PYGB", "RAB22A",
   "RAD21L1", "RAE1", "RALGAPA2", "RALGAPB", "RALY", "RASSF2", "RBBP8NL",
   "RBBP9", "RBCK1", "RBL1", "RBM12", "RBM38", "RBM39", "RBPJL", "REM1",
   "RGS19", "RIMS4", "RIN2", "RNF114", "ROMO1", "RPN2", "RPRD1B", "RPS21",
   "RRBP1", "RTEL1", "SALL4", "SAMD10", "SAMHD1", "SCAND1", "SCP2D1", "SCRT2",
   "SDCBP2", "SEC23B", "SEL1L2", "SGK2", "SIGLEC1", "SIRPB1", "SIRPD", "SLA2",
   "SLC2A4RG", "SLC2A10", "SLC4A11", "SLC12A5", "SLX4IP", "SMOX", "SNAI1",
   "SNAP25", "SNRPB", "SNRPB2", "SNTA1", "SNX5", "SNX21", "SOGA1", "SOX12",
   "SOX18", "SPAG4", "SPATA2", "SPATA25", "SPEF1", "SPO11", "SPTLC3", "SRC",
   "SRMS", "SRSF6", "SRXN1", "SS18L1", "STAU1", "STK4", "STK35", "STMN3",
   "STX16", "SULF2", "SUN5", "SYCP2", "TAF4", "TASP1", "TCEA2", "TCF15",
   "TCFL5", "TFAP2C", "TGIF2", "TGM2", "TGM3", "TGM6", "TLDC2", "TNNC2",
   "TOMM34", "TOP1", "TOX2", "TP53INP2", "TP53RK", "TP53TG5", "TPD52L2",
   "TPX2", "TRIB3", "TRMT6", "TRPC4AP", "TSHZ2", "TTI1", "TTPAL", "TUBB1",
   "UBE2C", "UBE2V1", "UBOX5", "UCKL1", "UQCC1", "VAPB", "VPS16", "VSX1",
   "WFDC2", "WFDC3", "WFDC9", "WFDC10B", "XRN2", "YTHDF1", "YWHAB", "ZBP1",
   "ZBTB46", "ZCCHC3", "ZFP64", "ZGPAT", "ZHX3", "ZMYND8", "ZNF133", "ZNF217",
   "ZNF334", "ZNF335", "ZNF337", "ZNF341", "ZNF343", "ZNF512B", "ZNF831",
   "ZNFX1", "ZSWIM1", "ZSWIM3"], "Predicted membrane proteins": ["ABHD12",
   "ACSS1", "ACSS2", "ADAM33", "ADIG", "ADRA1D", "AP5S1", "APCDD1L", "APMAP",
   "ATP9A", "ATRN", "BCL2L1", "BPI", "C20orf141", "CABLES2", "CD40", "CD93",
   "CDH4", "CDH22", "CDH26", "CDS2", "CFAP61", "CHRNA4", "COX4I2", "CRLS1",
   "CTCFL", "DNAJC5", "ENTPD6", "ERGIC3", "FAM209A", "FAM209B", "FAM210B",
   "FITM2", "FKBP1A", "FLRT3", "GDAP1L1", "GGT7", "HM13", "HRH3", "JAG1",
   "JPH2", "KCNB1", "KCNG1", "KCNK15", "KCNQ2", "KCNS1", "LAMP5", "LRRN4",
   "MANBAL", "MAVS", "MC3R", "MKKS", "MMP24", "NKAIN4", "NNAT", "NPBWR2",
   "NRSN2", "NTSR1", "OCSTAMP", "OPRL1", "PIGT", "PIGU", "PMEPA1", "PRND",
   "PRNP", "PROCR", "PROKR2", "PTGIS", "PTPN1", "PTPRA", "PTPRT", "PXMP4",
   "RALGAPA2", "RBL1", "RNF24", "RPN2", "RRBP1", "SDC4", "SEL1L2", "SERINC3",
   "SIGLEC1", "SIRPA", "SIRPB1", "SIRPB2", "SIRPG", "SLC2A10", "SLC4A11",
   "SLC9A8", "SLC12A5", "SLC13A3", "SLC17A9", "SLC23A2", "SLC24A3", "SLC32A1",
   "SLC35C2", "SLC52A3", "SLCO4A1", "SNPH", "SPAG4", "SPTLC3", "SSTR4", "STX16",
   "SUN5", "SYNDIG1", "SYS1", "TBC1D20", "THBD", "TM9SF4", "TMC2", "TMEM74B",
   "TMEM189", "TMEM230", "TMEM239", "TMX4", "UQCC1", "VAPB", "XKR7"],
   "Predicted secreted proteins": ["ACTL10", "ADAM33", "ADIG", "ANGPT4",
   "ANKRD60", "ASIP", "AVP", "B4GALT5", "BMP2", "BMP7", "BPI", "BPIFA1",
   "BPIFA2", "BPIFA3", "BPIFB1", "BPIFB2", "BPIFB3", "BPIFB4",
   "BPIFB6", "CBLN4", "CD40", "CHGB", "COL9A3", "COL20A1", "CPXM1", "CST1",
   "CST2", "CST3", "CST4", "CST5", "CST7", "CST8", "CST9", "CST9L", "CST11",
   "CSTL1", "CTSA", "CTSZ", "DEFB115", "DEFB116", "DEFB118", "DEFB119",
   "DEFB121", "DEFB123", "DEFB124", "DEFB125", "DEFB126", "DEFB127",
   "DEFB128", "DEFB129", "DEFB132", "EDEM2", "EDN3", "EMILIN3", "EPPIN",
   "GCNT7", "GDF5", "GFRA4", "GHRH", "GNAS", "GNRH2", "ID1", "ISM1", "LAMA5",
   "LBP", "LIME1", "MATN4", "MMP9", "NECAB3", "OTOR", "OXT", "PCSK2", "PDYN",
   "PET117", "PI3", "PIGT", "PLTP", "PMEPA1", "POFUT1", "PRNP",
   "PTPRA", "R3HDML", "RPN2", "RSPO4", "SEMG1", "SEMG2", "SIRPB1", "SIRPD",
   "SLPI", "SPINT3", "SPINT4", "SULF2", "TNFRSF6B", "VSTM2L", "WFDC2", "WFDC3",
   "WFDC5", "WFDC6", "WFDC8", "WFDC10A", "WFDC10B", "WFDC11", "WFDC12",
   "WFDC13", "WISP2"], "RAS pathway related proteins": ["ANGPT4",
   "BCL2L1", "PAK5", "PLCG1", "STK4"], "RNA polymerase related proteins":
   ["POLR3F"], "Ribosomal proteins": ["MRPS26", "RPS21"],
   "Transcription factors": ["ADNP", "BHLHE23", "CEBPB", "CTCFL", "DNMT3B",
   "E2F1", "EBF4", "FOXA2", "FOXS1", "GATA5", "GMEB2", "GZF1", "HNF4A", "ID1",
   "INSM1", "L3MBTL1", "MAFB", "MYBL2", "MYT1", "NCOA3", "NFATC2", "NKX2-2",
   "NKX2-4", "OVOL2", "PAX1", "PLAGL2", "RBPJL", "SALL4", "SCRT2", "SNAI1",
   "SOX12", "SOX18", "TCF15", "TCFL5", "TFAP2C", "TGIF2", "TOX2", "TSHZ2",
   "VSX1", "ZBTB46", "ZFP64", "ZGPAT", "ZHX3", "ZNF133", "ZNF217", "ZNF334",
   "ZNF335", "ZNF337", "ZNF341", "ZNF343", "ZNF512B", "ZNFX1"],
   "Transporters": ["ATP9A", "BCL2L1", "BPI", "BPIFB2", "CHRNA4", "COX4I2",
   "CSE1L", "KCNB1", "KCNK15", "KCNQ2", "KCNS1", "LBP", "NPBWR2", "NRSN2",
   "NTSR1", "OCSTAMP", "PDYN", "PLTP", "PRND", "PRNP", "PXMP4", "RAE1",
   "ROMO1", "SDC4", "SERINC3", "SLC2A10", "SLC4A11", "SLC9A8", "SLC12A5",
   "SLC13A3", "SLC17A9", "SLC23A2", "SLC24A3", "SLC32A1", "SLC35C2",
   "SLC52A3", "SLCO4A1", "SNAP25", "TM9SF4", "VAPB"],
   "Voltage-gated ion channels": ["KCNB1", "KCNG1", "KCNK15", "KCNQ2",
   "KCNS1"]},lst)

#draws the graph.
example.draw_graph()
