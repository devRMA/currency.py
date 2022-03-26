from enum import Enum
from typing import Literal, TypeAlias

# Data taken from https://economia.awesomeapi.com.br/json/available/uniq

# Type alias used for typing the parameters
TCurrency: TypeAlias = Literal[
    'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AZN', 'BAM', 'BBD',
    'BDT', 'BGN', 'BHD', 'BIF', 'BND', 'BOB', 'BRL', 'BRLT', 'BSD', 'BTC',
    'BWP', 'BYN', 'BZD', 'CAD', 'CHF', 'CLP', 'CNH', 'CNY', 'COP', 'CRC', 'CUP',
    'CVE', 'CZK', 'DJF', 'DKK', 'DOGE', 'DOP', 'DZD', 'EGP', 'ETB', 'ETH',
    'EUR', 'FJD', 'GBP', 'GEL', 'GHS', 'GMD', 'GNF', 'GTQ', 'HKD', 'HNL', 'HRK',
    'HTG', 'HUF', 'IDR', 'ILS', 'INR', 'IQD', 'IRR', 'ISK', 'JMD', 'JOD', 'JPY',
    'KES', 'KGS', 'KHR', 'KMF', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR',
    'LSL', 'LTC', 'LYD', 'MAD', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO',
    'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR',
    'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON',
    'RSD', 'RUB', 'RWF', 'SAR', 'SCR', 'SDG', 'SDR', 'SEK', 'SGD', 'SOS', 'STD',
    'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TRY', 'TTD', 'TWD', 'TZS',
    'UAH', 'UGX', 'USD', 'USDT', 'UYU', 'UZS', 'VEF', 'VND', 'VUV', 'XAF',
    'XAGG', 'XBR', 'XCD', 'XOF', 'XPF', 'XRP', 'YER', 'ZAR', 'ZMK', 'ZWL']


