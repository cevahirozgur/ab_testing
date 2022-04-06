########################  AB Testi ile Bidding Yöntemlerinin Dönüşümünün Karşılaştırılması  #####################
#İş Problemi
# Facebook kısa süre önce mevcut "maximumbidding" adı verilen teklif verme türüne alternatif olarak
# yeni bir teklif türü olan "average bidding"’i tanıttı.

#Müşterilerimizden biri olan bombabomba.com, bu yeni özelliği test etmeye karar verdi
# ve average bidding'in maximumbidding'den daha fazla dönüşüm getirip getirmediğini
# anlamak için bir A/B testi yapmak istiyor.

# A/B testi 1 aydır devam ediyor ve bombabomba.com şimdi sizden bu A/B testinin sonuçlarını analiz etmenizi bekliyor.
# Bombabomba.com için nihai başarı ölçütü Purchase'dır. Bu nedenle, istatistiksel testler için
# Purchase metriğine odaklanılmalıdır.

#Veri Seti Hikayesi
#Bir firmanın web site bilgilerini içeren bu veri setinde kullanıcıların gördükleri ve tıkladıkları reklam sayıları
# gibi bilgilerin yanı sıra buradan gelen kazanç bilgileri yer almaktadır.
# Kontrol ve Test grubu olmak üzere iki ayrı veri seti vardır.
# Bu veri setleri ab_testing.xlsx excel’inin ayrı sayfalarında yer almaktadır.
# Kontrol grubuna Maximum Bidding, test grubuna Average Bidding uygulanmıştır.

# Impression Reklam görüntüleme sayısı
# Click: Görüntülenen reklama tıklama sayısı
# Purchase: Tıklanan reklamlar sonrası satın alınan ürün sayısı
# Earning: Satın alınan ürünler sonrası elde edilen kazanç

#################################### Görev 1: Veriyi Hazırlama ve Analiz Etme ####################################

#Adım 1: ab_testing_data.xlsx adlı kontrol ve test grubu verilerinden oluşan veri setini okutunuz.
#Kontrol ve test grubu verilerini ayrı değişkenlere atayınız.

# import os
# print("Current working directory: {0}".format(os.getcwd()))
# os.chdir("D:\yazilim/VBO")

import itertools
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, \
    pearsonr, spearmanr, kendalltau, f_oneway, kruskal
import statsmodels.stats.proportion as proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

control = pd.read_excel("ab_testing.xlsx", sheet_name="Control Group")
test = pd.read_excel("ab_testing.xlsx", sheet_name="Test Group")

#Adım 2: Kontrol ve test grubu verilerini analiz ediniz.

control.describe()
test.describe()

#Adım 3: Analiz işleminden sonra concat metodunu kullanarak kontrol ve test grubu verilerini birleştiriniz.

df = pd.concat([control, test], ignore_index=True)
df.head()
###############################  Görev 2: A/B Testinin Hipotezinin Tanımlanması  ############################

#Adım 1: Hipotezi tanımlayınız.

# H0 : M1 = M2  ( control ve test Purchase ort. arasında anlamlı bir fark yoktur)
# H1 : M1!= M2  (....vardır)

# Adım 2: Kontrol ve test grubu için purchase (kazanç) ortalamalarını analiz ediniz.
control.head()
control["Purchase"].mean()
test["Purchase"].mean()

#############################  Görev 3: Hipotez Testinin Gerçekleştirilmesi  #################################


control["Purchase"].mean()
test["Purchase"].mean()

#Adım 1: Hipotez testi yapılmadan önce varsayım kontrollerini yapınız.
#Adım 2: Normallik Varsayımı ve Varyans Homojenliği sonuçlarına göre uygun testi seçiniz.


#Normallik Varsayımı

test_stat, pvalue = shapiro(test["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

                                # p-value > 0.05 H0 Reddedilemez
                                # Normallik sağlanıyor

test_stat, pvalue = shapiro(control["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

                                # p-value > 0.05 H0 Reddedilemez
                                # Normallik sağlanıyor

# Varyans Homojenliği

test_stat, pvalue = levene(test["Purchase"],
                           control["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))             # p-value > 0.05
                                                                             # Var. Hom. Sağlanır


#Adım 3: Test sonucunda elde edilen p_value değerini göz önünde bulundurarak kontrol ve test grubu satın alma
# ortalamaları arasında istatistiki olarak anlamlı bir fark olup olmadığını yorumlayınız.

test_stat, pvalue = ttest_ind(test["Purchase"],
                              control["Purchase"], equal_var=True)
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))

                        # p-value > 0.05 H0 Reddedilemez (ort arasında ist bir fark yoktur)


################################  Görev 4: Sonuçların Analizi  ########################################

#Adım 1: Hangi testi kullandınız, sebeplerini belirtiniz.

#Ortalamalar kıyaslandığından varsayımlar sağlanıyorsa T testi, sağlanmıyorsa mannwhitneyu testi yapmalıydım.
#Varsayımlar sağlandığı için T testi kullandım.

#Adım 2: Elde ettiğiniz test sonuçlarına göre müşteriye tavsiyede bulununuz.

# Test sonuçlarına göre "maximumbidding" adı verilen teklif verme türü ile yeni alternatifimiz olan
# "average bidding" 'in getirdiği ort kazançlar arasında istatistiki olarak anlamlı bir farklılık yoktur.
# Yaptığımız testler sonucu average bidding'inmaximumbidding'den
# daha fazla dönüşüm getirip getirmediği tespit edilmiştir.
# Bu durumda teklif verme sisteminde bu yeniliğe ihtiyaç yoktur.