class CurrencyEnum(Enum):
    """
    Enum of currencies
    """
    AED = 'Dirham dos Emirados'
    AFN = 'Afghani do Afeganistão'
    ALL = 'Lek Albanês'
    AMD = 'Dram Armênio'
    ANG = 'Guilder das Antilhas'
    AOA = 'Kwanza Angolano'
    ARS = 'Peso Argentino'
    AUD = 'Dólar Australiano'
    AZN = 'Manat Azeri'
    BAM = 'Marco Conversível'
    BBD = 'Dólar de Barbados'
    BDT = 'Taka de Bangladesh'
    BGN = 'Lev Búlgaro'
    BHD = 'Dinar do Bahrein'
    BIF = 'Franco Burundinense'
    BND = 'Dólar de Brunei'
    BOB = 'Boliviano'
    BRL = 'Real Brasileiro'
    BRLT = 'Real Brasileiro Turismo'
    BSD = 'Dólar das Bahamas'
    BTC = 'Bitcoin'
    BWP = 'Pula de Botswana'
    BYN = 'Rublo Bielorrusso'
    BZD = 'Dólar de Belize'
    CAD = 'Dólar Canadense'
    CHF = 'Franco Suíço'
    CHFRTS = 'Franco Suíço'
    CLP = 'Peso Chileno'
    CNH = 'Yuan chinês offshore'
    CNY = 'Yuan Chinês'
    COP = 'Peso Colombiano'
    CRC = 'Colón Costarriquenho'
    CUP = 'Peso Cubano'
    CVE = 'Escudo cabo-verdiano'
    CZK = 'Coroa Checa'
    DJF = 'Franco do Djubouti'
    DKK = 'Coroa Dinamarquesa'
    DOGE = 'Dogecoin'
    DOP = 'Peso Dominicano'
    DZD = 'Dinar Argelino'
    EGP = 'Libra Egípcia'
    ETB = 'Birr Etíope'
    ETH = 'Ethereum'
    EUR = 'Euro'
    FJD = 'Dólar de Fiji'
    GBP = 'Libra Esterlina'
    GEL = 'Lari Georgiano'
    GHS = 'Cedi Ganês'
    GMD = 'Dalasi da Gâmbia'
    GNF = 'Franco de Guiné'
    GTQ = 'Quetzal Guatemalteco'
    HKD = 'Dólar de Hong Kong'
    HNL = 'Lempira Hondurenha'
    HRK = 'Kuna Croata'
    HTG = 'Gourde Haitiano'
    HUF = 'Florim Húngaro'
    IDR = 'Rupia Indonésia'
    ILS = 'Novo Shekel Israelense'
    INR = 'Rúpia Indiana'
    IQD = 'Dinar Iraquiano'
    IRR = 'Rial Iraniano'
    ISK = 'Coroa Islandesa'
    JMD = 'Dólar Jamaicano'
    JOD = 'Dinar Jordaniano'
    JPY = 'Iene Japonês'
    JPYRTS = 'Iene Japonês'
    KES = 'Shilling Queniano'
    KGS = 'Som Quirguistanês'
    KHR = 'Riel Cambojano'
    KMF = 'Franco Comorense'
    KRW = 'Won Sul-Coreano'
    KWD = 'Dinar Kuwaitiano'
    KYD = 'Dólar das Ilhas Cayman'
    KZT = 'Tengue Cazaquistanês'
    LAK = 'Kip Laosiano'
    LBP = 'Libra Libanesa'
    LKR = 'Rúpia de Sri Lanka'
    LSL = 'Loti do Lesoto'
    LTC = 'Litecoin'
    LYD = 'Dinar Líbio'
    MAD = 'Dirham Marroquino'
    MDL = 'Leu Moldavo'
    MGA = 'Ariary Madagascarense'
    MKD = 'Denar Macedônio'
    MMK = 'Kyat de Mianmar'
    MNT = 'Mongolian Tugrik'
    MOP = 'Pataca de Macau'
    MRO = 'Ouguiya Mauritana'
    MUR = 'Rúpia Mauriciana'
    MVR = 'Rufiyaa Maldiva'
    MWK = 'Kwacha Malauiana'
    MXN = 'Peso Mexicano'
    MYR = 'Ringgit Malaio'
    MZN = 'Metical de Moçambique'
    NAD = 'Dólar Namíbio'
    NGN = 'Naira Nigeriana'
    NGNI = 'Naira Nigeriana'
    NGNPARALLEL = 'Naira Nigeriana'
    NIO = 'Córdoba Nicaraguense'
    NOK = 'Coroa Norueguesa'
    NPR = 'Rúpia Nepalesa'
    NZD = 'Dólar Neozelandês'
    OMR = 'Rial Omanense'
    PAB = 'Balboa Panamenho'
    PEN = 'Sol do Peru'
    PGK = 'Kina Papua-Nova Guiné'
    PHP = 'Peso Filipino'
    PKR = 'Rúpia Paquistanesa'
    PLN = 'Zlóti Polonês'
    PYG = 'Guarani Paraguaio'
    QAR = 'Rial Catarense'
    RON = 'Leu Romeno'
    RSD = 'Dinar Sérvio'
    RUB = 'Rublo Russo'
    RUBTOD = 'Rublo Russo'
    RUBTOM = 'Rublo Russo'
    RWF = 'Franco Ruandês'
    SAR = 'Riyal Saudita'
    SCR = 'Rúpias de Seicheles'
    SDG = 'Libra Sudanesa'
    SDR = 'DSE'
    SEK = 'Coroa Sueca'
    SGD = 'Dólar de Cingapura'
    SOS = 'Shilling Somaliano'
    STD = 'Dobra São Tomé/Príncipe'
    SVC = 'Colon de El Salvador'
    SYP = 'Libra Síria'
    SZL = 'Lilangeni Suazilandês'
    THB = 'Baht Tailandês'
    TJS = 'Somoni do Tajiquistão'
    TMT = 'TMT'
    TND = 'Dinar Tunisiano'
    TRY = 'Nova Lira Turca'
    TTD = 'Dólar de Trinidad'
    TWD = 'Dólar Taiuanês'
    TZS = 'Shilling Tanzaniano'
    UAH = 'Hryvinia Ucraniana'
    UGX = 'Shilling Ugandês'
    USD = 'Dólar Americano'
    USDT = 'Dólar Americano Turismo'
    UYU = 'Peso Uruguaio'
    UZS = 'Som Uzbequistanês'
    VEF = 'Bolívar Venezuelano'
    VND = 'Dong Vietnamita'
    VUV = 'Vatu de Vanuatu'
    XAF = 'Franco CFA Central'
    XAGG = 'XPrata'
    XBR = 'Brent Spot'
    XCD = 'Dólar do Caribe Oriental'
    XOF = 'Franco CFA Ocidental'
    XPF = 'Franco CFP'
    XRP = 'XRP'
    YER = 'Riyal Iemenita'
    ZAR = 'Rand Sul-Africano'
    ZMK = 'Kwacha Zambiana'
    ZWL = 'Dólar Zimbabuense'
