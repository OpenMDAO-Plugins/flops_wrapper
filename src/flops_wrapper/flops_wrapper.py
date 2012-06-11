"""
OpenMDAO Wrapper for Flops
Automatically generated from flops.scriptWrapper with parse_phoenixwrapper.

This wrapper is based on the ModelCenter Java wrapper, version 2.00 Beta
"""

# pylint: disable-msg=E0611,F0401,E1101
from numpy import int64 as numpy_int64
from numpy import float64 as numpy_float64
from numpy import str as numpy_str
from numpy import zeros, array

from openmdao.util.filewrap import FileParser
from openmdao.util.namelist_util import Namelist

from openmdao.main.api import VariableTree, FileMetadata
from openmdao.lib.datatypes.api import Str, Bool, Int, Array, Enum, Float, \
                                       File, List, Slot
from openmdao.lib.components.api import ExternalCode

# pylint: disable-msg=C0301,C0324,C0103,R0903

class FlopsWrapper_output_Weight_Wing(VariableTree):
    """Container for output.Weight.Wing"""

    # OpenMDAO Public Variables
    w = Float(0.0, desc='Bending material factor. For detailed wing definition, this factor is calculated by numerical integration along the specified load path to determine the amount of bending material required to support an elliptical load distribution.  The wing is treated as an idealized beam with dimensions proportional to the wing local chord and thickness. The bending factor is modified for aeroelastic penalties (flutter, divergence, and aeroelastic loads) depending on wing sweep (including forward), aspect ratio, degree of aeroelastic tailoring, and strut bracing, if any.  These modifications are based on a curve fit of the results of a study performed using the Aeroelastic Tailoring and Structural Optimization (ATSO) code to structurally optimize a large matrix of wings.\n\nIf the detailed wing definition is not used, an equivalent bending factor is computed assuming a trapezoidal wing with constant t/c.')
    ew = Float(0.0, desc='Engine inertia relief factor.')
    w1 = Float(0.0, desc='The first term in the wing weight is the bending factor. It is adjusted for inertia relief for the wing itself and for any engines on the wing.')
    w2 = Float(0.0, desc='The second term represents control surfaces and shear material.  According to structural and statistical studies conducted during weight module development, the weight of spars and ribs depends almost entirely on control surfaces.  The amount of shear material required to carry structural loads is not critical.')
    w3 = Float(0.0, desc='The third term depends entirely on wing area and covers multitude of miscellaneous items.')


class FlopsWrapper_output_Weight_Inertia(VariableTree):
    """Container for output.Weight.Inertia"""

    # OpenMDAO Public Variables
    cgx = Array(dtype=numpy_float64)
    cgy = Array(dtype=numpy_float64)
    cgz = Array(dtype=numpy_float64)
    ixxroll = Array(dtype=numpy_float64)
    ixxptch = Array(dtype=numpy_float64)
    ixxyaw = Array(dtype=numpy_float64)
    ixz = Array(dtype=numpy_float64)


class FlopsWrapper_output_Weight(VariableTree):
    """Container for output.Weight"""

    # OpenMDAO Public Variables
    dowe = Float(0.0)
    paylod = Float(0.0)
    fuel = Float(0.0)
    rampwt = Float(0.0)
    wsr = Float(0.0)
    thrso = Float(0.0)
    esf = Float(0.0)
    twr = Float(0.0)
    wldg = Float(0.0)
    fultot = Float(0.0)
    exsful = Float(0.0)
    frwi = Float(0.0)
    frht = Float(0.0)
    frvt = Float(0.0)
    frfin = Float(0.0)
    frcan = Float(0.0)
    frfu = Float(0.0)
    wlg = Float(0.0)
    frna = Float(0.0)
    wengt = Float(0.0)
    wthr = Float(0.0)
    wpmisc = Float(0.0)
    wfsys = Float(0.0)
    frsc = Float(0.0)
    wapu = Float(0.0)
    win = Float(0.0)
    whyd = Float(0.0)
    welec = Float(0.0)
    wavonc = Float(0.0)
    wfurn = Float(0.0)
    wac = Float(0.0)
    wai = Float(0.0)
    wempty = Float(0.0)
    wflcrbw = Float(0.0)
    wwstuab = Float(0.0)
    wuf = Float(0.0)
    woil = Float(0.0)
    wsrv = Float(0.0)
    zfw = Float(0.0)
    wbomb = Float(0.0)
    
    def __init__(self, *args, **kwargs):
        """Constructor for the FlopsWrapper_output_Weight component"""

        super(FlopsWrapper_output_Weight, self).__init__(*args, **kwargs)

        # VariableTrees
        self.add('Inertia',  FlopsWrapper_output_Weight_Inertia())
        self.add('Wing',  FlopsWrapper_output_Weight_Wing())


class FlopsWrapper_output_Plot_Files(VariableTree):
    """Container for output.Plot_Files"""

    # OpenMDAO Public Variables
    # TODO - Do we really need to read these in every time? Let's not for now.
    #cnfile = File(iotype='out', path='Insert_Filename_Here', desc='Contour or thumbprint plot data file')
    #msfile = File(iotype='out', path='Insert_Filename_Here', desc='Mission summary data file')
    #crfile = File(iotype='out', path='Insert_Filename_Here', desc='Cruise schedule summary data file')
    #tofile = File(iotype='out', path='Insert_Filename_Here', desc='Takeoff and landing aerodynamic and thrust data file')
    #nofile = File(iotype='out', path='Insert_Filename_Here', desc='Takeoff and climb profile data file')
    #apfile = File(iotype='out', path='Insert_Filename_Here', desc='Drag polar plot data file')
    #thfile = File(iotype='out', path='Insert_Filename_Here', desc='Engine plot data file name')
    #hsfile = File(iotype='out', path='Insert_Filename_Here', desc='Design history plot file')
    #psfile = File(iotype='out', path='Insert_Filename_Here', desc='Excess power and load factor plot data file')


class FlopsWrapper_output_Performance_Segments(VariableTree):
    """Container for output.Performance.Segments"""

    # OpenMDAO Public Variables
    segment = Array(dtype=numpy_str)
    weights = Array(dtype=numpy_float64)
    alts = Array(dtype=numpy_float64)
    machs = Array(dtype=numpy_float64)
    thrusts = Array(dtype=numpy_float64)
    totmaxs = Array(dtype=numpy_float64)
    lods = Array(dtype=numpy_float64)
    sfcs = Array(dtype=numpy_float64)
    engparms = Array(dtype=numpy_float64)
    weighte = Array(dtype=numpy_float64)
    alte = Array(dtype=numpy_float64)
    mache = Array(dtype=numpy_float64)
    thruste = Array(dtype=numpy_float64)
    totmaxe = Array(dtype=numpy_float64)
    lode = Array(dtype=numpy_float64)
    sfce = Array(dtype=numpy_float64)
    engparme = Array(dtype=numpy_float64)


class FlopsWrapper_output_Performance_Constraints(VariableTree):
    """Container for output.Performance.Constraints"""

    # OpenMDAO Public Variables
    constraint = Array(dtype=numpy_str)
    value = Array(dtype=numpy_float64)
    units = Array(dtype=numpy_str)
    limit = Array(dtype=numpy_float64)
    weight = Array(dtype=numpy_float64)
    mach = Array(dtype=numpy_float64)
    alt = Array(dtype=numpy_float64)
    g = Array(dtype=numpy_float64)
    location = Array(dtype=numpy_str)


class FlopsWrapper_output_Performance(VariableTree):
    """Container for output.Performance"""

    # OpenMDAO Public Variables
    fuel = Float(0.0)
    range = Float(0.0)
    vapp = Float(0.0)
    taxofl = Float(0.0)
    faroff = Float(0.0)
    farldg = Float(0.0)
    amfor = Float(0.0)
    ssfor = Float(0.0)
    esf = Float(0.0)
    thrso = Float(0.0)
    vmmo = Float(0.0)

    def __init__(self, *args, **kwargs):
        """Constructor for the FlopsWrapper_output_Performance component"""

        super(FlopsWrapper_output_Performance, self).__init__(*args, **kwargs)

        # VariableTrees
        self.add('Constraints',  FlopsWrapper_output_Performance_Constraints())
        self.add('Segments',  FlopsWrapper_output_Performance_Segments())


class FlopsWrapper_output_Payload(VariableTree):
    """Container for output.Payload"""

    # OpenMDAO Public Variables
    npf = Int(0)
    npb = Int(0)
    npt = Int(0)
    nstu = Int(0)
    ngalc = Int(0)
    nflcr = Int(0)
    nstuag = Int(0)
    wppass = Float(0.0)
    bpp = Float(0.0)
    cargow = Float(0.0)
    cargof = Float(0.0)
    wcon = Float(0.0)


class FlopsWrapper_output_Noise(VariableTree):
    """Container for output.Noise"""

    # OpenMDAO Public Variables
    #nsplot = File(iotype='out', path='nsplot.out', msg='Noise output file')


class FlopsWrapper_output_Geometry_BWB(VariableTree):
    """Container for output.Geometry.BWB"""

    # OpenMDAO Public Variables
    xlp = Float(0.0, units='ft', desc='Length of centerline')
    xlw = Float(0.0, units='ft', desc='Length of side wall')
    wf = Float(0.0, units='ft', desc='Width of cabin')
    acabin = Float(0.0, units='ft*ft', desc='Cabin area')
    nbaw = Int(0, desc='Number of bays')
    bayw = Float(0.0, units='ft', desc='Width of bay')
    nlava = Int(0, desc='NUMBER OF LAVATORIES')
    ngally = Int(0, desc='Number of galleys')
    nclset = Int(0, desc='Number of closets')
    xl = Float(0.0, units='ft', desc='Total fuselage length')
    df = Float(0.0, units='ft', desc='Fuselage maximum depth')


class FlopsWrapper_output_Geometry(VariableTree):
    """Container for output.Geometry"""

    # OpenMDAO Public Variables
    xl = Float(0.0)
    wf = Float(0.0)
    df = Float(0.0)
    xlp = Float(0.0)
    ar = Float(0.0)
    sw = Float(0.0)
    tr = Float(0.0)
    sweep = Float(0.0)
    tca = Float(0.0)
    span = Float(0.0)
    glov = Float(0.0)
    sht = Float(0.0)
    svt = Float(0.0)
    xnac = Float(0.0)
    dnac = Float(0.0)
    xmlg = Float(0.0)
    xnlg = Float(0.0)

    def __init__(self, *args, **kwargs):
        """Constructor for the FlopsWrapper_output_Geometry component"""

        super(FlopsWrapper_output_Geometry, self).__init__(*args, **kwargs)

        # VariableTrees
        self.add('BWB', FlopsWrapper_output_Geometry_BWB())


class FlopsWrapper_output_Engine(VariableTree):
    """Container for output.Engine"""

    # OpenMDAO Public Variables
    #ofile = File(iotype='out', path='ofile.out')
    #eofile = File(iotype='out', path='eofile.out')
    #anopp = File(iotype='out', path='anopp.out')
    #footpr = File(iotype='out', path='footpr.out')
    #pltfil = File(iotype='out', path='pltfil')


class FlopsWrapper_output_Econ(VariableTree):
    """Container for output.Econ"""

    # OpenMDAO Public Variables
    sl = Array(dtype=numpy_float64)
    blockt = Array(dtype=numpy_float64)
    blockf = Array(dtype=numpy_float64)
    blockNx = Array(dtype=numpy_float64)
    wpayl = Array(dtype=numpy_float64)
    wgross = Array(dtype=numpy_float64)
    range = Array(dtype=numpy_float64)
    vapp = Array(dtype=numpy_float64)
    faroff = Array(dtype=numpy_float64)
    farldg = Array(dtype=numpy_float64)
    amfor = Array(dtype=numpy_float64)
    ssfor = Array(dtype=numpy_float64)


class FlopsWrapper_output(VariableTree):
    """Container for output"""

    def __init__(self, *args, **kwargs):
        """Constructor for the FlopsWrapper_output component"""

        super(FlopsWrapper_output, self).__init__(*args, **kwargs)

        # VariableTrees
        self.add('Econ',  FlopsWrapper_output_Econ())
        self.add('Engine',  FlopsWrapper_output_Engine())
        self.add('Geometry',  FlopsWrapper_output_Geometry())
        self.add('Noise',  FlopsWrapper_output_Noise())
        self.add('Payload',  FlopsWrapper_output_Payload())
        self.add('Performance',  FlopsWrapper_output_Performance())
        self.add('Plot_Files',  FlopsWrapper_output_Plot_Files())
        self.add('Weight',  FlopsWrapper_output_Weight())


class FlopsWrapper_input_wtin_Wing_Data(VariableTree):
    """Container for input.wtin.Wing_Data"""

    # OpenMDAO Public Variables
    span = Float(0.0, units='ft', desc='Wing span (optional, see &CONFIN - SW and AR)')
    dih = Float(0.0, units='deg', desc='Wing dihedral (positive) or anhedral (negative) angle')
    flapr = Float(0.3330, desc='Flap ratio -- ratio of total movable wing surface area (flaps, elevators, spoilers, etc.) to wing area')
    glov = Float(0.0, units='ft*ft', desc='Total glove and bat area beyond theoretical wing')
    varswp = Float(0.0, desc='Fraction of wing variable sweep weight penalty = 0., Fixed-geometry wing = 1., Full variable-sweep wing')
    fcomp = Float(0.0, desc='Decimal fraction of amount of composites used in wing structure = 0., No composites = 1., Maximum use of composites, approximately equivalent to FRWI1=.6, FRWI2=.83, FRWI3=.7 (Not necessarily all composite) This only applies to the wing.  Use override parameters for other components such as FRHT=.75, FRVT=.75, FRFU=.82, FRLGN=.85, FRLGM=.85, FRNA=.8')
    faert = Float(0.0, desc='Decimal fraction of amount of aeroelastic tailoring used in design of wing = 0., No aeroelastic tailoring = 1., Maximum aeroelastic tailoring')
    fstrt = Float(0.0, desc='Wing strut-bracing factor = 0., No wing strut = 1., Full benefit from strut bracing')


class FlopsWrapper_input_wtin_Tails_Fins(VariableTree):
    """Container for input.wtin.Tails_Fins"""

    # OpenMDAO Public Variables
    sht = Float(0.0, units='ft*ft', desc='Horizontal tail theoretical area')
    swpht = Float(-100.0, units='deg', desc='Horizontal tail 25% chord sweep angle (Default = SWEEP, Namelist &CONFIN)')
    arht = Float(-100.0, desc='Horizontal tail theoretical aspect ratio (Default = AR/2, Namelist &CONFIN)')
    trht = Float(-100.0, desc='Horizontal tail theoretical taper ratio (Default = TR, Namelist &CONFIN)')
    tcht = Float(0.0, desc='Thickness-chord ratio for the horizontal tail (Default = TCA, Namelist &CONFIN)')
    hht = Float(-100.0, desc='Decimal fraction of vertical tail span where horizontal tail is mounted = 0. for body mounted (Default for transports with all engines on the wing and for fighters) = 1. for T tail (Default for transports with multiple engines on the fuselage)')
    nvert = Int(1, desc='Number of vertical tails')
    svt = Float(0.0, units='ft*ft', desc='Vertical tail theoretical area (per tail)')
    swpvt = Float(-100.0, units='deg', desc='Vertical tail sweep angle at 25% chord (Default = SWPHT)')
    arvt = Float(-100.0, desc='Vertical tail theoretical aspect ratio (Default = ARHT/2)')
    trvt = Float(-100.0, desc='Vertical tail theoretical taper ratio (Default = TRHT)')
    tcvt = Float(0.0, desc='Thickness-chord ratio for the vertical tail (Default = TCHT)')
    nfin = Int(0, desc='Number of fins')
    sfin = Float(0.0, units='ft*ft', desc='Vertical fin theoretical area')
    arfin = Float(-100.0, desc='Vertical fin theoretical aspect ratio')
    trfin = Float(-100.0, desc='Vertical fin theoretical taper ratio')
    swpfin = Float(-100.0, units='deg', desc='Vertical fin sweep angle at 25% chord')
    tcfin = Float(0.0, desc='Vertical fin thickness - chord ratio')
    scan = Float(0.0, units='ft*ft', desc='Canard theoretical area')
    swpcan = Float(-100.0, units='deg', desc='Canard sweep angle at 25% chord')
    arcan = Float(-100.0, desc='Canard theoretical aspect ratio')
    trcan = Float(-100.0, desc='Canard theoretical taper ratio')
    tccan = Float(0.0, desc='Canard thickness-chord ratio (Default = TCHT)')


class FlopsWrapper_input_wtin_Propulsion(VariableTree):
    """Container for input.wtin.Propulsion"""

    # OpenMDAO Public Variables
    new = Int(0, desc='Number of wing mounted engines')
    nef = Int(0, desc='Number of fuselage mounted engines')
    thrso = Float(0.0, units='lb', desc='Rated thrust of baseline engine as described in Engine Deck (Default = THRUST, see &CONFIN)')
    weng = Float(0.0, units='lb', desc='Weight of each baseline engine or bare engine if WINL and WNOZ (below) are supplied (Default = THRSO/5.5 for transports and THRSO/8 for fighters)')
    eexp = Float(1.15, desc='Engine weight scaling parameter\nW(Engine) = WENG*(THRUST/THRSO)**EEXP\nIf EEXP is less than 0.3,\nW(Engine) = WENG + (THRUST-THRSO)*EEXP')
    winl = Float(0.0, units='lb', desc='Inlet weight for baseline engine if not included in WENG above')
    einl = Float(1.0, desc='Inlet weight scaling exponent\nW(Inlet) = WINL*(THRUST/THRSO)**EINL')
    wnoz = Float(0.0, units='lb', desc='Nozzle weight for baseline engine if not included in WENG above')
    enoz = Float(1.0, desc='Nozzle weight scaling exponent\nW(Nozzle) = WNOZ*(THRUST/THRSO)**ENOZ')
    xnac = Float(0.0, units='ft', desc='Average length of baseline engine nacelles.  Scaled by SQRT(THRUST/THRSO)')
    dnac = Float(0.0, units='ft', desc='Average diameter of baseline engine nacelles.  Scaled by SQRT(THRUST/THRSO)')
    wpmisc = Float(0.0, desc='Additional miscellaneous propulsion system weight or fraction of engine weight if < 1.  This is added to the engine control and starter weight and may be overridden if WPMSC is input.')


class FlopsWrapper_input_wtin_Override(VariableTree):
    """Container for input.wtin.Override"""

    # OpenMDAO Public Variables
    frwi = Float(1.0, desc='Total wing weight - fixed weight overrides FRWI1, FRWI2, FRWI3, FRWI4 below, scale factor is cumulative \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component\n \n')
    frwi1 = Float(1.0, desc='First term in wing weight equation - loosely corresponds to bending material weight \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component\n')
    frwi2 = Float(1.0, desc='Second term in wing weight equation - loosely corresponds to control surfaces, spars and ribs \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component\n')
    frwi3 = Float(1.0, desc='Third term in wing weight equation - miscellaneous, just because it')
    frwi4 = Float(1.0, desc='Fourth term in wing weight equation - miscellaneous, just because it')
    frht = Float(1.0, desc='Horizontal tail weight \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    frvt = Float(1.0, desc='Vertical tail weight \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    frfin = Float(1.0, desc='Wing vertical fin weight \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    frcan = Float(1.0, desc='Canard weight \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    frfu = Float(1.0, desc='Fuselage weight \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    frlgn = Float(1.0, desc='Landing gear weight, nose \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    frlgm = Float(1.0, desc='Landing gear weight, main \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    frna = Float(1.0, desc='Total weight of nacelles and/or air induction system \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    wthr = Float(0.0, desc='Total weight of thrust reversers\n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    wpmsc = Float(1.0, desc='Weight of miscellaneous propulsion systems such as engine controls, starter and wiring \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    wfsys = Float(1.0, desc='Weight of fuel system \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    frsc = Float(1.0, desc='Surface controls weight \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    wapu = Float(1.0, desc='Auxiliary power unit weight \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    win = Float(1.0, desc='Instrument Group weight \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    whyd = Float(1.0, desc='Hydraulics Group weight \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    welec = Float(1.0, desc='Electrical Group weight \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    wavonc = Float(1.0, desc='Avionics Group weight \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    warm = Float(0.0, desc='Armament Group weight - includes thermal protection system or armor and fixed weapons\n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    wfurn = Float(1.0, desc='Furnishings Group weight \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    wac = Float(1.0, desc='Air Conditioning Group weight \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    wai = Float(1.0, desc='Transports: Anti-icing Group weight\n            Fighters:   Auxiliary gear \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    wuf = Float(1.0, desc='Weight of unusable fuel \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    woil = Float(1.0, desc='Engine oil weight \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    wsrv = Float(1.0, desc='Transports: Passenger service weight\n             Fighters: Ammunition and nonfixed weapons weight \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    wcon = Float(1.0, desc='Transports: Cargo and baggage container weight Fighters:   Miscellaneous operating items weight If < 0.5, as a fraction of Gross Weight \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    wauxt = Float(1.0, desc='Auxiliary fuel tank weight (Fighters only) \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    wflcrb = Float(1.0, desc='Total weight of flight crew and baggage\n           (Defaults:  Transports    - 225.*NFLCR\n           Fighters      - 215.*NFLCR\n           Carrier-based - 180.*NFLCR)\n           \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    wstuab = Float(1.0, desc='Total weight of cabin crew and baggage (Default = 155.*NSTU + 200.*NGALC) \n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')
    ewmarg = Float(0.0, desc='Empty weight margin (Special Option) - delta weight added to Weight Empty.  If abs(EWMARG) < 5., it is interpreted as a fraction of calculated Weight Empty.  May be positive or negative\n < 0., negative of starting weight which will be modified as appropriate during optimization or parametric variation\n \n = 0., no weight for that component\n \n > 0. but < 5., scale factor applied to internally computed weight\n \n > 5., actual fixed weight for component')


class FlopsWrapper_input_wtin_OEW_Calculations(VariableTree):
    """Container for input.wtin.OEW_Calculations."""

    # OpenMDAO Public Variables
    ispowe = Enum(0, (0,1), desc='= 0, Normal FLOPS weight equations will be used\n= 1, Special equation for Operating Weight Empty will be used:\n            \n            OWE = SPWTH*THRUST + SPWSW*SW + SPWGW*GW + SPWCON\n            \n            Structures group weights will be scaled to meet the calculated OWE.\n            \n            = 2, Use response surface for weights - available only in DOSS version', aliases=('Normal FLOPS', 'Special eqn for OEW'))
    spwth = Float(2.2344, units='lb/lb', desc='Multiplier for thrust/engine in special equation for Operating Weight Empty\nSPWTH = \n                                  AIRFLOWref\n(PODsclr + dOEWsclr) * ------------\n                               SLSTHRUSTref\n            ')
    spwsw = Float(9.5, units='psf', desc='Multiplier for wing area in special equation for Operating Weight Empty')
    spwgw = Float(0.104087, units='lb/lb', desc='Multiplier for gross weight in special equation for Operating Weight Empty\nSPWGW = \n            MTOWsclr+OEWgrwth*MTOWgrwth\n        -----------------------------------\n            1. + MTOWgrowth\n\n')
    spwcon = Float(38584.0, units='lb', desc='Constant weight term in special equation for Operating Weight Empty\n            \nSPWCON = OEWuncycled\n            - MTOWscalar*MTOWuncycled\n            - WINGscalar*SWref\n            - (PODscalar + dOEWscalar)\n            *AIRFLOWref\n')


class FlopsWrapper_input_wtin_Landing_Gear(VariableTree):
    """Container for input.wtin.Landing_Gear"""

    # OpenMDAO Public Variables
    xmlg = Float(0.0, units='inch', desc='Length of extended main landing gear oleo (Default is computed internally)')
    xnlg = Float(0.0, units='inch', desc='Length of extended nose landing gear oleo (Default is computed internally)')
    wldg = Float(0.0, units='lb', desc='Design landing weight (if WRATIO is input in Namelist &AERIN, WLDG = GW*WRATIO) See Namelist &AERIN for WRATIO defaults.')
    mldwt = Enum(0, (1,0), desc='= 1, The design landing weight is set to the end of descent weight for the main mission plus DLDWT.  Use only if IRW = 1 in Namelist &MISSIN.  = 0, The design landing weight is determined by WLDG above or WRATIO in Namelist &AERIN')
    dldwt = Float(0.0, units='lb', desc='Delta landing weight for MLDWT = 1')
    carbas = Float(0.0, desc='Carrier based aircraft switch, affects weight of flight crew, avionics and nose gear = 1., Carrier based = 0., Land based')


class FlopsWrapper_input_wtin_Inertia(VariableTree):
    """Container for input.wtin.Inertia"""

    # OpenMDAO Public Variables
    inrtia = Enum(0, (1,0), desc='= 1, Aircraft inertias will be calculated = 0, Otherwise', aliases=('Calculate', 'Do not calculate'))
    zht = Float(0.0, units='inch', desc='Vertical C.G. of the horizontal tail (optional)')
    zvt = Float(0.0, units='inch', desc='Vertical C.G. of the vertical tail (optional)')
    zfin = Float(0.0, units='inch', desc='Vertical C.G. of the vertical fin (optional)')
    yfin = Float(0.0, units='inch', desc='Lateral C.G. of the vertical fin (optional)')
    zef = Float(0.0, units='inch', desc='Vertical C.G. of two forward mounted engines (optional)')
    yef = Float(0.0, units='inch', desc='Lateral C.G. of two forward mounted engines (optional, may be input as a fraction of the semispan)')
    zea = Float(0.0, units='inch', desc='Vertical C.G. of one or two aft mounted engines (optional)')
    yea = Float(0.0, units='inch', desc='Lateral C.G. of one or two aft mounted engines (optional, may be input as a fraction of the semispan)')
    zbw = Float(0.0, units='inch', desc='Lowermost point of wing root airfoil section')
    zap = Float(0.0, units='inch', desc='Vertical C.G. of Auxiliary Power Unit (optional)')
    zrvt = Float(0.0, units='inch', desc='Vertical datum line (Water Line) of vertical tail theoretical root chord (optional, if blank assumes at maximum height of fuselage)')
    ymlg = Float(0.0, units='inch', desc='Lateral C.G. of extended main landing gear')
    yfuse = Float(0.0, units='inch', desc='Lateral C.G. of outboard fuselage if there is more than one fuselage')
    yvert = Float(0.0, units='inch', desc='Lateral C.G. of outboard vertical tail if there is more than one vertical tail')
    swtff = Float(0.0, desc='Gross fuselage wetted area (Default = internally computed)')
    tcr = Float(0.0, desc='Wing root thickness-chord ratio (Default = TOC(0) or TCA in &CONFIN)')
    tct = Float(0.0, desc='Wing tip thickness-chord ratio (Default = TOC(NETAW) or TCA in &CONFIN)')
    incpay = Enum(0, (1,0), desc='For inertia calculations, all mission fuel is placed in "tanks." \n \n = 1, Include passengers, passenger baggage, and cargo in the fuselage and contents for inertia calculations. \n \n = 0, For inertia calculations, all payload (passengers, passenger baggage, and cargo) are placed in "tanks" like the fuel', aliases=('Passengers-etc in fuse', 'All payload in tanks'))
    tx = Array(dtype=numpy_float64, units='inch', desc='x coordinates of the centroid of the Ith tank')
    ty = Array(dtype=numpy_float64, units='inch', desc='y coordinates of the centroid of the Ith tank')
    tz = Array(dtype=numpy_float64, units='inch', desc='z coordinates of the centroid of the Ith tank')
    tl = Array(dtype=numpy_float64, desc='Length of the Ith tank (optional, used only in calculating I0')
    tw = Array(dtype=numpy_float64, desc='Width of the Ith tank (optional, used only in calculating I0')
    td = Array(dtype=numpy_float64, desc='Depth of the Ith tank (optional, used only in calculating I0')
    tf = Array(dtype=numpy_float64, units='lb', desc='Weight of fuel (or payload) in Ith tank for the Jth fuel condition NOTE: Dimensions are [J,I]')


class FlopsWrapper_input_wtin_Fuselage(VariableTree):
    """Container for input.wtin.Fuselage"""

    # OpenMDAO Public Variables
    nfuse = Int(1, desc='Number of fuselages')
    xl = Float(0.0, units='ft', desc='Fuselage total length (See Fuselage Design Data)')
    wf = Float(0.0, units='ft', desc='Maximum fuselage width')
    df = Float(0.0, units='ft', desc='Maximum fuselage depth')
    xlp = Float(0.0, units='ft', desc='Length of passenger compartment (Default is internally computed)')


class FlopsWrapper_input_wtin_Fuel_System(VariableTree):
    """Container for input.wtin.Fuel_System"""

    # OpenMDAO Public Variables
    ntank = Int(7, desc='Number of fuel tanks')
    fulwmx = Float(-1.0, units='lb', desc='Total fuel capacity of wing.  The default is internally calculated from:\n \n                             TCA * SW**2         TR\n FULWMX = FWMAX * ---------- * ( 1 - -------- )\n                                SPAN         (1+TR)**2\n \n Where the default value of FWMAX is 23.  If FULWMX is input < 50, it is interpreted as FWMAX and the above equation is used.  This equation is also used for scaling when the wing area, t/c, aspect ratio, or taper ratio is varied or optimized.\n \n Alternatively,  FULWMX = FUELRF + FUSCLA*(SW**1.5 - FSWREF**1.5)\n + FUSCLB*(SW - FSWREF)\n')
    fulden = Float(1.0, desc='Fuel density ratio for alternate fuels compared to jet fuel (typical density of 6.7 lb/gal), used in the calculation of FULWMX (if FULWMX is not input) and in the calculation of fuel system weight.')
    fuelrf = Float(0.0, units='lb', desc='Fuel capacity at FSWREF for alternate method')
    fswref = Float(-1.0, units='ft*ft', desc='Reference wing area for alternate method (Default = SW in Namelist &CONFIN)')
    fuscla = Float(0.0, desc='Alternate fuel capacity scaling method - Factor A')
    fusclb = Float(0.0, desc='Alternate fuel capacity scaling method - Factor B')
    fulfmx = Float(0.0, desc='Total fuel capacity of fuselage (wing ')
    ifufu = Int(0, desc='= 1, Fuselage fuel capacity is adjusted to meet the required fuel capacity for the primary mission.  Use only if IRW = 1 in Namelist &MISSIN, and use with care - some passengers can')
    fulaux = Float(0.0, units='lb', desc='Auxiliary (external) fuel tank capacity (Fighters only)')


class FlopsWrapper_input_wtin_Detailed_Wing(VariableTree):
    """Container for input.wtin.Detailed_Wing"""

    # OpenMDAO Public Variables
    etaw = Array(dtype=numpy_float64, desc='Wing station location - fraction of semispan or distance from fuselage centerline.  Typically, goes from 0. to 1.  Input fixed distances (>1.1) are not scaled with changes in span.')
    chd = Array(dtype=numpy_float64, desc='Chord length - fraction of semispan or actual chord.   Actual chord lengths (>5.) are not scaled.')
    toc = Array(dtype=numpy_float64, desc='Thickness - chord ratio')
    swl = Array(dtype=numpy_float64, units='deg', desc='Sweep of load path.  Typically parallel to rear spar tending toward max t/c of airfoil.  The Ith value is used between wing stations I and I+1.')
    etae = Array(array([0.3, 0.6, 0.0, 0.0]), dtype=numpy_float64, desc='Engine locations - fraction of semispan or distance from fuselage centerline.  Actual distances are not scaled with changes in span.  NEW/2 values are input')
    pctl = Float(1.0, desc='Fraction of load carried by defined wing')
    arref = Float(0.0, desc='Reference aspect ratio (Default = AR in &CONFIN)')
    tcref = Float(0.0, desc='Reference thickness-chord ratio (Default = TCA in &CONFIN)')
    nstd = Int(50, desc='Number of integration stations')
    pdist = Float(2.0, desc='Pressure distribution indicator\n= 0., Input distribution - see below\n= 1., Triangular distribution\n= 2., Elliptical distribution\n= 3., Rectangular distribution PDIST is a continuous variable, i.e., a value of 1.5 would be half way between triangular and elliptical.\nCAUTION - the constants in the wing weight calculations were correlated with existing aircraft assuming an elliptical distribution.  Use the default value unless you have a good reason not to.')
    etap = Array(dtype=numpy_float64, desc='Fraction of wing semispan')
    pval = Array(dtype=numpy_float64, desc='Relative spanwise pressure at ETAP(J)')


class FlopsWrapper_input_wtin_Crew_Payload(VariableTree):
    """Container for input.wtin.Crew_Payload"""

    # OpenMDAO Public Variables
    npf = Int(0, desc='Number of first class passengers')
    npb = Int(0, desc='Number of business class passengers')
    npt = Int(0, desc='Number of tourist passengers')
    nstu = Int(-1, desc='Number of flight attendants (optional)')
    ngalc = Int(-1, desc='Number of galley crew (optional)')
    nflcr = Int(-1, desc='Number of flight crew (optional)')
    wppass = Float(165.0, units='lb', desc='Weight per passenger')
    bpp = Float(-1.0, units='lb', desc='Weight of baggage per passenger (Default = 35., or 40. if DESRNG in Namelist &CONFIN > 900., or 44. if DESRNG > 2900.)')
    cargf = Float(0.0, desc='Military cargo aircraft floor factor = 0., Passenger transport\n= 1., Military cargo transport floor')
    cargow = Float(0.0, units='lb', desc='Cargo carried in wing (Weight of wing-mounted external stores for fighters)')
    cargof = Float(0.0, units='lb', desc='Cargo (other than passenger baggage) carried in fuselage (Fuselage external stores for fighters)')


class FlopsWrapper_input_wtin_Center_of_Gravity(VariableTree):
    """Container for input.wtin.Center_of_Gravity"""

    # OpenMDAO Public Variables
    cgw = Float(0.0, units='inch', desc='Longitudinal C.G. of wing')
    cght = Float(0.0, units='inch', desc='Longitudinal C.G. of horizontal tail')
    cgvt = Float(0.0, units='inch', desc='Longitudinal C.G. of vertical tail')
    cgfin = Float(0.0, units='inch', desc='Longitudinal C.G. of wing vertical fins')
    cgcan = Float(0.0, units='inch', desc='Longitudinal C.G. of canard')
    cgf = Float(0.0, units='inch', desc='Longitudinal C.G. of fuselage')
    cglgn = Float(0.0, units='inch', desc='Longitudinal C.G. of nose landing gear')
    cglgm = Float(0.0, units='inch', desc='Longitudinal C.G. of main landing gear')
    cgef = Float(0.0, units='inch', desc='Longitudinal C.G. of two forward mounted engines')
    cgea = Float(0.0, units='inch', desc='Longitudinal C.G. of one or two aft mounted engines')
    cgap = Float(0.0, units='inch', desc='Longitudinal C.G. of auxiliary power unit')
    cgav = Float(0.0, units='inch', desc='Longitudinal C.G. of avionics group (optional)')
    cgarm = Float(0.0, units='inch', desc='Longitudinal C.G. of armament group - includes thermal protection system or armor and fixed weapons (Default = CGF)')
    cgcr = Float(0.0, units='inch', desc='Longitudinal C.G. of flight crew')
    cgp = Float(0.0, units='inch', desc='Longitudinal C.G. of passengers')
    cgcw = Float(0.0, units='inch', desc='Longitudinal C.G. of wing cargo or external stores')
    cgcf = Float(0.0, units='inch', desc='Longitudinal C.G. of fuselage cargo or external stores')
    cgzwf = Float(0.0, units='inch', desc='Longitudinal C.G. of fuselage fuel')
    cgfwf = Float(0.0, units='inch', desc='Longitudinal C.G. of wing fuel in full condition')
    cgais = Float(0.0, units='inch', desc='Longitudinal C.G. of air induction system')
    cgacon = Float(0.0, units='inch', desc='Longitudinal C.G. of air conditioning system')
    cgaxg = Float(0.0, units='inch', desc='Longitudinal C.G. of auxiliary gear')
    cgaxt = Float(0.0, units='inch', desc='Longitudinal C.G. of auxiliary tanks')
    cgammo = Float(0.0, units='inch', desc='Longitudinal C.G. of ammunition and nonfixed weapons')
    cgmis = Float(0.0, units='inch', desc='Longitudinal C.G. of miscellaneous operating items')


class FlopsWrapper_input_wtin_Basic(VariableTree):
    """Container for input.wtin.Basic"""

    # OpenMDAO Public Variables
    ulf = Float(3.75, desc='Structural ultimate load factor')
    dgw = Float(1.0, units='lb', desc='Design gross weight - fraction of GW (see &CONFIN) or weight')
    vmmo = Float(0.0, desc='Maximum operating Mach number (Default = VCMN, Namelist &CONFIN)')
    nwref = Enum(39, (39,37,33,26), desc='The number of the reference weight for percentage weight output.', aliases=('Ramp weight', 'Zero fuel weight', 'Operating weight empty', 'Weight empty'))
    cgrefl = Float(0.0, units='inch', desc='Reference length for percentage C.G. location output (Default = XL*12., fuselage length)')
    cgrefx = Float(0.0, units='inch', desc='X - location of start of reference length')
    mywts = Enum(0, (0,1), desc='= 0, Weights will be computed\n = 1, Otherwise (See User-Specified Weights, Namelist &MISSIN)', aliases=('Compute weight', 'User-specified'))
    hydpr = Float(3000.0, units='psi', desc='Hydraulic system pressure')
    wpaint = Float(0.0, units='psf', desc='Weight of paint for all wetted areas')
    ialtwt = Enum(0, (0,1), desc='= 1, Alternate weight equations for some components will be used (Special option)\n= 0, Normal FLOPS weight equations will be used', aliases=('Normal', 'Alternate'))


class FlopsWrapper_input_wtin(VariableTree):
    """Container for input.wtin"""

    # OpenMDAO Public Variables

    def __init__(self, *args, **kwargs):
        """Constructor for the FlopsWrapper_input_wtin component"""

        super(FlopsWrapper_input_wtin, self).__init__(*args, **kwargs)

        # VariableTrees
        self.add('Basic',  FlopsWrapper_input_wtin_Basic())
        self.add('Center_of_Gravity',  FlopsWrapper_input_wtin_Center_of_Gravity())
        self.add('Crew_Payload',  FlopsWrapper_input_wtin_Crew_Payload())
        self.add('Detailed_Wing',  FlopsWrapper_input_wtin_Detailed_Wing())
        self.add('Fuel_System',  FlopsWrapper_input_wtin_Fuel_System())
        self.add('Fuselage',  FlopsWrapper_input_wtin_Fuselage())
        self.add('Inertia',  FlopsWrapper_input_wtin_Inertia())
        self.add('Landing_Gear',  FlopsWrapper_input_wtin_Landing_Gear())
        self.add('OEW_Calculations',  FlopsWrapper_input_wtin_OEW_Calculations())
        self.add('Override',  FlopsWrapper_input_wtin_Override())
        self.add('Propulsion',  FlopsWrapper_input_wtin_Propulsion())
        self.add('Tails_Fins',  FlopsWrapper_input_wtin_Tails_Fins())
        self.add('Wing_Data',  FlopsWrapper_input_wtin_Wing_Data())


class FlopsWrapper_input_tolin_Thrust_Reverser(VariableTree):
    """Container for input.tolin.Thrust_Reverser"""

    # OpenMDAO Public Variables
    inthrv = Int(-1, desc='= -1, Use takeoff thrust\n=  0, Input thrust values will be used\n=  1, Input values will be scaled\n>  1, Scaled engine deck for the (INTHRV-1)th power setting will be used')
    rvfact = Float(0.0, desc='Fraction of thrust reversed - net  (Real values should be negative)')
    velrv = Array(dtype=numpy_float64, units='ft/s', desc='Velocities for reverse thrust')
    thrrv = Array(dtype=numpy_float64, units='lb', desc='Thrust values')
    tirvrs = Float(5.0, units='s', desc='Time after touchdown to reverse thrust')
    revcut = Float(-1000.0, units='nmi', desc='Cutoff velocity for thrust reverser')
    clrev = Float(0.0, desc='Change in lift coefficient due to thrust reverser')
    cdrev = Float(0.0, desc='Change in drag coefficient due to thrust reverser')


class FlopsWrapper_input_tolin_Takeoff(VariableTree):
    """Container for input.tolin.Takeoff"""

    # OpenMDAO Public Variables
    cltom = Float(-1.0, desc='Maximum CL for takeoff (Default, see &AERIN)')
    cdmto = Float(0.0, desc='Minimum CD for takeoff, typically, this is the drag coefficient at zero lift')
    fcdmto = Float(0.3, desc='Fraction of CDMTO due to wing')
    almxto = Float(25.0, units='deg', desc='Maximum angle of attack during takeoff')
    obsto = Float(-1.0, units='ft', desc='Takeoff obstacle height (Defaults, Transport = 35., Fighter = 50.)')
    alpto = Array(array([-100.0]), dtype=numpy_float64, units='deg', desc='Angles of attack for takeoff polar')
    clto = Array(array([-100.0]), dtype=numpy_float64, desc='Lift coefficients for takeoff polar.  These are not generated internally')
    cdto = Array(array([-100.0]), dtype=numpy_float64, desc='Drag coefficients for takeoff polar.  These are not generated internally')
    inthto = Int(0, desc='= 0, Input thrust values will be used\n= 1, The input values will be scaled\n> 1, Scaled engine data deck for the (INTHTO-1)th power setting will be used')
    velto = Array(dtype=numpy_float64, units='ft/s', desc='Velocities for takeoff thrust')
    thrto = Array(dtype=numpy_float64, units='lb', desc='Thrust values')
    alprot = Float(-100.0, desc='Maximum angle of attack during rotation phase of takeoff (Default = ALMXTO)')
    vrotat = Float(1.05, desc='Minimum rotation start speed, knots or fraction of Vstall')
    vangl = Float(2.0, units='deg/s', desc='Rotation rate')
    thfact = Float(1.0, desc='Thrust multiplier for input or extracted thrust data')
    ftocl = Float(1.0, desc='Factor for takeoff lift.  Also applied to drag polars input in &PROIN')
    ftocd = Float(1.0, desc='Factor for takeoff drag.  Also applied to drag polars input in &PROIN')
    igobs = Enum(0, (0,1), desc='Gear retraction switch', aliases=('Liftoff + TDELG', 'Obstacle + TDELG'))
    tdelg = Float(0.0, units='s', desc='Time delay after liftoff/obstacle before start of landing gear retraction')
    tigear = Float(2.0, units='s', desc='Time required to retract landing gear.  Landing gear drag is reduced using a cosine function.')
    ibal = Enum(1, (1,2,0), desc='Option to compute balanced field length', aliases=('pre-1998 FAA rules', 'post-1998 FAA rules', 'Do not compute'))
    itxout = Enum(0, (1,0), desc='Weight to use for takeoff field length calculations', aliases=('Ramp weight - taxi out fuel', 'Ramp weight'))
    pilott = Float(1.0, units='s', desc='Actual pilot reaction time from engine failure to brake application.  Spoilers, brakes, and thrust reversal are assumed to become effective and engine cutback occurs at PILOTT + 2 seconds after engine failure.')
    tispa = Float(0.0, units='s', desc='Not currently used')
    tibra = Float(0.0, units='s', desc='Not currently used')
    tirva = Float(0.0, units='s', desc='Not currently used')
    ispol = Enum(1, (0,1), desc='Option for spoiler use during aborted takeoff', aliases=('Not used', 'Used'))
    irev = Enum(1, (0,1,2), desc='Option for thrust reversal during aborted takeoff', aliases=('Not used', 'Only if all engines operational', 'Always used'))


class FlopsWrapper_input_tolin_Landing(VariableTree):
    """Container for input.tolin.Landing"""

    # OpenMDAO Public Variables
    clldm = Float(-1.0, desc='Maximum CL for landing (Default, see &AERIN)')
    cdmld = Float(0.0, desc='Minimum CD for landing')
    fcdmld = Float(-1.0, desc='Fraction of CDMLD due to wing (Default = FCDMTO)')
    almxld = Float(25.0, units='deg', desc='Maximum angle of attack during landing')
    obsld = Float(50.0, units='ft', desc='Landing obstacle height')
    alpld = Array(dtype=numpy_float64, units='deg', desc='Angles of attack for landing polar')
    clld = Array(dtype=numpy_float64, desc='Lift coefficients for landing polar.  These are not generated internally')
    cdld = Array(dtype=numpy_float64, desc='Drag coefficients for landing polar.  These are not generated internally')
    inthld = Int(0, desc='= 0, Input thrust values will be used\n= 1, The input values will be scaled\n> 1, Scaled engine data deck will be used')
    velld = Array(dtype=numpy_float64, units='ft/s', desc='Velocities for landing')
    thrld = Array(dtype=numpy_float64, units='lb', desc='Thrust values')
    thdry = Float(-1.0, units='lb', desc='Maximum dry thrust at missed appproach for fighters (Default = takeoff thrust)')
    aprhgt = Float(100.0, units='ft', desc='Height above ground for start of approach')
    aprang = Float(-3.0, units='deg', desc='Approach flight path angle')
    fldcl = Float(1.0, desc='Factor for landing lift')
    fldcd = Float(1.0, desc='Factor for landing drag')
    tdsink = Float(0.0, units='ft/s', desc='Sink rate at touchdown (Must be positive if input)')
    vangld = Float(0.0, units='deg/s', desc='Flare rate (Default = VANGL)')
    noflar = Enum(0, (1,0), desc='Option for flare during landing.  If no flare, sink rate at touchdown is the approach sink rate with ground effects.', aliases=('No flare', 'Flare'))
    tispol = Float(2.0, units='s', desc='Time after touchdown to spoiler actuation')
    ticut = Float(3.0, units='s', desc='Time after touchdown to cut back of engines to zero thrust')
    tibrak = Float(4.0, units='s', desc='Time after touchdown to brake application')
    acclim = Float(16.0, units='ft/(s*s)', desc='Deceleration limit')
    magrup = Enum(-1, (1,0,-1), desc='Missed approach landing gear switch', aliases=('Gear up during missed approach', 'Gear down during missed approach', 'Use default'))


class FlopsWrapper_input_tolin_Integration_Intervals(VariableTree):
    """Container for input.tolin.Integration_Intervals"""

    # OpenMDAO Public Variables
    delvto = Float(4.0, units='ft/s', desc='Velocity step during ground run')
    deltro = Float(0.2, units='s', desc='Time step during rotation')
    deltcl = Float(0.2, units='s', desc='Time step during climbout')
    delhap = Float(10.0, units='ft', desc='Altitude step during approach')
    deldfl = Float(10.0, units='ft', desc='Distance step during flare')
    deltrn = Float(0.25, units='s', desc='Time step during runout')


class FlopsWrapper_input_tolin_Basic(VariableTree):
    """Container for input.tolin.Basic"""

    # OpenMDAO Public Variables
    apa = Float(0.0, units='ft', desc='Airport altitude')
    dtct = Float(0.0, units='degC', desc='Delta temperature from standard day.  (This parameter is independent from the DTC in Namelist &MISSIN and DTCE in Namelist &ENGINE.)')
    swref = Float(-1.0, units='ft*ft', desc='Wing area on which takeoff and landing drag polars are based (Default = SW, Namelist &CONFIN). If different from SW, polars will be scaled.')
    arret = Float(-1.0, desc='Wing aspect ratio on which takeoff and landing drag polars are based (Default = AR, Namelist &CONFIN). If different from AR, polars will be modified.')
    whgt = Float(8.0, units='ft', desc='Wing height above ground')
    alprun = Float(0.0, units='deg', desc='Angle of attack on ground')
    tinc = Float(0.0, units='deg', desc='Thrust incidence on ground')
    rollmu = Float(0.025, desc='Coefficient of rolling friction')
    brakmu = Float(0.3, desc='Coefficient of friction, brakes on')
    cdgear = Float(0.0, desc='Landing gear drag coefficient')
    cdeout = Float(0.0, desc='Delta drag coefficient due to engine out condition.  Includes effect of stopped or windmilling engine and the trim drag associated with compensating for asymmetric thrust.')
    clspol = Float(0.0, desc='Spoiler delta lift coefficient (Should be negative)')
    cdspol = Float(0.0, desc='Spoiler delta drag coefficient')
    incgef = Enum(1, (1,0), desc='Ground effects switch', aliases=('Ground effects', 'No ground effects'))
    argef = Float(1.0, desc='Aspect ratio factor for ground effects')
    itime = Enum(0, (1,0), desc='Detailed takeoff and landing profiles print option', aliases=('Print', 'No print'))


class FlopsWrapper_input_tolin(VariableTree):
    """Container for input.tolin"""

    def __init__(self, *args, **kwargs):
        """Constructor for the FlopsWrapper_input_tolin component"""

        super(FlopsWrapper_input_tolin, self).__init__(*args, **kwargs)

        # VariableTrees
        self.add('Basic',  FlopsWrapper_input_tolin_Basic())
        self.add('Integration_Intervals',  FlopsWrapper_input_tolin_Integration_Intervals())
        self.add('Landing',  FlopsWrapper_input_tolin_Landing())
        self.add('Takeoff',  FlopsWrapper_input_tolin_Takeoff())
        self.add('Thrust_Reverser',  FlopsWrapper_input_tolin_Thrust_Reverser())


class FlopsWrapper_input_syntin_Variables(VariableTree):
    """Container for input.syntin.Variables"""

    # OpenMDAO Public Variables
    desrng = Float(-1.0, desc='Design range, n.mi. (or endurance, min.). See INDR in Namelist &MISSIN (Overrides input in Namelist &CONFIN).')
    vappr = Float(-1.0, units='nmi', desc='Maximum allowable landing approach velocity (Overrides input in Namelist &AERIN)')
    flto = Float(-1.0, units='ft', desc='Maximum allowable takeoff field length (Overrides input in Namelist &AERIN)')
    flldg = Float(-1.0, units='ft', desc='Maximum allowable landing field length (Overrides input in Namelist &AERIN)')
    exfcap = Float(0.0, units='lb', desc='Minimum allowable excess fuel capacity')
    cdtmax = Float(-1.0, units='degR', desc='Maximum allowable compressor discharge temperature (Overrides input in Namelist &ENGINE')
    cdpmax = Float(-1.0, units='psi', desc='Maximum allowable compressor discharge pressure (Overrides input in Namelist &ENGINE')
    vjmax = Float(-1.0, units='ft/s', desc='Maximum allowable jet velocity (Overrides input in Namelist &ENGINE')
    stmin = Float(-1.0, units='lb/lb/s', desc='Minimum allowable specific thrust (Overrides input in Namelist &ENGINE')
    armax = Float(-1.0, desc='Maximum allowable ratio of the bypass area to the core area of a mixed flow turbofan (Overrides input in Namelist &ENGINE')
    gnox = Float(0.0, units='lb', desc='Maximum allowable NOx emissions')
    roclim = Float(100.0, units='ft/min', desc='Minimum allowable potential rate of climb during climb segments')
    dhdtlm = Float(100.0, units='ft/min', desc='Minimum allowable actual rate of climb during climb segments')
    tmglim = Float(0.1, desc='Minimum allowable thrust margin, (Thrust-Drag)/Drag, during climb segments')
    ig = Array(dtype=numpy_int64, desc='= 1, Ith behavioral constraint is used in optimization\n= 0, Otherwise')
    ibfgs = Enum(1, (0,1,2,3,4,5), desc='Search algorithm for optimization', aliases=('Davidon-Fletcher-Powell', 'Broyden-Fletcher-Goldfarb-Shano', 'Conjugate Gradient (Polak-Ribiere)', 'Steepest Descent', 'Univariate Search', 'Kreisselmeier-Steinhauser with DFP'))
    itfine = Enum(0, (1,0), desc='Option to set IRW = 1 for final analysis', aliases=('Yes', 'No'))


class FlopsWrapper_input_syntin_Optimization_Control(VariableTree):
    """Container for input.syntin.Optimization_Control"""

    # OpenMDAO Public Variables
    ndd = Int(0, desc='Number of drawdowns (Defaults to analysis only - no optimization is performed.  Suggested value = 3 or 4)')
    rk = Float(0.0, desc='Initial value of RK (Default internally computed)')
    fdd = Float(0.2, desc='RK multiplier for successive drawdowns')
    nlin = Int(-1, desc='Maximum number of gradients per drawdown (Default = number of active design variables times 2)')
    nstep = Int(20, desc='Maximum number of steps per one-dimensional minimization (Default = 20)')
    ef = Float(3.0, desc='Limits one-dimensional minimization step size to EF times previous step')
    eps = Float(0.001, desc='Fraction of initial design variable value used as a finite difference delta')
    amult = Float(10.0, desc='The initial step in a one-dimensional search is controlled by the design variable value times EPS times AMULT')
    dep = Float(0.001, desc='One-dimensional search convergence criterion on step size as a fraction of move distance')
    accux = Float(3.0e-4, desc='One-dimensional search convergence criterion on step size as a fraction of initial design variable value')
    glm = Float(0.0, desc='Value of G at which constraint switches to quadratic extended form, a value of .002 is recommended')
    gfact = Array(dtype=numpy_float64, desc='Scaling factor for each behavioral constraint')
    autscl = Float(1.0, desc='Design variable scale factor exponent.  Scale factors for design variables default to VALUE ** AUTSCL')
    icent = Enum(0, (0,1), desc='Type of differencing to be used in gradient calculations', aliases=('Forward', 'Central'))
    rhomin = Float(0.0, desc='Starting value for RHO, a scalar multiplying factor used in the KS function.  (Default is computed internally)')
    rhomax = Float(300.0, desc='Maximum value for RHO')
    rhodel = Float(0.0, desc='RHO increment (Default is computed internally)')
    itmax = Int(30, desc='Maximum number of iterations')
    jprnt = Int(2, desc='KS module print control\n= 0, No output from the KS module\n= 999, Maximum output')
    rdfun = Float(0.01, desc='If the relative change in the KS function is less than RDFUN for three consecutive iterations, optimization is terminated.')
    adfun = Float(0.001, desc='If the absolute change in the KS function is less than ADFUN for three consecutive iterations, optimization is terminated.')


class FlopsWrapper_input_syntin(VariableTree):
    """Container for input.syntin"""

    def __init__(self, *args, **kwargs):
        """Constructor for the FlopsWrapper_input_syntin component"""

        super(FlopsWrapper_input_syntin, self).__init__(*args, **kwargs)

        # VariableTrees
        self.add('Optimization_Control',  FlopsWrapper_input_syntin_Optimization_Control())
        self.add('Variables',  FlopsWrapper_input_syntin_Variables())


class FlopsWrapper_input_rfhin(VariableTree):
    """Container for input.rfhin"""

    # OpenMDAO Public Variables
    tmach = Array(dtype=numpy_float64, desc='Mach numbers in increasing order')
    cdmin = Array(dtype=numpy_float64, desc='Minimum drag for each Mach number.\nThe lift dependent drag coefficient for the Ith Mach number is computed from:\n\nCD = CDMIN(I) + CK(I) * [CL - CLB(I)] ** 2\n+ C1SW(I) * (SW/REFAS - REFBS) ** EXPS\n+ C1TH(I) * (THRUST/REFAT - REFBT) ** EXPT\n\nwhere SW and THRUST are the current values for the wing area and for the thrust per engine, and CL is the lift coefficient.')
    ck = Array(dtype=numpy_float64, desc='Drag-due-to-lift factors for each Mach number')
    clb = Array(dtype=numpy_float64, desc='Lift coefficients corresponding to each CDMIN')
    c1sw = Array(dtype=numpy_float64, desc='Coefficient for wing area term for each Mach number.  May be a drag coefficient or D/Q depending on the values of REFAS, REFBS and EXPS.')
    c1th = Array(dtype=numpy_float64, desc='Coefficient for thrust term for each Mach number.  May be a drag coefficient or D/Q depending on the values of REFAT, REFBT and EXPT.')
    refas = Float(1.0, desc='Wing area reference value')
    refbs = Float(0.0, desc='Wing area base value')
    exps = Float(1.0, desc='Wing area term exponent')
    refat = Float(1.0, desc='Thrust reference value')
    refbt = Float(0.0, desc='Thrust base value')
    expt = Float(1.0, desc='Thrust term exponent')


class FlopsWrapper_input_proin(VariableTree):
    """Container for input.proin"""

    # OpenMDAO Public Variables
    npol = Int(0, desc='Number of drag polars to be printed out (Default = size of dflap)')
    alpro = Array(dtype=numpy_float64, units='deg', desc='Angles of attack for each drag polar')
    clpro = Array(dtype=numpy_float64, desc='Lift coefficients for each drag polar')
    cdpro = Array(dtype=numpy_float64, desc='Drag coefficients for each drag polar')
    dflap = Array(array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), dtype=numpy_float64, units='deg', desc='Flap deflection corresponding to each drag polar.  Used only for output')
    ntime = Enum(0, (1,0), desc='Option for printing detailed takeoff and climb profiles for noise', aliases=('Print', 'No print'))
    ipcmax = Int(1, desc='Maximum engine power code (This variable could be used, for example, to limit takeoff and climb to dry power settings on an afterburning engine.)')
    keas = Enum(0, (1,0), desc='Type of velocity given by VFIX in namelist &SEGIN', aliases=('Knots equivalent airspeed (keas)', 'True airspeed'))
    txf = Float(-1.0, units='lb', desc='Fuel used in taxiing out to runway (Default is computed in mission analysis)')
    alpmin = Float(0.0, units='deg', desc='Minimum angle of attack during climb segment')
    gamlim = Float(0.0, units='deg', desc='Minimum flight path angle during fixed angle of attack segments')
    inm = Enum(0, (1,0), desc='Option to generate data files necessary for transporting FLOPS takeoff and climb profile data to the FAA Integrated Noise Model (INM) program', aliases=('Generate', 'Do not generate'))
    iatr = Enum(0, (1,0), desc='Automatic thrust restoration indicator option (INM=1, has no effect of takeoff and climb profile)', aliases=('ATR', 'No ATR'))
    fzf = Float(1.25, desc='Maneuver speed factor (INM=1)')
    thclmb = Float(-1.0, desc='Climb throttle setting (INM=1)')
    flapid = Array(dtype=numpy_str, desc='Six character label for each of the NPOL input drag polars, for example, "gearup"')


class FlopsWrapper_input_option_Program_Control(VariableTree):
    """Container for input.option.Program_Control"""

    # OpenMDAO Public Variables
    mprint = Enum(1, (0,1), desc='Print control \n = 0, Print only 3-5 line summary for each analysis. Usually used only for contour plots (IOPT = 4) \n = 1, Normal output for all analyses', aliases=('Short Summary', 'Normal'))
    iopt = Enum(1, (1,2,3,4), desc='Execution Type', aliases=('Analysis', 'Parametric Variation', 'Optimization', 'Contour or Thumbprint plot'))
    ianal = Enum(3, (1,2,3,4), desc='Analysis Type', aliases=('Weights', 'Weights and Aerodynamics', 'Full Analysis', 'Propulsion'))
    ineng = Enum(0, (0,1), desc='Force engine Data Read', aliases=('If necessary', 'Yes'))
    itakof = Enum(0, (0,1), desc='Detailed takeoff', aliases=('No', 'Yes (Namelist &TOLIN required)'))
    iland = Enum(0, (0,1), desc='Detailed landing', aliases=('No', 'Yes (Namelist &TOLIN required)'))
    nopro = Enum(0, (0,1), desc='Generate takeoff and climb profiles (Namelists &TOLIN &PROIN and &SEGIN required)', aliases=('No', 'Yes'))
    noise = Enum(0, (0,1,2), desc='Calculate noise', aliases=('No', 'Yes (Namelist &COSTIN required)', 'Yes for final analysis only'))
    icost = Enum(0, (0,1), desc='Calculate costs', aliases=('No', 'Yes (Namelist &COSTIN required)'))
    ifite = Enum(0, (0,1,2,3), desc='Weight equations', aliases=('Transports', 'Fighter/attack', 'General aviation', 'Blended wing body'))


class FlopsWrapper_input_option_Plot_Files(VariableTree):
    """Container for input.option.Plot_Files"""

    # OpenMDAO Public Variables
    ixfl = Enum(0, (0,1), desc='Generate mission summary plot files', aliases=('No', 'Yes'))
    npfile = Enum(0, (0,1,2), desc='Output takeoff and climb profiles for use with ANOPP preprocessor (andin)', aliases=('No', 'Yes', 'XFlops'))
    ipolp = Enum(0, (0,1,2), desc='Drag polar plot data', aliases=('None', 'Drag polars at existing Mach numbers', 'User specified Mach numbers'))
    polalt = Float(0.0, units='ft', desc='Altitude for drag polar plots')
    pmach = Array(dtype=numpy_float64, desc='Mach numbers for drag polar plot data')
    ipltth = Enum(0, (0,1,2), desc='Generate engine plot data', aliases=('None', 'Initial engine', 'Final scaled engine'))
    iplths = Enum(0, (0,1), desc='Design history plot data', aliases=('No', 'Yes'))
    cnfile = Str(desc='Contour or thumbprint plot data filename')
    msfile = Str(desc='Mission summary data filename')
    crfile = Str(desc='Cruise schedule summary data filename')
    tofile = Str(desc='Takeoff and landing aerodynamic and thrust data filename')
    nofile = Str(desc='Takeoff and climb profile data filename')
    apfile = Str(desc='Drag polar plot data filename')
    thfile = Str(desc='Engine plot data filename')
    hsfile = Str(desc='Design history plot filename')
    psfile = Str(desc='Excess power and load factor plot data filename')


class FlopsWrapper_input_option_Excess_Power_Plot(VariableTree):
    """Container for input.option.Excess_Power_Plot"""

    # OpenMDAO Public Variables
    xmax = Float(0.9, desc='Maximum Mach number for plots')
    xmin = Float(0.3, desc='Minimum Mach number for plots')
    xinc = Float(0.2, desc='Mach number increment for plots')
    ymax = Float(40000.0, units='ft', desc='Maximum altitude for plots')
    ymin = Float(0.0, units='ft', desc='Minimum altitude for plots')
    yinc = Float(10000.0, units='ft', desc='Altitude increment for plots')
    pltnz = Array(dtype=numpy_float64, desc='Nz at which Ps contours are plotted (or Nz)')
    pltpc = Array(dtype=numpy_float64, desc='Engine power (fraction if =< 1; else setting)')
    ipstdg = Array(dtype=numpy_int64, desc='Store drag schedule (see Namelist &MISSIN)')
    pltwt = Array(dtype=numpy_float64, units='lb', desc='Fixed weight')
    ipltsg = Array(dtype=numpy_int64, desc='Weight at start of mission segment IPLTSG is used')
    pltfm = Array(dtype=numpy_float64, desc='Fraction of fuel burned')
    pltwta = Array(dtype=numpy_float64, units='lb', desc='Delta weight')


class FlopsWrapper_input_option(VariableTree):
    """Container for input.option"""

    def __init__(self, *args, **kwargs):
        """Constructor for the FlopsWrapper_input_option component"""

        super(FlopsWrapper_input_option, self).__init__(*args, **kwargs)

        # VariableTrees
        self.add('Excess_Power_Plot',  FlopsWrapper_input_option_Excess_Power_Plot())
        self.add('Plot_Files',  FlopsWrapper_input_option_Plot_Files())
        self.add('Program_Control',  FlopsWrapper_input_option_Program_Control())


class FlopsWrapper_input_noisin_Turbine(VariableTree):
    """Container for input.noisin.Turbine"""

    # OpenMDAO Public Variables
    tsupp = Array(dtype=numpy_float64, desc='Turbine suppression spectrum')
    tbndia = Float(-1.0, units='ft', desc='Diameter of last-stage turbine')
    gear = Float(1.0, desc='Gear ratio:  turbine RPM/fan RPM')
    cs = Float(0.0, desc='Stator chord to rotor spacing ratio')
    nblr = Int(-1, desc='Number of last stage rotor blades')
    ityptb = Enum(0, (1,0), desc='Type of exit plane', aliases=('Turbofans', 'Turbojets or coplanar exits'))
    etdop = Float(4.0, desc='Exponent on source motion (Doppler) amplification on turbine noise')


class FlopsWrapper_input_noisin_Shielding(VariableTree):
    """Container for input.noisin.Shielding"""

    # OpenMDAO Public Variables
    iuotw = Enum(0, (1,0), desc='Engine location relative to wing', aliases=('Over the wing', 'Under the wing'))
    sfuse = Float(10.0, desc='Maximum fuselage shielding')
    swide = Float(60.0, units='deg', desc='Degrees of arc where fuselage shielding is greater than SFUSE/e')
    swing = Float(10.0, desc='Maximum wing shielding for over-the-wing engine')
    smx = Float(90.0, units='deg', desc='Angle in flyover plane of maximum over-the-wing shielding')
    cfuse = Float(10.0, units='ft', desc='Characteristic fuselage dimension (such as diameter)')
    cwing = Float(10.0, units='ft', desc='Characteristic wing dimension (such as chord)')


class FlopsWrapper_input_noisin_Propeller(VariableTree):
    """Container for input.noisin.Propeller"""

    # OpenMDAO Public Variables
    nb = Int(0, desc='Number of blades per propeller')
    bldia = Float(0.0, units='ft', desc='Diameter of propeller')
    blarea = Float(0.0, units='ft*ft', desc='Total blade area for one side of propeller')
    gearp = Float(1.0, desc='Ratio of propeller rpm / engine rpm')
    epdop = Float(1.0, desc='Exponent on source motion (Doppler) amplification on propeller noise')
    blth = Float(0.0, units='ft', desc='Blade thickness at 70% span')
    blch = Float(0.0, units='ft', desc='Blade chord at 70% span')
    blattk = Float(0.0, units='deg', desc='Blade angle of attack at 70% span')
    dharm = Float(0.5, desc='Rate of decrease in harmonic level beyond tenth, dB/harmonic')
    nph = Int(10, desc='Number of harmonics of BDF desired')
    ivor = Enum(1, (1,0), desc='Calculate vortex noise component', aliases=('Vortex noise', 'No vortex noise'))
    irot = Enum(1, (1,0), desc='Calculate rotational noise component', aliases=('Rotational noise', 'No rotational noise'))
    ipdir = Enum(0, (1,0), desc='Apply Boeing directivity correction', aliases=('Yes', 'No'))
    psupp = Array(dtype=numpy_float64, desc='Propeller noise suppression spectrum')


class FlopsWrapper_input_noisin_Propagation(VariableTree):
    """Container for input.noisin.Propagation"""

    # OpenMDAO Public Variables
    isupp = Enum(0, (1,0), desc='Apply suppression spectra to each source for which they are supplied', aliases=('Yes', 'No'))
    idop = Enum(0, (1,0), desc='Apply Doppler frequency and intensity correction to total noise', aliases=('Yes', 'No'))
    ignd = Enum(0, (0,1,2), desc='Ground reflection option', aliases=('None', 'Perfect reflection', 'Putnam method'))
    iatm = Enum(0, (0,1,2), desc='Atmospheric absorption correction', aliases=('None', 'SAE ARP 866', 'Bass & Shields'))
    iega = Enum(0, (1,0), desc='Extra ground attenuation', aliases=('Yes', 'No'))
    ishld = Enum(0, (1,0), desc='Shielding of fan, jet, core, turbine and propeller sources', aliases=('Yes', 'No'))
    deldb = Float(20.0, desc='Number of dB down from the peak noise level to cut off printing of noise time histories')
    heng = Float(0.0, units='ft', desc='Height of engine above ground during taxi')
    filbw = Float(1.0, desc='Fraction of filter bandwidth with a gain of 1')
    tdi = Float(1.0, units='s', desc='Reception time increment')
    rh = Float(70.0, desc='Ambient relative humidity')


class FlopsWrapper_input_noisin_Observers(VariableTree):
    """Container for input.noisin.Observers"""

    # OpenMDAO Public Variables
    xo = Array(dtype=numpy_float64, units='ft', desc='X-coordinates of observers')
    yo = Array(dtype=numpy_float64, units='ft', desc='Y-coordinates of observers')
    zo = Float(0.0, units='ft', desc='Height of all observers above the ground')
    ndprt = Enum(1, (1,0), desc='Print observer noise histories')
    ifoot = Enum(0, (1,0), desc='Print noise levels of input observers in countour format to file NSPLOT for subsequent plotting of the noise footprint', aliases=('Print', 'No print'))
    igeom = Enum(0, (1,0), desc='Print geometric relations of aircraft/observer at each time point', aliases=('Print', 'No print'))
    thrn = Float(-1.0, units='lb', desc='Thrust of baseline engine.  Geometry data and engine parameter arrays will be scaled accordingly (Default=THRSO, Namelist &WTIN)')
    icorr = Enum(0, (1,0), desc='Apply corrections to engine parameters to correct for ambient conditions', aliases=('Yes', 'No'))
    tcorxp = Float(1.0, desc='Exponent for core temperature correction in engine parameter arrays')


class FlopsWrapper_input_noisin_MSJet(VariableTree):
    """Container for input.noisin.MSJet"""

    # OpenMDAO Public Variables
    iy9 = Enum(1, (1,2,3,4,5,6), desc='Type of nozzle', aliases=('Convergent conical', 'Single multitube', 'Single multichute', 'Dual convergent conical', 'Dual, multitube on outer', 'Dual, multichute/spoke on outer'))
    n = Int(1, desc='Number of tubes (IY9=2,5) or elements (IY9=3,6)')
    rp = Float(0.0, units='ft', desc='Centerbody plug radius (IY9=2,3,5,6)')
    b9 = Float(0.0, units='deg', desc='Tube centerline cant angle (IY9-2,5)\nChute/spoke exit cant angle (IY9=3,6)')
    dt = Float(0.0, units='inch', desc='Tube diameter (IY9=2,5)')
    z5 = Float(0.0, desc='Number of rows of tubes, counting center tube (if present) as zero (IY9=2,5)')
    s1j = Float(0.0, desc='Tube centerline spacing to tube diameter ratio (IY9=2,5)')
    a6 = Float(0.0, desc='Ratio of ejector inlet area to nozzle (total or annulus) area (input zero for no ejector) (IY9=2,3,5,6)')
    zl9 = Float(0.0, desc='Ratio of ejector length to suppressor nozzle equivalent diameter (IY9=2,3,5,6)')
    a = Array(dtype=numpy_float64, desc='A(0): Ejector treatment faceplate thickness, in\nA(1): Ejector treatment hole diameter, in\nA(2): Ejector treatment cavity depth, in\nA(3): Ejector treatment open area ratio\n(IY9=2,3,5,6)')
    
    # TODO - rr and rx are units of 'Rayl' (rayleigh)
    rr = Array(dtype=numpy_float64, desc='Ejector treatment specific resistance (59 values required) (IY9=2,3,5,6)')
    rx = Array(dtype=numpy_float64, desc='Ejector treatment specific reactance (59 values required) (IY9=2,3,5,6)')
    r4 = Float(0.0, units='inch', desc='Outer circumferential flow dimension (IY9=3,6)')
    r6 = Float(0.0, units='inch', desc='Inner circumferential flow dimension (IY9=3,6)')
    ss = Float(0.0, units='inch', desc='Outer circumferential element dimension (IY9=3,6)')
    dn = Float(0.0, units='ft', desc='Nozzle outer diameter')
    aa = Float(0.0, desc='Unknown variable')
    nflt = Int(1, desc='Unknown variable')
    htr = Float(0.0, desc='Unknown variable')
    nst = Int(1, desc='Unknown variable')


class FlopsWrapper_input_noisin_Jet(VariableTree):
    """Container for input.noisin.Jet"""

    # OpenMDAO Public Variables
    inoz = Enum(0, (1,0), desc='Type of nozzle', aliases=('Coaxial', 'Circular'))
    iplug = Enum(0, (1,0), desc='Plug nozzle on primary', aliases=('Plug', 'No plug'))
    islot = Enum(0, (1,0), desc='Slot nozzle on primary', aliases=('Slot nozzle', 'No slot'))
    iaz = Enum(0, (1,0), desc='Azimuthal correction for nozzle geometry', aliases=('Yes', 'No'))
    dbaz = Float(0.0, desc='Noise reduction due to nozzle geometry at phi = 75 degrees, used only if IAZ = 1')
    ejdop = Float(1.0, desc='Exponent on source motion (Doppler) amplification on shock noise only.  Used for IJET=1,2')
    zmdc = Float(1.0, desc='Core (primary) jet design Mach number.  Used for application of non-ideally expanded shock noise.  Used for IJET=1,2')
    gammac = Float(-1.0, desc='Core (primary) jet exhaust gamma Used for IJET=1,2,6 (Default = 1.4)')
    gasrc = Float(-1.0, units='(ft*lb)/(lb*degR)', desc='Core exhaust gas constant, Used for IJET=1,2 (Default = 53.35)')
    annht = Float(0.0, units='ft', desc='Core nozzle annulus height.  Used for IJET=1,2')
    zmdf = Float(1.0, desc='Fan (secondary) jet design Mach number.  Used for application of non-ideally expanded shock noise.  Used for IJET=1,2')
    gammap = Float(-1.0, desc='Fan (secondary) jet exhaust gamma Used for IJET=1,2 (Default = GAMMAF)')
    gasrf = Float(53.35, units='(ft*lb)/(lb*degR)', desc='Fan exhaust gas constant.  Used for IJET=1,2')
    annhtf = Float(0.0, units='ft', desc='Fan nozzle annulus height.  Used for IJET=1,2')
    dhc = Float(-1.0, units='ft', desc='Core nozzle hydraulic diameter.  Used for IJET=3,4')
    dhf = Float(0.0, units='ft', desc='Fan nozzle hydraulic diameter.  Used for IJET=3,4')
    zl2 = Float(0.0, units='ft', desc='Axial distance from the outer exit plane to the exit plane of the inner nozzle.  Used for IJET=3,4')
    ifwd = Enum(0, (1,0), desc='Forward velocity effects on source.  Used for IJET=1,2,3,4,5', aliases=('Yes', 'No'))
    ishock = Enum(1, (1,0), desc='Calculate shock noise.  Used for IJET=1,2,3,4,5', aliases=('Shock noise', 'No shock'))
    zjsupp = Array(dtype=numpy_float64, desc='Jet suppression spectrum.  Used for IJET=1,2,3,4,5')


class FlopsWrapper_input_noisin_Ground_Effects(VariableTree):
    """Container for input.noisin.Ground_Effects"""

    # OpenMDAO Public Variables
    itone = Enum(0, (1,0), desc='1/3-octave bands exceeding adjacent bands by 3 dB or more are approximated as tones', aliases=('Yes', 'No'))
    #nht = Int(0, desc='Number of heights to be used to approximate a distributed source by multiple sources')
    dk = Array(dtype=numpy_float64, units='ft', desc='Heights of multiple sources from source center')


class FlopsWrapper_input_noisin_Flap_Noise(VariableTree):
    """Container for input.noisin.Flap_Noise"""

    # OpenMDAO Public Variables
    ilnoz = Enum(0, (2,1,0), desc='Nozzle type', aliases=('Coaxial, mixed flow', 'Coaxial, separate flow', 'Circular'))
    insens = Enum(0, (1,0), desc='Configuration with noise levels insensitive to flap angle', aliases=('Yes', 'No'))
    ac1 = Float(0.0, units='ft*ft', desc='Core (primary) nozzle area')
    af1 = Float(0.0, units='ft*ft', desc='Fan (secondary) nozzle area')
    bpr = Float(0.0, desc='Bypass ratio, for mixed flow coaxial nozzle')
    wingd = Float(0.0, desc='Ratio of wing chord to total nozzle diameter, used for large BPR designs when WINGD < 3')
    flsupp = Array(dtype=numpy_float64, desc='Flap noise suppression spectrum')
    eldop = Float(0.0, desc='Exponent on source motion (Doppler) amplification on flap noise')


class FlopsWrapper_input_noisin_Fan(VariableTree):
    """Container for input.noisin.Fan"""

    # OpenMDAO Public Variables
    igv = Enum(0, (1,0), desc='Inlet guide vane option', aliases=('Inlet guide vane', 'No IGV'))
    ifd = Enum(0, (1,0), desc='Inlet flow distortion option during ground run', aliases=('Inlet flow distortion', 'No distortion'))
    iexh = Enum(2, (0,1,2), desc='Fan inlet, exhaust noise options', aliases=('Inlet only', 'Exhaust only', 'Both inlet & exhaust'))
    nfh = Int(10, desc='Number of harmonics to be considered in blade-passing tone')
    nstg = Int(-1, desc='Number of fan stages')
    suppin = Array(dtype=numpy_float64, desc='Fan inlet suppression spectrum')
    suppex = Array(dtype=numpy_float64, desc='Fan exhaust suppression spectrum')
    methtip = Enum(1, (1,2,3), desc='Method for calculation of relative tip Mach number', aliases=('ANOPP method', 'Clark', 'Use ATIPM'))
    icomb = Enum(1, (1,0), desc='Option to include combination tones if relative tip Mach number is supersonic', aliases=('Combination tones', 'No combination tones'))
    decmpt = Float(0.0, desc='Decrement to apply to combination tones')
    gammaf = Float(1.4, desc='Gamma of fan air')
    nbl = Int(-1, desc='Number of fan blades')
    nvan = Int(-1, desc='Number of stator vanes')
    fandia = Float(-1.0, units='ft', desc='Fan diameter')
    fanhub = Float(-1.0, units='ft', desc='Fan hub diameter')
    tipmd = Float(-1.0, desc='Design relative tip Mach number')
    rss = Float(100.0, desc='Rotor-stator spacing in percent')
    efdop = Float(4.0, desc='Exponent on source motion (Doppler) amplification on fan noise')
    faneff = Float(0.88, desc='Constant first stage fan efficiency, < 1.0.  Overridden by AFANEF')
    nbl2 = Int(-1, desc='Number of fan blades for second stage (Default = NBL)')
    nvan2 = Int(-1, desc='Number of stator vanes for second stage (Default = NVAN)')
    fand2 = Float(-1.0, units='ft', desc='Fan diameter for second stage (Default = FANDIA)')
    tipmd2 = Float(-1.0, desc='Design relative tip Mach number for second stage (Default = TIPMD)')
    rss2 = Float(-1.0, desc='Rotor-stator spacing in percent for second stage (Default = RSS)')
    efdop2 = Float(-1.0, desc='Exponent on source motion (Doppler) amplification on second stage fan noise (Default = EFDOP)')
    fanef2 = Float(0.88, desc='Constant second stage fan efficiency, < 1.0.  Overridden by AFANF2')
    trat = Float(-1.0, desc='Ratio of second stage temperature rise (DELT2) to that of first stage.  Either TRAT or PRAT is used to calculate DELT2.')
    prat = Float(1.0, desc='Ratio of second stage fan pressure ratio to that of first stage')


class FlopsWrapper_input_noisin_Engine_Parameters(VariableTree):
    """Container for input.noisin.Engine_Parameters"""

    # OpenMDAO Public Variables
    aepp = Array(dtype=numpy_float64, desc='Throttle settings as a fraction of net thrust')
    avc = Array(dtype=numpy_float64, units='ft/s', desc='Core/primary exhaust jet velocity (ideally expanded velocity; exclude friction and expansion alterations).  Used for IJET=1,2,3,4,6')
    avf = Array(dtype=numpy_float64, units='ft/s', desc='Fan/secondary exhaust jet velocity (ideally expanded velocity; exclude friction and expansion alterations).  Used for IJET=1,2,3,4')
    atc = Array(dtype=numpy_float64, units='degR', desc='Core/primary jet exhaust total temperature.  Used for IJET=1,2,3,4,6')
    atf = Array(dtype=numpy_float64, units='degR', desc='Fan/secondary jet exhaust total temperature.  Used for IJET=1,2,3,4')
    aac = Array(dtype=numpy_float64, units='ft*ft', desc='Core jet nozzle exhaust area.  For IJET=1,2,6, AAC represents exit area; for IJET=3,4, AAC represents throat area.')
    aaf = Array(dtype=numpy_float64, units='ft*ft', desc='Fan jet nozzle exhaust area.  For IJET=1 or IJET=2, AAF represents exit area; for IJET=3,4, AAF represents throat area.')
    adj = Array(dtype=numpy_float64, units='ft', desc='Core outer diameter; at the equivalent throat if the nozzle is C-D.   Used only for IJET=3,4')
    adj2 = Array(dtype=numpy_float64, units='ft', desc='Fan outer diameter; at the equivalent throat if the nozzle is C-D.  Used only for IJET=3,4')
    ahj = Array(dtype=numpy_float64, units='ft', desc='Core annulus height; at the equivalent throat if the nozzle is C-D.  Used only for IJET=3,4')
    ahj2 = Array(dtype=numpy_float64, units='ft', desc='Fan annulus height; at the equivalent throat if the nozzle is C-D.  Used only for IJET=3,4')
    afuel = Array(dtype=numpy_float64, units='lb/s', desc='Fuel flow.  Used if ICORE, ITURB=1; and IJET=1,2 and only if calculating GAMMAC and GASRC.')
    atipm = Array(dtype=numpy_float64, desc='Fan first-stage relative tip Mach number.  These are approximated if not input.  Used if IFAN=1')
    atipm2 = Array(dtype=numpy_float64, desc='Fan second-stage relative tip Mach number.  These are approximated if not input.  Used if IFAN=1')
    awafan = Array(dtype=numpy_float64, units='lb/s', desc='Total engine airflow.  Used if IFAN=1')
    adelt = Array(dtype=numpy_float64, units='degR', desc='Fan temperature rise.  Used if IFAN=1')
    afpr = Array(dtype=numpy_float64, desc='Fan pressure ratio.  This is not needed if ADELT is input.  Otherwise, values for ADELT will be calculated using AFANEF and AFANF2 values.')
    afanef = Array(dtype=numpy_float64, desc='Fan first-stage efficiency.  These are required if AFPR is supplied rather than ADELT.')
    afanf2 = Array(dtype=numpy_float64, desc='Fan second-stage efficiency.  These are required if AFPR is supplied rather than ADELT.')
    arpm = Array(dtype=numpy_float64, units='rpm', desc='Fan or turbine speed.  Used if IFAN, ITURB=1')
    awcore = Array(dtype=numpy_float64, units='lb/s', desc='Burner and turbine airflow.  Used if ICORE or ITURB=1 and IJET=1,2 and only if calculating GAMMAC and GASRC.')
    ap3 = Array(dtype=numpy_float64, units='psf', desc='Burner inlet pressure.  Used if ICORE=1')
    at3 = Array(dtype=numpy_float64, units='degR', desc='Burner inlet temperature.  Used if ICORE=1')
    at4 = Array(dtype=numpy_float64, units='degR', desc='Burner exit static temperature.  These are approximated from the fuel/air ratio if not input.  Used if ICORE=1')
    aturts = Array(dtype=numpy_float64, units='ft/s', desc='Turbine last stage rotor relative tip speed.  These are approximated if not input.  Used if ITURB=1')
    atctur = Array(dtype=numpy_float64, units='degR', desc='Turbine exit temperature.  These are assumed the same as ATC if not supplied.  Used if ITURB=1')
    aepwr = Array(dtype=numpy_float64, units='hp', desc='Horsepower supplied to propeller.  Used if IPROP=1')
    athrst = Array(dtype=numpy_float64, units='lb', desc='Propeller thrust.  Used if IPROP=1')
    amsp9 = Array(dtype=numpy_float64, desc='Nozzle pressure ratio: entance total to ambient static.  Used for M*S code jet predictions, IJET=5')
    amstt3 = Array(dtype=numpy_float64, units='degR', desc='Nozzle exit total temperature.  Used for M*S code jet predictions, IJET=5')
    amsa9 = Array(dtype=numpy_float64, units='ft*ft', desc='Nozzle exit area.  Used for M*S code jet predictions, IJET=5')
    amsa7 = Array(dtype=numpy_float64, desc='Nozzle ejector chute area ratio.  Used for M*S code jet predictions, IJET=5')
    amsaa8 = Array(dtype=numpy_float64, units='ft*ft', desc='Inner nozzle flow area.  Used for M*S code jet predictions, IJET=5')
    amstt4 = Array(dtype=numpy_float64, units='degR', desc='Inner nozzle exit total temperature.  Used for M*S code jet predictions, IJET=5')
    amsp4 = Array(dtype=numpy_float64, desc='Inner nozzle pressure ratio: entrance total to ambient static.  Used for M*S code jet predictions, IJET=5')
    amstt5 = Array(dtype=numpy_float64, units='degR', desc='Outer nozzle exit total temperature.  Used for M*S code jet predictions, IJET=5')
    amsp5 = Array(dtype=numpy_float64, desc='Outer nozzle pressure ratio: entrance total to ambient static.  Used for M*S code jet predictions, IJET=5')


class FlopsWrapper_input_noisin_Core(VariableTree):
    """Container for input.noisin.Core"""

    # OpenMDAO Public Variables
    csupp = Array(dtype=numpy_float64, desc='Core suppression spectrum')
    gamma = Float(1.4, desc='Specific heat ratio;  required if using AP3 rather than AT3')
    imod = Enum(0, (1,0), desc='Use modified core level prediction', aliases=('Yes', 'No'))
    dtemd = Float(-1.0, units='degR', desc='Design turbine temperature drop')
    ecdop = Float(2.0, desc='Exponent on source motion (Doppler) amplification on core noise')


class FlopsWrapper_input_noisin_Basic(VariableTree):
    """Container for input.noisin.Basic"""

    # OpenMDAO Public Variables
    iepn = Enum(0, (0,1,2), desc='= 0, Stage III\n= 1, Stage III - Delta dB (see DEPNT, DEPNS and DEPNL)\n=2, Find the X-coordinate where the maximum EPNL occurs.  NOB, XO and YO must be input.  YO should be constant.  IEPN=2 is usually used to get a sideline (YO) noise for GA aircraft.', aliases=('Stage III', 'Stage III - Delta', 'Find max. EPNL'))
    depnt = Float(0.0, desc='Increment below Stage III for takeoff (see IEPN)')
    depns = Float(0.0, desc='Increment below Stage III for sideline (see IEPN).\nIf IEPN=2, DEPNS is the upper limit for sideline noise.')
    depnl = Float(0.0, desc='Increment below Stage III for landing (see IEPN)')
    itrade = Enum(0, (1,0), desc='Option to trade 2 dB between sideline and flyover noise', aliases=('Trade', 'No trade'))
    ijet = Enum(0, (0,1,2,3,4,5,6), desc='Jet noise option', aliases=('None', 'Stone/Clark', 'Kresja', 'Stone ALLJET', 'Stone JET181', 'GE M*S', 'SAE A-21 (ANOPP)'))
    ifan = Enum(0, (0,1,2), desc='Fan noise option', aliases=('None', 'Heidmann', 'Gliebe'))
    icore = Enum(0, (0,1), desc='Core noise option', aliases=('None', 'Core noise'))
    iturb = Enum(0, (0,1), desc='Turbine noise option', aliases=('None', 'Turbine noise'))
    iprop = Enum(0, (0,1,2), desc='Propeller noise option', aliases=('None', 'SAE', 'Gutin'))
    iflap = Enum(0, (0,1), desc='Flap noise/Jet-flap impingement noise option', aliases=('None', 'Flap & jet/flap noise'))
    iairf = Enum(0, (0,1), desc='Airframe noise option', aliases=('None', 'Airframe noise'))
    igear = Enum(0, (0,1), desc='Gear box noise option', aliases=('None', 'Approx. gear box noise'))


class FlopsWrapper_input_noisin_Airframe(VariableTree):
    """Container for input.noisin.Airframe"""

    # OpenMDAO Public Variables
    ifl = Enum(0, (1,0), desc='Include slotted flap noise', aliases=('Slotted flap noise', 'No slotted flap noise'))
    nf = Int(2, desc='Number of trailing edge flap slots for IFL = 1')
    pfchd = Float(0.25, desc='Average chord for slotted flap, ft or fraction of wing chord.  Used only if IFL = 1')
    itypw = Enum(1, (1,2), desc='Type of wing', aliases=('Conventional', 'Delta'))
    iclean = Enum(0, (1,0), desc='Aerodynamically clean aircraft', aliases=('Aerodynamically clean', 'Conventional'))
    iwing = Enum(0, (1,0), desc='Wing, horizontal and vertical tail noise', aliases=('Wing, horiz., vert. tail noise', 'No wing, tail noise'))
    islat = Enum(0, (1,0), desc='Slatted leading edge noise', aliases=('Slatted l.e. noise', 'No slatted l.e. noise'))
    ilg = Enum(0, (1,0), desc='Nose and main landing gear noise', aliases=('Landing gear noise', 'No landing gear noise'))
    ng = Array(dtype=numpy_int64, desc='NG(0):  Number of nose gear trucks\nNG(1):  Number of main gear trucks')
    nw = Array(dtype=numpy_int64, desc='NW(0):  Number of wheels per nose gear truck\nNW(1):  Number of wheels per main gear truck')
    dw = Array(dtype=numpy_float64, units='ft', desc='DW(0):  Diameter of nose gear tires\nDW(1):  Diameter of main gear tires')
    cg = Array(dtype=numpy_float64, desc='CG(0):  Ratio of nose strut length to DW(0)\nCG(1):  Ratio of main strut length to DW(1)')


class FlopsWrapper_input_noisin(VariableTree):
    """Container for input.noisin"""

    def __init__(self, *args, **kwargs):
        """Constructor for the FlopsWrapper_input_noisin component"""

        super(FlopsWrapper_input_noisin, self).__init__(*args, **kwargs)

        # VariableTrees
        self.add('Airframe',  FlopsWrapper_input_noisin_Airframe())
        self.add('Basic',  FlopsWrapper_input_noisin_Basic())
        self.add('Core',  FlopsWrapper_input_noisin_Core())
        self.add('Engine_Parameters',  FlopsWrapper_input_noisin_Engine_Parameters())
        self.add('Fan',  FlopsWrapper_input_noisin_Fan())
        self.add('Flap_Noise',  FlopsWrapper_input_noisin_Flap_Noise())
        self.add('Ground_Effects',  FlopsWrapper_input_noisin_Ground_Effects())
        self.add('Jet',  FlopsWrapper_input_noisin_Jet())
        self.add('MSJet',  FlopsWrapper_input_noisin_MSJet())
        self.add('Observers',  FlopsWrapper_input_noisin_Observers())
        self.add('Propagation',  FlopsWrapper_input_noisin_Propagation())
        self.add('Propeller',  FlopsWrapper_input_noisin_Propeller())
        self.add('Shielding',  FlopsWrapper_input_noisin_Shielding())
        self.add('Turbine',  FlopsWrapper_input_noisin_Turbine())


class FlopsWrapper_input_nacell(VariableTree):
    """Container for input.nacell"""

    # OpenMDAO Public Variables
    x1r = Float(2.06, desc='X1 / R.  If IVAR = -1, X1R is the cowl length divided by the inlet capture radius.')
    x2r = Float(1.58, desc='X2 / R')
    r1r = Float(0.354, desc='R1 / R')
    r2r = Float(0.585, desc='R2 / R')
    angle = Float(7.0, units='deg', desc='Average angle of the subsonic diffuser portion of the inlet between the throat and the engine face')
    clang = Float(0.0, units='deg', desc='Cowl lip angle')
    mixed = Enum(-1, (-1,0,1), desc='Inlet compression type indicator\n= -1, Inlet geometry is based solely on the geometry variables described above.\n=  0, Inlet geometry is based in the internal geometry data base for external compression inlets and the given inlet design Mach number.\n=  1, Inlet geometry is based in the internal geometry data base for mixed compression inlets and the given inlet design Mach number', aliases=('Use geometry variables', 'External compression inlet', 'Mixed compression inlet'))
    radd = Float(3.0, units='inch', desc='Distance from the engine compressor tip to the exterior of the nacelle.  If RADD < 1. the added radial distance is RADD times the compressor tip radius.')
    xnlod = Float(-10.0, desc='Nozzle length / diameter (Default is computed')
    xnld2 = Float(-10.0, desc='Fan nozzle length / diameter (Default is computed')
    inac = Enum(0, (-5,-4,-3,-2,-1,0,1,2,3,4,5), desc='Nacelle type indicator', aliases=('2-D Bifurcated inlet + axisymmetric nozzle + podded together', '2-D Bifurcated inlet + 2-D nozzle + podded together', '2-D inlet + axisymmetric nozzle + podded together', '2-D + podded together', 'Axisymmetric + podded together', 'None', 'Axisymmetric', '2-D', '2-D inlet + Axisymmetric nozzle', '2-D Bifurcated inlet + 2-D nozzle', '2-D Bifurcated inlet + axisymmetric nozzle'))
    ivar = Enum(1, (-1,0,1,2,3), desc='Inlet variable geometry switch used to estimate weight factor WTCB1', aliases=('Fixed no centerbody', 'Fixed centerbody', 'Translating centerbody', 'Collapsing centerbody', 'Translating & collapsing centerbody'))
    nvar = Enum(0, (0,1,2,3,4), desc='Nozzle variable geometry switch used to estimate weight factor WTNOZ', aliases=('Fixed geometry', 'Variable area throat', 'Variable area exit', 'Variable throat & exit', 'Fixed plug core & fixed fan nozzle'))
    wtcb1 = Float(-10.0, desc='Weighting factor for the inlet centerbody up to the throat.   Multiplied by the surface area of the applicable inlet section to predict inlet weight.  The default is based on the internal materials data base and the maximum cruise Mach number.')
    wtcb2 = Float(-10.0, desc='Weighting factor for the inlet centerbody from the throat to the engine face.  Multiplied by the surface area of the applicable inlet section to predict inlet weight.  The default is based on the internal materials data base and the maximum cruise Mach number.')
    wtint = Float(-10.0, desc='Weighting factor for the internal cowl up to the engine face.  Multiplied by the surface area of the applicable inlet section to predict inlet weight.  The default is based on the internal materials data base and the maximum cruise Mach number.')
    wtext = Float(-10.0, desc='Weighting factor for the external nacelle.  Multiplied by the surface area of the applicable inlet section to predict inlet weight.  The default is based on the internal materials data base and the maximum cruise Mach number.')
    wtnoz = Float(-10.0, desc='Weighting factor for the nozzle.  Multiplied by the surface area of the applicable inlet section to predict inlet weight.  The default is based on the internal materials data base and the maximum cruise Mach number.')
    h2w = Float(1.0, desc='Inlet height to width ratio for 2-D inlets')


class FlopsWrapper_input_mission_definition(VariableTree):
    """Container for input.mission_definition"""

    # OpenMDAO Public Variables
    mission = List(iotype='in')


class FlopsWrapper_input_missin_User_Weights(VariableTree):
    """Container for input.missin.User_Weights"""

    # OpenMDAO Public Variables
    mywts = Enum(0, (0,1), desc='Weight input switch, overrides value input in Namelist &WTIN.', aliases=('Compute weight', 'User-specified'))
    rampwt = Float(0.0, units='lb', desc='Gross weight before taxi out (Default = DOWE + PAYLOD + FUEMAX)')
    dowe = Float(0.0, units='lb', desc='Fixed operating weight empty')
    paylod = Float(0.0, units='lb', desc='Fixed payload weight')
    fuemax = Float(0.0, units='lb', desc='Total usable fuel weight\nFUEMAX = RAMPWT - DOWE - PAYLOD.\nRequired only if RAMPWT is not input')


class FlopsWrapper_input_missin_Turn_Segments(VariableTree):
    """Container for input.missin.Turn_Segments"""

    # OpenMDAO Public Variables
    xnz = Array(dtype=numpy_float64, units='g', desc='Maximum turn load factor at each Mach number')
    xcl = Array(dtype=numpy_float64, desc='Maximum turn lift coefficient at each Mach number')
    xmach = Array(dtype=numpy_float64, desc='Mach number array corresponding to both XNZ and XCL')


class FlopsWrapper_input_missin_Store_Drag(VariableTree):
    """Container for input.missin.Store_Drag"""

    # OpenMDAO Public Variables
    stma = Array(dtype=numpy_float64, desc='Mach number schedule for store drags.  Store drags can also be assessed in ACCEL and TURN segments of the mission as covered in the Segment Definition Cards section, in PS and NZ plots (see Namelist &OPTION), and in performance constraints (see Namelist &PCONIN)')
    cdst = Array(dtype=numpy_float64, desc='Corresponding drag coefficients or D/q')
    istcl = Array(dtype=numpy_int64, desc='Store drag condition applied to climb schedule K\n= 0, No store drag for climb schedule K')
    istcr = Array(dtype=numpy_int64, desc='Store drag condition applied to cruise schedule K\n= 0, No store drag for cruise schedule K')
    istde = Int(0, desc='Store drag condition applied to descent schedule\n= 0, No store drag for descent schedule')


class FlopsWrapper_input_missin_Reserve(VariableTree):
    """Container for input.missin.Reserve"""

    # OpenMDAO Public Variables
    irs = Enum(2, (1,2,3), desc='Reserve fuel calculation switch', aliases=('Calculated for trip to alternate airport plus RESRFU and/or RESTRP', 'Constant values (RESRFU and/or RESTRP) only', 'Reserve fuel is what is left over after primary mission'))
    resrfu = Float(0.0, desc='> 1., Fixed reserve fuel, lb\n< 1., Reserve fuel as a fraction of total usable fuel weight')
    restrp = Float(0.0, desc='Reserve fuel as a fraction of total trip fuel weight')
    timmap = Float(0.0, units='min', desc='Missed approach time')
    altran = Float(0.0, units='nmi', desc='Range to alternate airport')
    nclres = Int(1, desc='Climb schedule number used in reserve mission')
    ncrres = Int(1, desc='Cruise schedule number used in reserve mission')
    sremch = Float(-1.0, desc='Start reserve Mach number (Default = CLMMIN[NCLRES])')
    eremch = Float(-1.0, desc='End reserve Mach number (Default = DEMMIN)')
    srealt = Float(-1.0, units='ft', desc='Start reserve altitude (Default = CLAMIN[NCLRES])')
    erealt = Float(-1.0, units='ft', desc='End reserve altitude (Default = DEAMIN)')
    holdtm = Float(0.0, units='min', desc='Reserve holding time')
    ncrhol = Int(0, desc='Cruise schedule number for hold (Default = NCRRES)')
    ihopos = Enum(1, (0,1,2), desc='Hold position switch', aliases=('Between main descent and missed approach', 'End of reserve cruise', 'End of reserve descent'))
    icron = Enum(0, (0,1,2), desc='Type of flight to alternate airport', aliases=('Climb-cruise-descend', 'Climb-cruise-beam down to airport', 'Cruise only'))
    thold = Float(0.0, desc='Used to define a hold segment between main mission descent and missed approach.\n> 1., Reserve holding time, min\n< 1., Fraction of flight time to be used as reserve holding time.  (Effective only if IRW = 1)\n= 0., This option is ignored')
    ncrth = Int(1, desc='Cruise schedule number for THOLD')


class FlopsWrapper_input_missin_Ground_Operations(VariableTree):
    """Container for input.missin.Ground_Operations"""

    # OpenMDAO Public Variables
    takotm = Float(0.0, units='min', desc='Takeoff time')
    taxotm = Float(0.0, units='min', desc='Taxi out time')
    apprtm = Float(0.0, units='min', desc='Approach time')
    appfff = Float(2.0, desc='Approach fuel flow factor applied to sea level static idle fuel flow')
    taxitm = Float(0.0, units='min', desc='Taxi in time')
    ittff = Int(0, desc='> 0, Engine deck power setting for takeoff (Usually = 1 if specified).  Taxi fuel flow is sea level static idle.\n= 0, Use TAKOFF and TXFUFL.')
    takoff = Float(0.0, units='lb/h', desc='Takeoff fuel flow')
    txfufl = Float(0.0, units='lb/h', desc='Taxi fuel flow')
    ftkofl = Float(0.0, units='lb', desc='Fixed takeoff fuel.  This ovverides the calculated value and is not scaled with engine thrust')
    ftxofl = Float(0.0, units='lb', desc='Fixed taxi out fuel.  This ovverides the calculated value and is not scaled with engine thrust')
    ftxifl = Float(0.0, units='lb', desc='Fixed taxi in fuel.  This ovverides the calculated value and is not scaled with engine thrust')
    faprfl = Float(0.0, units='lb', desc='Fixed approach fuel.  This ovverides the calculated value and is not scaled with engine thrust')


class FlopsWrapper_input_missin_Descent(VariableTree):
    """Container for input.missin.Descent"""

    # OpenMDAO Public Variables
    ivs = Enum(1, (0,1,2), desc='Descent option switch', aliases=('No descent time or distance or fuel', 'Descend at optimum L/D', 'Descend at constance lift coefficient'))
    decl = Float(0.8, desc='Descent lift coefficient for IVS = 2')
    demmin = Float(0.3, desc='Minimum Mach number')
    demmax = Float(0.0, desc='Max Mach number (Default = VCMN, Namelist &CONFIN)')
    deamin = Float(0.0, units='ft', desc='Minimum altitude')
    deamax = Float(0.0, units='ft', desc='Max altitude (Default = CH, Namelist &CONFIN)')
    ninde = Int(31, desc='Number of descent steps')
    dedcd = Float(0.0, desc='Drag coefficient increment applied to descent')
    rdlim = Float(-99999.0, units='ft/min', desc='Limiting or constant rate of descent.  Must be negative')
    ns = Int(0, desc='Number of altitudes for q limit schedule (Default = 0 - QLIM is used, Maximum = 20 )')
    keasvd = Enum(0, (0,1), desc='= 1, VDTAB is in knots equivalent airspeed (keas)\n\n= 0, VDTAB is true airspeed or Mach number (Default)', aliases=('VDTAB is Mach number', 'VDTAB in knots'))
    adtab = Array(dtype=numpy_float64, units='ft', desc='Descent altitude schedule.  If only part of the descent profile is specified, the portion of the profile outside the energy range defined by values of ADTAB and VDTAB will be optimized for the descent schedule.')
    vdtab = Array(dtype=numpy_float64, desc='Descent speed schedule, kts or Mach number')


class FlopsWrapper_input_missin_Cruise(VariableTree):
    """Container for input.missin.Cruise"""

    # OpenMDAO Public Variables
    ncruse = Int(1, desc='Number of cruise schedules to be defined (Default = 1, Maximum = 6, Include reserve cruise)')
    ioc = List([1], Enum(1, (0,1,2,3,4,5,6,7,8,9,10), aliases=('Opt. alt. and Mach for specific range', 'Fixed Mach + opt. alt. for specific range', 'Fixed Mach at input max. alt. or cruise ceiling', 'Fixed alt. + opt. Mach for specific range', 'Fixed alt. + opt. Mach for endurance (min. fuel flow)', 'Fixed alt. + constant lift coefficient (CRCLMX)', 'Fixed Mach + opt. alt. for endurance', 'Opt. Mach and alt. for endurance', 'Max. Mach at input fixed alt.', 'Max. Mach at opt. alt.', 'Fixed Mach + constant lift coefficient (CRCLMX')), desc='Cruise option switch')
    crmach = Array(array([0.0]), dtype=numpy_float64, desc='Maximum or fixed Mach number (or velocity, kts) (Default = VCMN, Namelist &CONFIN)')
    cralt = Array(array([-1.0]), dtype=numpy_float64, units='ft', desc='Maximum or fixed altitude (Default = CH, Namelist &CONFIN)')
    crdcd = Array(array([0.0]), dtype=numpy_float64, desc='Drag coefficient increment')
    flrcr = Array(array([1.0]), dtype=numpy_float64, desc='Specific range factor for long range cruise Mach number - used if IOC = 3')
    crmmin = Array(array([0.0]), dtype=numpy_float64, desc='Minimum Mach number')
    crclmx = Array(array([0.0]), dtype=numpy_float64, desc='Maximum or fixed lift coefficient')
    hpmin = Array(array([1000.0]), dtype=numpy_float64, units='ft', desc='Minimum cruise altitude.\nFor fixed Mach number cruise schedules, HPMIN can be used to enforce a dynamic pressure (Q) limit.')
    ffuel = Array(array([1.0]), dtype=numpy_float64, desc='Fuel factor in cruise profile optimization')
    fnox = Array(array([0.0]), dtype=numpy_float64, desc='NOx emissions factor in cruise profile optimization.\nSince for supersonic engines the NOx emissions are on the order of 1 - 3 percent of fuel, FNOX should be relatively large (30. - 100.) to get comparable weighting.')
    ifeath = List([0], Enum(0, (1,0,-1)), desc='Cruise feathering option', aliases=('Engines may be feathered', 'No feathering', 'Engines must be feathered'))
    feathf = Array(array([0.5]), dtype=numpy_float64, desc='Fraction of engines remaining after feathering')
    cdfeth = Array(array([0.0]), dtype=numpy_float64, desc='Drag coefficient increase due to feathered engines')
    dcwt = Float(1.0, units='lb', desc='Weight increment used to compute cruise tables (Default = the greater of 1. or DWT/20)')
    rcin = Float(100.0, units='ft/min', desc='Instantaneous rate of climb for ceiling calculation')
    wtbm = Array(dtype=numpy_float64, desc='Array of weights for specification of max. allowable altitude for low sonic boom configurations (must be in ascending order) Since linear interpolation/extrapolation is used, data should cover the entire expected weight range.')
    altbm = Array(dtype=numpy_float64, units='ft', desc='Corresponding array of maximum altitudes')


class FlopsWrapper_input_missin_Climb(VariableTree):
    """Container for input.missin.Climb"""

    # OpenMDAO Public Variables
    nclimb = Int(1, desc='Number of climb schedules to be defined (Default = 1, Maximum = 4, Include reserve climb)')
    clmmin = Array(array([0.3]), dtype=numpy_float64, desc='Minimum Mach number for each climb schedule.\nNote: Separate climb schedules are not required if the only changes are in the minimum or maximum Mach number or altitude.  Just make sure all climbs are bracketed.')
    clmmax = Array(array([0.0]), dtype=numpy_float64, desc='Maximum Mach number (Default = VCMN, Namelist &CONFIN).\nNote: Separate climb schedules are not required if the only changes are in the minimum or maximum Mach number or altitude.  Just make sure all climbs are bracketed.')
    clamin = Array(array([0.0]), dtype=numpy_float64, units='ft', desc='Minimum altitude')
    clamax = Array(array([0.0]), dtype=numpy_float64, units='ft', desc='Maximum altitude (Default = CH, Namelist &CONFIN)')
    nincl = Array(array([31]), dtype=numpy_int64, desc='Number of climb steps')
    fwf = Array(array([-0.0010]), dtype=numpy_float64, desc='Climb profile optimization function control parameter.  Recommended aircraft in parentheses.\n=  1., minimum fuel-to-distance profile (Subsonic transports, do NOT use for supersonic transports)\n=  0., minimum time-to-distance profile (Interceptors only)\n1. > FWF > 0., combination of the above\n= -.001, minimum time-to-climb profile (Fighters)\n= -1., minimum fuel-to-climb profile (Supersonic transports, Subsonic transports)\n-1. < FWF < -.001, combination of the above')
    ncrcl = Array(array([1]), dtype=numpy_int64, desc='Number of the cruise schedule to be used in fuel- or time-to-distance profile climb optimization comparisons')
    cldcd = Array(array([0.0]), dtype=numpy_float64, desc='Drag coefficient increment applied to each climb schedule.  If coefficient varies with Mach number, see ISTCL above.')
    ippcl = Array(array([1]), dtype=numpy_int64, desc='Number of power settings to be considered for climb.  Program will select the most efficient.  Should be used only with afterburning engines for minimum fuel climb profiles.')
    maxcl = Array(array([1]), dtype=numpy_int64, desc='Maximum power setting used for climb')
    actab = Array(zeros(shape=(0,0)), dtype=numpy_float64, units='ft', desc='Altitude schedule.  If not input, climb profile will be optimized')
    vctab = Array(zeros(shape=(0,0)), dtype=numpy_float64, units='nmi', desc='Climb speed schedule.  If not input, climb profile will be optimized')
    keasvc = Enum(0, (1,0), desc='Type of velocity input in VCTAB', aliases=('Knots equivalent airspeed (keas)', 'True airspeed or Mach no.'))
    ifaacl = Enum(1, (0,1,2), desc='Climb speed limit option', aliases=('Optimum speed', 'Max. 250 knots CAS below 10,000 ft', 'Climb to 250 kcas at 1500 ft then SPDLIM at 10,000 ft'))
    ifaade = Enum(-1, (-1,0,1), desc='Descent speed limit option', aliases=('Use default', 'Optimum speed', 'Max. 250 knots CAS below 10,000 ft'))
    nodive = Enum(0, (0,1), desc='Rate of climb limit option', aliases=('Optimum altitude at each energy level', 'Min. rate of climb limit enfored'))
    divlim = Float(0.0, units='ft/min', desc='Minimum allowable rate of climb or descent.\nEnforced only if NODIVE = 1, may be negative to allow a shallow dive during climb.')
    qlim = Float(0.0, units='psf', desc='Constant dynamic pressure limit.  Applied at all climb and descent points not covered by the variable dynamic pressure limit below.')
    spdlim = Float(0.0, desc='Maximum speed at 10,000 ft, used only for IFAACL = 2, kts or Mach number  (Default is computed from\n  a) the variable dynamic pressure limit below, if applicable,\n  b) QLIM above, if QLIM > 0., or\n  c) a dynamic pressure of 450 psf, in that order)')
    nql = Int(0, desc='Number of altitudes for q limit schedule (Default = 0 - QLIM is used, Maximum = 20 )')
    qlalt = Array(dtype=numpy_float64, units='ft', desc='Altitudes, in increasing order, for variable dynamic pressure limit schedule')
    vqlm = Array(dtype=numpy_float64, units='psf', desc='Corresponding dynamic pressure limits')


class FlopsWrapper_input_missin_Basic(VariableTree):
    """Container for input.missin.Basic"""

    # OpenMDAO Public Variables
    indr = Enum(0, (0,1), desc='= 0, DESRNG is design range in n.mi.\n= 1, DESRNG is endurance in minutes', aliases=('Range', 'Endurance'))
    fact = Float(1.0, desc='Factor to increase or decrease fuel flows.  Cumulative with FFFSUB and FFFSUP in Namelist &ENGDIN.')
    fleak = Float(0.0, units='lb/h', desc='Constant delta fuel flow')
    fcdo = Float(1.0, desc='Factor to increase or decrease lift-independent drag coefficients')
    fcdi = Float(1.0, desc='Factor to increase or decrease lift-dependent drag coefficients')
    fcdsub = Float(1.0, desc='Factor to increase or decrease all subsonic drag coefficients.  Cumulative with FCDO and FCDI.')
    fcdsup = Float(1.0, desc='Factor to increase or decrease all supersonic drag coefficients.  Cumulative with FCDO and FCDI.')
    iskal = Enum(1, (1,0), desc='Special option used to turn off engine scaling using THRUST/THRSO', aliases=('Scale engine', 'No scaling'))
    owfact = Float(1.0, desc='Factor for increasing or decreasing OWE')
    iflag = Enum(0, (0,1,2,3), desc='Mission print option', aliases=('Mission summary only', 'Plus cruise', 'Plus climb & descent', 'Plus scaled engine'))
    msumpt = Enum(0, (1,0), desc='Option to calculate and print detailed mission summary', aliases=('Yes', 'No'))
    dtc = Float(0.0, units='degC', desc='Deviation from standard day temperature (See also DTCT in Namelist &TOLIN and DTCE in Namelist &ENGINE.  These temperature deviations are independent.)')
    irw = Enum(2, (1,2), desc='Range/weight calculation option', aliases=('Range fixed-calculate ramp weight', 'Ramp weight fixed-calculate range'))
    rtol = Float(0.001, units='nmi', desc='Tolerance in range calculation for IRW = 1')
    nhold = Int(0, desc='Special option - Time for segment NHOLD (which must be a Hold Segment) is adjusted until the specified range is met for the input ramp weight.  Note - IRW must be 1')
    iata = Enum(1, (1,0), desc='Option to adjust range for ATA Traffic Allowance', aliases=('Yes', 'No'))
    tlwind = Float(0.0, units='nmi', desc='Velocity of tail wind (Input negative value for head wind)')
    dwt = Float(1.0, units='lb', desc='Gross weight increment for performance tables (Default is internally computed)')
    offdr = Array(dtype=numpy_float64, units='nmi', desc='Off design range.  Note: This simply performs the defined mission with the sized airplane with a different design range.  If more changes are desired or if additional analyses are required (e.g., cost analysis), use Namelist &RERUN.  If OFFDR is used with a cost analysis, costs will be computed for the last design range.')
    idoq = Enum(0, (1,0), desc='Form for drag increments', aliases=('D/q', 'Drag coefficients'))
    nsout = Int(0, desc='Last segment number in outbound leg (Combat Radius Mission - Iterates until outbound leg and inbound leg are equal.  IRW must be equal to 2, and there must be at least two cruise segments).  If NSOUT = 0, radius is not calculated')
    nsadj = Int(0, desc='Cruise segment in outbound leg to be adjusted for radius calculation (Default = NSOUT).  Note: Make sure that the NSADJ Cruise segment is terminated on total rather than segment distance in the Mission Definition Data.')
    mirror = Int(0, desc='Cruise segment in inbound leg to be set equal to segment NSADJ  (if MIRROR = 0, only total leg lengths are forced to be equal).  This option would be used for a high-low-low-high mission where the dash in and dash out are unknown but must be equal to each other.  NSADJ would be the dash in segment number, and MIRROR would be the dash out segment number.')


class FlopsWrapper_input_missin(VariableTree):
    """Container for input.missin"""

    def __init__(self, *args, **kwargs):
        """Constructor for the FlopsWrapper_input_missin component"""

        super(FlopsWrapper_input_missin, self).__init__(*args, **kwargs)

        # VariableTrees
        self.add('Basic',  FlopsWrapper_input_missin_Basic())
        self.add('Climb',  FlopsWrapper_input_missin_Climb())
        self.add('Cruise',  FlopsWrapper_input_missin_Cruise())
        self.add('Descent',  FlopsWrapper_input_missin_Descent())
        self.add('Ground_Operations',  FlopsWrapper_input_missin_Ground_Operations())
        self.add('Reserve',  FlopsWrapper_input_missin_Reserve())
        self.add('Store_Drag',  FlopsWrapper_input_missin_Store_Drag())
        self.add('Turn_Segments',  FlopsWrapper_input_missin_Turn_Segments())
        self.add('User_Weights',  FlopsWrapper_input_missin_User_Weights())


class FlopsWrapper_input_fusein_Basic(VariableTree):
    """Container for input.fusein.Basic"""

    # OpenMDAO Public Variables
    fpitch = Float(0.0, units='inch', desc='Seat pitch for the first class passengers')
    nfabr = Int(0, desc='Number of first class passengers abreast')
    bpitch = Float(0.0, units='inch', desc='Seat pitch for business class passengers')
    nbabr = Int(0, desc='Number of business class passengers abreast')
    tpitch = Float(0.0, units='inch', desc='Seat pitch for tourist class passengers')
    ntabr = Int(0, desc='Number of tourist class passengers abreast')


class FlopsWrapper_input_fusein_BWB(VariableTree):
    """Container for input.fusein.BWB"""

    # OpenMDAO Public Variables
    osspan = Float(0.0, units='ft', desc='Outboard semispan (Default = ETAW(NETAW), required if ETAW(NETAW) is less than or equal to 1.0 and IFITE = 3 and NETAW > 1)\nThis variable is used if a detailed wing outboard panel (See Detailed Wing Data in Namelist $WTIN) is being added to a BWB fuselage.')
    tipchd = Float(0.0, units='ft', desc='Wing tip chord (Default = 0.06*Wing span)\nThis variable is used if the wing outer panel is defined as a trapezoid attached to the BWB cabin.')
    nesob = Int(0, desc='Wing eta station number for outboard side of body.  If this variable is greater than 1, the detailed wing definition is assumed to include the cabin.  Weight calculations for the outboard wing start at this eta station. (If = 0, the detailed outboard wing is added to the cabin as indicated above.)')
    acabin = Float(0.0, units='ft*ft', desc='Fixed area of passenger cabin for blended wing body transports (Default is internally computed based on passenger data)')
    xlw = Float(0.0, units='ft', desc='Fixed length of side wall.\nThis is the outboard wall of the passenger cabin and is used to define the outboard wing root chord.')
    xlwmin = Float(0.0, units='ft', desc='Minimum side wall length.  The typical value of 38.5 ft is based on a required maximum depth at the side wall of 8.25 ft divided by a fuselage thickness/chord ratio of 0.15 and 70 percent of the resulting wing root chord of 55 ft.')
    nbay = Int(0, desc='Fixed number of bays')
    nbaymx = Int(0, desc='Maximum number of bays')
    bayw = Float(0.0, units='ft', desc='Fixed bay width')
    baywmx = Float(0.0, units='ft', desc='Maximum bay width')
    swple = Float(45.0, units='deg', desc='Sweep angle of the leading edge of the passenger cabin')
    cratio = Float(0.0, desc='Fixed ratio of the centerline length to the cabin width (XLP/WF)')
    tcf = Float(0.0, desc='Fuselage thickness/chord ratio (Default = TCA, Namelist &CONFIN)')
    tcsob = Float(0.0, desc='Fuselage thickness/chord ratio at side of body (Default = TCF)')
    rspchd = Float(0.0, desc='Rear spar percent chord for BWB fuselage and wing (Default = 70 percent)')
    rspsob = Float(0.0, desc='Rear spar percent chord for BWB fuselage at side of body (Default = 70 percent)')


class FlopsWrapper_input_fusein(VariableTree):
    """Container for input.fusein"""

    def __init__(self, *args, **kwargs):
        """Constructor for the FlopsWrapper_input_fusein component"""

        super(FlopsWrapper_input_fusein, self).__init__(*args, **kwargs)

        # VariableTrees
        self.add('BWB',  FlopsWrapper_input_fusein_BWB())
        self.add('Basic',  FlopsWrapper_input_fusein_Basic())


class FlopsWrapper_input_engine_deck(VariableTree):
    """Container for input.engine_deck"""

    # OpenMDAO Public Variables
    engdek = Str(iotype='in')


class FlopsWrapper_input_engine_Other(VariableTree):
    """Container for input.engine.Other"""

    # OpenMDAO Public Variables
    hpcpr = Float(5.0, desc='Pressure ratio of the high pressure (third) compressor (Only used if there are three compressor components)')
    aburn = Bool(False, desc='True if there is an afterburner')
    dburn = Bool(False, desc='True if there is a duct burner (Separate flow turbofans only).  ABURN and DBURN cannot both be true.')
    effab = Float(0.85, desc='Afterburner/duct burner efficiency')
    tabmax = Float(3500.0, units='degR', desc='Maximum afterburner/duct burner temperature')
    ven = Bool(False, desc='True if the exhaust nozzle has a variable flow area.  The nozzle flow area is automatically allowed to vary for cases when the afterburner or duct burner is on.')
    costbl = Float(1.0, units='lb/s', desc='Customer high pressure compressor bleed')
    fanbl = Float(0.0, desc='Fan bleed fraction, only used for bypass engines')
    hpext = Float(200.0, units='hp', desc='Customer power extraction')
    wcool = Float(-1.0e-4, desc='Turbine cooling flow as a fraction of high pressure compressor mass flow. The cooling flow defaults to the value in the engine cycle definition file. If WCOOL is input greater than or equal to zero the default will be overridden.\nIf WCOOL > 1., the turbine cooling flow fraction required to bring the turbine inlet temperature down to WCOOL will be computed.')
    fhv = Float(18500.0, units='Btu/lb', desc='Fuel heating value')
    dtce = Float(0.0, units='degC', desc='Deviation from standard day temperature.  The deviation, as used in the cycle analysis module, is DTCE at sea level and varies to zero at ALC (see below). The design point is at standard temperature.')
    alc = Float(10000.0, units='ft', desc='The altitude at which DTCE (see above) becomes zero.')
    year = Float(1985.0, desc='Technology availability date used to estimate compressor polytropic efficiency')
    boat = Bool(False, desc='True to include boattail drag')
    ajmax = Float(0.0, units='ft*ft', desc='Nozzle reference area for boattail drag.  Used only if BOAT = true.  Default is the largest of\n1) 1.1 times the inlet capture area\n2) Nozzle exit area at the inlet design point\n3) Estimated engine frontal area\n4) Estimated nozzle entrance area\nor\nIf nacelle weight and geometry calculations are\nperformed (see NGINWT below) AJMAX is set to the\nnacelle cross-sectional area at the customer connect. \nor\nIf AJMAX is less than zero, the cruise design point\nnozzle exit area multiplied by the absolute value\nof AJMAX is used as the reference.')
    spill = Bool(False, desc='True to include spillage and lip drag in engine performance data')
    lip = Bool(False, desc='Compute inlet cowl lip drag.  Used only if SPILL = true')
    blmax = Float(-1.0, desc='Inlet bleed flow fraction of total flow at the inlet design point (Default = .016 * AMINDS**1.5).  Used only if SPILL = true')
    spldes = Float(0.01, desc='Inlet design spillage fraction.  Used only if SPILL = true')
    aminds = Float(0.0, desc='Inlet design Mach number (Default = XMMAX).  Used only if SPILL = true')
    alinds = Float(0.0, units='ft', desc='Inlet design altitude (Default = AMAX).  Used only if SPILL = true')
    etaprp = Float(0.84, desc='Maximum propeller efficiency (Turboprops only). The actual propeller efficiency is based on an internal schedule of efficiency versus Mach number with the maximum efficiency (ETAPRP) occurring at a Mach number of 0.80.  To use the Hamilton Standard Method set ETAPRP=1 and input the propeller characteristics as defined under ')
    shpowa = Float(60.0, units='hp/(lb/s)', desc='Design point shaft horsepower divided by the design point core airflow')
    cdtmax = Float(99999.0, units='degR', desc='Maximum allowable compressor discharge temperature')
    cdpmax = Float(99999.0, units='psi', desc='Maximum allowable compressor discharge pressure')
    vjmax = Float(99999.0, units='ft/s', desc='(IENG < 100) Maximum allowable jet velocity\n(IENG > 100) Propeller tip speed')
    stmin = Float(1.0, units='lb/lb/s', desc='Minimum allowable specific thrust')
    armax = Float(99999.0, desc='Maximum allowable ratio of the bypass area to the core area of a mixed flow turbofan')
    limcd = Enum(1, (0,1,2), desc='Switch to use the compressor discharge temperature and pressure limits only for optimization.', aliases=('Limit at cruise design Mach and altitude only for optimization', 'Limit at all points in envelope', 'Limit max. compressor discharge temp. everywhere'))


class FlopsWrapper_input_engine_Noise_Data(VariableTree):
    """Container for input.engine.Noise_Data"""

    # OpenMDAO Public Variables
    nprint = Enum(0, (-1,0,1,2), desc='Noise data print control', aliases=('Print compressor operating line', 'No print', 'Print to ANOPP', 'Print to FOOTPR'))
    #ivat = Enum(0, (0,1), desc='Flag for variable exit area low pressure turbine.  Used only for estimating LPT exit area when NPRINT=1', aliases=('Fixed', 'Variable'))
    jet = Enum(-1, (-1,0,1,2,3,4,5,6), desc='FOOTPR input data generation control', aliases=('No noise data', 'No jet noise', 'Stone/Clark', 'Kresja', 'Stone ALLJET', 'Stone JET181', 'GE M*S', 'SAE A-21'))
    ftmach = Float(0.0, desc='Mach number to calculate FOOTPR input data')
    ftalt = Float(0.0, desc='Altitude to calculate FOOTPR input data')


class FlopsWrapper_input_engine_IC_Engine(VariableTree):
    """Container for input.engine.IC_Engine"""

    # OpenMDAO Public Variables
    ncyl = Int(4, desc='Number of cylinders')
    deshp = Float(180.0, units='hp', desc='Baseline engine power')
    alcrit = Float(0.0, units='ft', desc='Critical turbocharger altitude.  The altitude to which turbocharged IC engines are able to maintain DESHP')
    sfcmax = Float(0.52, units='lb/h/hp', desc='Brake specific fuel consumption at maximum power')
    sfcmin = Float(0.4164, units='lb/h/hp', desc='Minimum brake specific fuel consumption or SFC')
    pwrmin = Float(0.65, desc='Fraction of maximum power where SFCMIN occurs. If NRPM > 0 and PWRMIN > 1 then PWRMIN is the rotational speed where SFCMIN occurs (recommend PWRMIN > 1 if SFCMIN is less than about 0.4')
    engspd = Float(2700.0, units='1/min', desc='Maximum engine crankshaft speed')
    prpspd = Float(2700.0, units='1/min', desc='Maximum propeller shaft speed')
    iwc = Enum(0, (0,1), desc='Cooling system', aliases=('Air cooled', 'Water cooled'))
    ecid = Float(361.0, units='inch*inch*inch', desc='Engine displacement')
    ecr = Float(8.5, desc='Engine compression ratio')
    eht = Float(19.96, units='inch', desc='Engine envelope height')
    ewid = Float(33.37, units='inch', desc='Engine envelope width')
    elen = Float(31.83, units='inch', desc='Engine envelope length')
    ntyp = Enum(2, (1,2,3,4,5,6), desc='Propeller type indicator', aliases=('Fixed pitch', 'Variable pitch', 'Variable pitch + full feathering', 'Variable pitch + full feathering + deicing', 'Variable pitch + full feathering + deicing w/reverse', 'Ducted fan'))
    af = Float(87.6, desc='Activity factor')
    cli = Float(0.569, desc='Integrated design lift coefficient')
    blang = Float(20.0, units='deg', desc='Blade angle for fixed pitch propeller')
    dprop = Float(6.375, units='ft', desc='Propeller diameter')
    nblade = Int(0, desc='Number of blades')
    gbloss = Float(0.02, desc='Gearbox losses, fraction. If PRPSPD = ENGSPD, there are no losses.')
    arrpm = Array(dtype=numpy_float64, units='rpm', desc='Rotational speed (descending order)')
    arpwr = Array(dtype=numpy_float64, units='hp', desc='Engine shaft power at ARRPM(I)')
    arful = Array(dtype=numpy_float64, desc='Engine fuel requirements at ARRPM(I) (Required only if LFUUN is not equal to zero)')
    lfuun = Enum(0, (0,1,2,3), desc='Fuel input type indicator', aliases=('Fuel flows are computed from SFCMAX SFCMIN and PWRMIN', 'Brake specific fuel consumption values are input in ARFUL', 'Actual fuel flows are input in ARFUL (lb/hr)', 'Actual fuel flows are input in ARFUL (gal/hr)'))
    feng = Float(1.0, desc='Scale factor on engine weight')
    fprop = Float(1.0, desc='Scale factor on propeller weight')
    fgbox = Float(1.0, desc='Scale factor on gear box weight')


class FlopsWrapper_input_engine_Engine_Weight(VariableTree):
    """Container for input.engine.Engine_Weight"""

    # OpenMDAO Public Variables
    nginwt = Enum(0, (-4,-3,-2,-1,0,1,2,3,4,5), desc='Switch for engine weight calculations.   Use the negative value to calculate the weight for the initial design and then scale engine weights and dimensions with airflow.  Zero or a negative value should always be used during optimization with engine cycle design variables.  (IENG > 100 options in parentheses)', aliases=('-Engine + inlet + nacelle + nozzle', '-Engine + inlet + nacelle', '-Engine and inlet', '-Engine only', 'None', 'Engine only (Total prop. system)', 'Engine and inlet (Propeller)', 'Engine + inlet + nacelle (Propeller + cowl + mounts)', 'Engine + inlet + nacelle + nozzle ( Propeller + cowl + mounts + exhaust)', '(Propeller + cowl + mounts + exhaust + alternator)'))
    iwtprt = Enum(1, (0,1,2,3,4), desc='Printout control for engine weight calculations.  Printout is on file OFILE.', aliases=('No output', 'Print component weights and dimensions', 'Print component design details', 'Plus initial and final optimization data', 'Print component details at each iteration'))
    iwtplt = Enum(0, (-4,-3,-2,-1,0,1,2,3,4), desc='PostScript plot control for engine (and nacelle) schematics on file PLTFIL.  If the negative value is input, only the final design will be plotted.')
    gratio = Float(1.0, desc='Ratio of the RPM of the low pressure compressor to the RPM of the connected fan')
    utip1 = Float(0.0, units='ft/s', desc='Tip speed of the first compressor (or fan) in the flow.  Default is based on YEAR, engine type, and other design considerations.')
    rh2t1 = Float(0.0, desc='Hub to tip radius ratio of the first compressor (or fan) in the flow.  Default is based on YEAR, engine type, and other design considerations.')
    igvw = Enum(0, (-2,-1,0,1,2), desc='Flag for compressor inlet guide vanes', aliases=('Variable-no fan IGV', 'Fixed-no fan IGV', 'None', 'Fixed', 'Variable'))
    trbrpm = Float(0.0, units='rpm', desc='The rotational speed of any free turbine.  TRBAN2 is used to set the free turbine rotational speed if TRBRPM is not input. TRBRPM overrides TRBAN2.')
    trban2 = Float(0.0, units='(inch*inch)/(min*min)', desc='Maximum allowable AN**2 for turbine components.  The input value is the actual maximum divided by 10**10.  AN**2 is the flow area multiplied by the rotational speed squared.  The default is based on year.')
    trbstr = Float(15000.0, units='psi', desc='Turbine usable stress lower limit.  Normally when component weights are predicted, the usable stress is a function of operating conditions.  For turbine components, this can be unusually low because cooling effects are not accounted for.')
    cmpan2 = Float(0.0, units='(inch*inch)/(min*min)', desc='Maximum allowable AN**2 for compressor components.  The input value is the actual maximum divided by 10**10.  AN**2 is the flow area multiplied by the rotational speed squared.  The default is based on year.')
    cmpstr = Float(25000.0, units='psi', desc='Requested compressor usable stress.  This forces a change in compressor material when the current (lower temperature) material starts to run out of strength as temperature increases.')
    vjpnlt = Float(0.0, units='lb', desc='Weight penalty factor for a suppressor to reduce the core jet velocity to 1500 ft/sec')
    wtebu = Float(0.2, desc='Fraction for weight of engine build up unit (pylon, mounting hardware, etc)')
    wtcon = Float(0.05, desc='Fraction for weight of engine controls')


class FlopsWrapper_input_engine_Design_Point(VariableTree):
    """Container for input.engine.Design_Point"""

    # OpenMDAO Public Variables
    desfn = Float(0.0, units='lb', desc='Engine design point net dry thrust (Default = THRUST, Namelist &CONFIN).  Do not use the default for afterburning engines since THRUST is the maximum wet thrust rating.  The maximum wet (afterburning) thrust for the generated engine is transferred back to THRSO for scaling with THRUST.')
    xmdes = Float(-9999.0, desc='Engine optimization point Mach number (Default = VCMN, Namelist &CONFIN).  XMDES and XADES are used for propulsion only analyses (IANAL = 4).')
    xades = Float(-9999.0, units='ft', desc='Engine optimization point altitude (Default = CH, Namelist &CONFIN).  If XADES < 0., it is interpreted as the negative of the design point dynamic pressure (psf), and the altitude is back-calculated with a minimum of 0.')
    oprdes = Float(25.0, desc='Overall pressure ratio')
    fprdes = Float(1.5, desc='Fan pressure ratio (turbofans only)')
    bprdes = Float(0.0, desc='Bypass ratio (Turbofans only, Default is computed based on OPRDES, FPRDES, TTRDES, XMDES and ALDES).  If BPRDES < -1, then the bypass ratio is computed such that the ratio of the fan to core jet velocities equals the absolute value of BPRDES.  For turbine bypass engines, BPRDES must be input and is defined as the fraction of compressor exit airflow that is bypassed around the main burner and the turbine.  If both EBPR and BPRDES are zero, the optimum bypass ratio is computed at the design Mach number and altitude (XMDES, XADES).')
    tetdes = Float(2500.0, units='degR', desc='Engine design point turbine entry temperature')
    ttrdes = Float(1.0, desc='Engine throttle ratio defined as the ratio of the maximum allowable turbine inlet temperature divided by the design point turbine inlet temperature.  If TTRDES is greater than TETDES, it is assumed to be the maximum allowable turbine inlet temperature.')


class FlopsWrapper_input_engine_Basic(VariableTree):
    """Container for input.engine.Basic"""

    # OpenMDAO Public Variables
    ieng = Enum(1, (0,1,2,3,4,5,6,7,8,9,101), desc='Engine cycle definition input file indicator', aliases=('User-defined', 'Turbojet', 'Separate flow turbofan w/ 2 compressors', 'Mixed flow turbofan w/ 2 compressors', 'Turboprop', 'Turbine bypass', 'Separate flow turofan w/ 3 compressors', 'Mixed flow turbofan w/ 3 compressors', '3-spool separate flow turbofan w/ 3 compressors', '2-spool turbojet', 'IC engine'))
    iprint = Int(1, desc='Engine cycle analysis printout control.  Printout is on file OFILE')
    gendek = Bool(False, desc='Engine data will be saved on the file designated by EOFILE as an Engine Deck for future use')
    ithrot = Enum(1, (0,1,2), desc='Controls frequency of part power data generation', aliases=('All Mach-altitude combos', 'Max. altitude for each Mach', 'Max. altitude for max. Mach'))
    npab = Int(0, desc='Maximum number of afterburning throttle settings for each Mach-altitude combination')
    npdry = Int(15, desc='Maximum number of dry (non-afterburning) throttle settings')
    xidle = Float(0.05, desc='Fraction of maximum dry thrust used as a cutoff for part power throttle settings')
    nitmax = Int(50, desc='Maximum iterations per point')
    xmmax = Float(-1.0, desc='Max Mach number (Default = VCMN, Namelist &CONFIN)')
    amax = Float(-1.0, units='ft', desc='Max altitude (Default = CH, Namelist &CONFIN)')
    xminc = Float(0.2, desc='Mach number increment (Default = .2)')
    ainc = Float(5000.0, units='ft', desc='Altitude increment (Default = 5000.)')
    qmin = Float(150.0, units='psf', desc='Minimum dynamic pressure')
    qmax = Float(1200.0, units='psf', desc='Maximum dynamic pressure')


class FlopsWrapper_input_engine(VariableTree):
    """Container for input.engine"""

    # OpenMDAO Public Variables
    ifile = Str(desc='Name of cycle definition input file.  Used only if IENG = 0.')
    tfile = Str('ENGTAB', desc='Name of the file containing component map tables.')

    def __init__(self, *args, **kwargs):
        """Constructor for the FlopsWrapper_input_engine component"""

        super(FlopsWrapper_input_engine, self).__init__(*args, **kwargs)

        # VariableTrees
        self.add('Basic',  FlopsWrapper_input_engine_Basic())
        self.add('Design_Point',  FlopsWrapper_input_engine_Design_Point())
        self.add('Engine_Weight',  FlopsWrapper_input_engine_Engine_Weight())
        self.add('IC_Engine',  FlopsWrapper_input_engine_IC_Engine())
        self.add('Noise_Data',  FlopsWrapper_input_engine_Noise_Data())
        self.add('Other',  FlopsWrapper_input_engine_Other())


class FlopsWrapper_input_engdin_Special_Options(VariableTree):
    """Container for input.engdin.Special_Options"""

    # OpenMDAO Public Variables
    dffac = Float(0.0, desc='Fuel flow scaling constant term.\nThe engine fuel flow scale factor for ENGSKAL = THRUST/THRSO is\nENGSKAL*[1. + DFFAC + FFFAC*(1. - ENGSKAL)]')
    fffac = Float(0.0, desc='Fuel flow scaling linear term.\nThe engine fuel flow scale factor for ENGSKAL = THRUST/THRSO is\nENGSKAL*[1. + DFFAC + FFFAC*(1. - ENGSKAL)]')
    emach = Array(dtype=numpy_float64, desc='Array of Mach numbers in descending order at which engine data are to be generated (Default computed internally, Do not zero fill)')
    alt = Array(zeros(shape=(0,0)), dtype=numpy_float64, units='ft', desc='Arrays of altitudes in descending order, one set for each Mach number, at which engine data are to be generated (Default computed internally, do not zero fill).  Altitudes and numbers of altitudes do not have to be consistent between Mach numbers.')
    insdrg = Enum(0, (0,1,2,3), desc='Nozzle installation drag scaling switch', aliases=('No drag scaling', 'Scale with A10', 'Calculate using A10', 'Calculate for Cd=0 at A9=A9ref'))
    nab = Int(6969, desc='Table number in CDFILE to be used for afterbody drag')
    nabref = Int(6969, desc='Table number in CDFILE to be used for reference afterbody drag')
    a10 = Float(0.0, units='inch*inch', desc='Maximum nozzle area (Required if INSDRG > 0)')
    a10ref = Float(0.0, units='inch*inch', desc='Reference maximum nozzle area (Required if INSDRG > 0)')
    a9ref = Float(0.0, units='inch*inch', desc='Reference nozzle exit area (Required if INSDRG = 3)')
    xnoz = Float(0.0, units='inch', desc='Nozzle length (Required if INSDRG > 0)')
    xnref = Float(0.0, units='inch', desc='Reference nozzle length (Required if INSDRG > 0)')
    rcrv = Float(-1.0, desc='Nozzle radius of curvature parameter (Triggers special nozzle drag option)')


class FlopsWrapper_input_engdin_Basic(VariableTree):
    """Container for input.engdin.Basic"""

    # OpenMDAO Public Variables
    ngprt = Enum(1, (0,1,2), desc='Print engine data tables', aliases=('No printout', 'Print tables', 'Print sorted tables'))
    igenen = Enum(0, (-3,-2,-1,0,1), desc='Switch indicating source of Engine Deck', aliases=('Response surfaces', 'External file (horsepower/rpm/fuel flow', 'External file (thrust/fuel flow)', 'Follows namelist &ENGDIN', 'Engine deck to be generated'))
    extfac = Float(1.0, desc='Slope factor for extrapolating engine fuel flows for thrust levels above the maximum for that Mach number and altitude')
    fffsub = Float(1.0, desc='Fuel flow factor for all subsonic engine points')
    fffsup = Float(1.0, desc='Fuel flow factor for all supersonic engine points')
    idle = Int(0, desc='> 0, Flight idle data will be internally generated with zero thrust and an extrapolated fuel flow.  The fuel flow must be at least FIDMIN times the fuel flow at power setting number IDLE and no more than FIDMAX times the fuel flow at power setting number IDLE.  If NONEG (below) = 0 and negative thrusts exist, an idle power setting is not generated.\n= 0, The lowest input power setting is assumed to be flight idle (Not recommended.  Results will be more consistent with IDLE > 0)')
    noneg = Enum(0, (1,0), desc='Option for using points in the Engine Deck with negative thrust', aliases=('Ignore', 'Use all points'))
    fidmin = Float(0.08, desc='Minimum fraction of the fuel flow at power setting number IDLE for generated flight idle fuel flows')
    fidmax = Float(1.0, desc='Maximum fraction of the fuel flow at power setting number IDLE for generated flight idle fuel flows')
    ixtrap = Int(1, desc='Option for extrapolation of engine data beyond altitudes provided in input data, which may result in radically improved SFC')
    ifill = Int(2, desc='Option for filling in part power data\n=0, No part power data will be generated\n> 0, Part power cruise data will be filled in for Mach-altitude points for which IFILL (or fewer) thrust levels have been input\nFor NPCODE > 1, data will be filled in for each specified power code that is not input for each Mach-altitude point.')
    maxcr = Int(2, desc='Maximum power setting used for cruise')
    nox = Enum(0, (0,1,2,3), desc='Option for NOx emissions data.  If IGENEN=-2, NOx emissions data are replaced with engine shaft speed, rpm', aliases=('Do not use', 'Indices in engine deck or generated', 'Emissions lb/hr in engine deck', 'Another parameter in engine deck'))
    pcode = Array(dtype=numpy_float64, desc='Power codes to be used in sorting the Engine Deck.  Values correspond to thrust levels in descending order, i.e., climb, maximum continuous, part power cruise settings, and flight idle.  Actual values are arbitrary (they are just used as labels), but only points in the Engine Deck with corresponding values for PC will be used.')
    boost = Float(0.0, desc='> 0., Scale factor for boost engine to be added to baseline engine for takeoff and climb.  Climb thrust of the boost engine in the Engine Deck must be artificially increased by 100,000.\n= 0., No boost engine')
    igeo = Enum(0, (0,1), desc='Engine deck altitude type', aliases=('Geometric', 'Geopotential-will be converted'))


class FlopsWrapper_input_engdin(VariableTree):
    """Container for input.engdin"""

    # OpenMDAO Public Variables
    #cdfile = File(iotype='in')

    # Special addition for analysis runs where we aren't connected to NPSS. 
    eifile = Str(desc="Engine deck filename")

    def __init__(self, *args, **kwargs):
        """Constructor for the FlopsWrapper_input_engdin component"""

        super(FlopsWrapper_input_engdin, self).__init__(*args, **kwargs)

        # VariableTrees
        self.add('Basic',  FlopsWrapper_input_engdin_Basic())
        self.add('Special_Options',  FlopsWrapper_input_engdin_Special_Options())


class FlopsWrapper_input_costin_Mission_Performance(VariableTree):
    """Container for input.costin.Mission_Performance"""

    # OpenMDAO Public Variables
    desmch = Float(0.0, desc='Design Mach number (Default = VCMN, Namelist &CONFIN)')
    dprsmx = Float(0.0, units='psf', desc='Maximum dynamic pressure (Default = 460. * DESMCH)')
    veloc = Float(0.0, units='mi/h', desc='Cruise velocity (Default = 660. * DESMCH)')
    blockf = Float(0.9, units='lb', desc='Block fuel, or fraction of aircraft fuel capacity  (Default = 0.90 * (FULWMX+FULFMX), Namelist &WTIN)')
    blockt = Float(0.0, units='h', desc='Block time (Default = DESRNG/VELOC + 0.65)')


class FlopsWrapper_input_costin_Cost_Technology(VariableTree):
    """Container for input.costin.Cost_Technology"""

    # OpenMDAO Public Variables
    fafrd = Float(1.0, desc='Technology factor on Airframe R&D')
    fenrd = Float(1.0, desc='Technology factor on Engine R&D')
    fmac = Float(1.0, desc='Technology factor on Air conditioning')
    fmai = Float(1.0, desc='Technology factor on Anti-icing')
    fmapu = Float(1.0, desc='Technology factor on Auxiliary power unit')
    fmav = Float(1.0, desc='Technology factor on Avionics')
    fmbody = Float(1.0, desc='Technology factor on Fuselage')
    fmcomp = Float(1.0, desc='Technology factor on Composite materials (applied to the wing, tails, fuselage, and nacelles)')
    fmel = Float(1.0, desc='Technology factor on Electrical systems')
    fmeng = Float(1.0, desc='Technology factor on Engine')
    fmensy = Float(1.0, desc='Technology factor on Engine systems')
    fmfcs = Float(1.0, desc='Technology factor on Surface controls')
    fmfeq = Float(1.0, desc='Technology factor on Furnishings and equipment')
    fmfusy = Float(1.0, desc='Technology factor on Fuel systems')
    fmgear = Float(1.0, desc='Technology factor on Landing gear')
    fmhyd = Float(1.0, desc='Technology factor on Hydraulic systems')
    fmins = Float(1.0, desc='Technology factor on Instruments')
    fmnac = Float(1.0, desc='Technology factor on Nacelles')
    fmpnm = Float(1.0, desc='Technology factor on Pneumatics')
    fmtail = Float(1.0, desc='Technology factor on Tail')
    fmtrv = Float(1.0, desc='Technology factor on Thrust reversers')
    fmwing = Float(1.0, desc='Technology factor on Wing')
    foac = Float(1.0, desc='Technology factor on Air conditioning')
    foai = Float(1.0, desc='Technology factor on Anti-icing')
    foapu = Float(1.0, desc='Technology factor on Auxiliary power unit')
    foav = Float(1.0, desc='Technology factor on Avionics')
    fobody = Float(1.0, desc='Technology factor on Fuselage')
    focomp = Float(1.0, desc='Technology factor on Composite materials')
    foel = Float(1.0, desc='Technology factor on Electrical systems')
    fofcs = Float(1.0, desc='Technology factor on Flight control system')
    fofeq = Float(1.0, desc='Technology factor on Furnishings and equipment')
    fofusy = Float(1.0, desc='Technology factor on Fuel systems')
    fogear = Float(1.0, desc='Technology factor on Landing gear')
    fohyd = Float(1.0, desc='Technology factor on Hydraulic systems')
    foins = Float(1.0, desc='Technology factor on Instruments')
    fonac = Float(1.0, desc='Technology factor on Nacelles')
    fopnm = Float(1.0, desc='Technology factor on Pneumatics')
    foprop = Float(1.0, desc='Technology factor on Propulsion system')
    fowing = Float(1.0, desc='Technology factor on Wing')
    feacsr = Float(1.0, desc='Technology factor on Aircraft servicing')
    fecfee = Float(1.0, desc='Technology factor on Aircraft control fee')
    fecrw = Float(1.0, desc='Technology factor on Flight crew')
    fedep = Float(1.0, desc='Technology factor on Depreciation')
    feflta = Float(1.0, desc='Technology factor on Flight attendants')
    feins = Float(1.0, desc='Technology factor on Insurance')
    felabr = Float(1.0, desc='Technology factor on R&D labor rate')
    feldfe = Float(1.0, desc='Technology factor on Landing fee')
    femain = Float(1.0, desc='Technology factor on Maintenance hours')


class FlopsWrapper_input_costin_Basic(VariableTree):
    """Container for input.costin.Basic"""

    # OpenMDAO Public Variables
    ac = Float(350.0, units='lb/min', desc='Airconditioning total pack air flow')
    apuflw = Float(400.0, units='lb/min', desc='Auxiliary power unit flow rate')
    apushp = Float(170.0, units='hp', desc='Auxiliary power unit shaft horsepower')
    depper = Float(14.0, units='year', desc='Depreciation period')
    devst = Float(1980.0, units='year', desc='Development start time')
    dlbur = Float(2.0, desc='Direct labor burden factor')
    dyear = Int(1986, desc='Desired year for dollar calculations')
    epr = Float(20.0, desc='Engine pressure ratio at sea level static')
    fafmsp = Float(0.1, desc='Spares factor for production airframes')
    fare = Float(0.0, units='USD/pax/mi', desc='Fare (Triggers calculation of return on investment)')
    fengsp = Float(0.3, desc='Spares factor for production engines')
    fppft = Float(0.5, desc='Spares factor for prototype and flight test engines')
    fuelpr = Float(0.5, units='USD/galUS', desc='Fuel price')
    hydgpm = Float(150.0, desc='Gallon per minute flow of hydraulic pumps')
    iacous = Enum(0, (0,1), desc='Acoustic treatment in nacelle', aliases=('No', 'Yes'))
    ibody = Enum(0, (0,1), desc='Body type indicator', aliases=('Narrow', 'Wide'))
    icirc = Enum(1, (1,2), desc='Circuit indicator - fire detection', aliases=('Single', 'Dual'))
    icorev = Enum(1, (0,1), desc='Thrust reverser', aliases=('No core reverser', 'Core reverser'))
    icostp = Enum(1, (1,2,3,4,5), desc='Type of cost calculation desired', aliases=('Life cycle cost (LCC)', 'Acquisition cost', 'Direct operating cost (DOC)', 'Indirect operating cost (IOC)', 'Operating cost only (DOC + IOC - Depreciation)'))
    idom = Enum(1, (1,2), desc='Operation type indicator', aliases=('Domestic', 'International'))
    imux = Enum(0, (0,1), desc='Multiplex indicator', aliases=('No multiplex', 'Multiplex'))
    inozz = Enum(1, (1,2,3,4,5), desc='Nozzle type indicator', aliases=('Translating sleeve', 'Simple target w/ separate flow nozzle', 'Simple target w/ mixed flow nozzle', 'Separate flow exhaust w/o thrust reverser', 'Short duct w/o thrust reverser'))
    ipflag = Enum(1, (0,1), desc='Print controller for Cost Module', aliases=('Print major elements', 'Print details'))
    irad = Enum(1, (0,1), desc='Indicator to include research and development', aliases=('Ignore R&D costs', 'Include R&D costs'))
    irange = Enum(1, (0,1,2), desc='Range indicator', aliases=('Short', 'Medium', 'Long'))
    ispool = Enum(0, (0,1), desc='Auxiliary power unit complexity indicator', aliases=('Single spool fixed vane', 'Double spool variable vane APU'))
    itran = Enum(0, (0,1), desc='Cargo/baggage transfer operation indicator', aliases=('No transfer', 'Transfer'))
    iwind = Enum(0, (0,1), desc='Windshield type indicator', aliases=('Flat', 'Curved'))
    kva = Float(200.0, desc='KVA rating of full-time generators')
    lf = Float(55.0, desc='Passenger load factor')
    life = Float(14.0, desc='Number of years for Life Cycle Cost calculation')
    napu = Int(1, desc='Number of auxiliary power units')
    nchan = Enum(1, (1,2,3), desc='Number of autopilot channels')
    nfltst = Int(2, desc='Number of flight test aircraft')
    ngen = Enum(3, (3,4), desc='Number of inflight operated generators')
    nins = Int(0, desc='Number of inertial navigation systems')
    npod = Int(4, desc='Number of podded engines')
    nprotp = Int(2, desc='Number of prototype aircraft')
    pctfc = Float(10.0, desc='Percent of seats for first class')
    plmqt = Float(1984.0, units='year', desc='Planned MQT (150-hour Model Qualification Test or FAA certification)')
    prorat = Float(15.0, desc='Manufacturers')
    prproc = Float(0.0, desc='Prior number of engines procured')
    q = Float(100.0, desc='Airframe production quantities')
    resid = Float(2.0, desc='Residual value at end of lifetime')
    roi = Float(10.0, desc='Return on investment (Triggers calculation of required fare)')
    sfc = Float(0.6, units='lb/h/lb', desc='Engine specific fuel consumption')
    taxrat = Float(0.33, desc='Corporate tax rate for ROI calculations')
    temp = Float(1800.0, units='degF', desc='Maximum turbine inlet temperature')


class FlopsWrapper_input_costin(VariableTree):
    """Container for input.costin"""

    def __init__(self, *args, **kwargs):
        """Constructor for the FlopsWrapper_input_costin component"""

        super(FlopsWrapper_input_costin, self).__init__(*args, **kwargs)

        # VariableTrees
        self.add('Basic',  FlopsWrapper_input_costin_Basic())
        self.add('Cost_Technology',  FlopsWrapper_input_costin_Cost_Technology())
        self.add('Mission_Performance',  FlopsWrapper_input_costin_Mission_Performance())


class FlopsWrapper_input_confin_Objective(VariableTree):
    """Container for input.confin.Objective"""

    # OpenMDAO Public Variables
    ofg = Float(0.0, desc='Objective function weighting factor for gross weight \nThe function that is minimized is\n \n OBJ = OFG*GW \n + OFF*Fuel \n + OFM*VCMN*(Lift/Drag) \n + OFR*Range + OFC*Cost \n + OSFC*SFC \n + OFNOX*NOx \n + OFNF*(Flyover Noise) \n + OFNS*(Sideline Noise) \n + OFNFOM*(Noise Figure of Merit) \n + OFH*(Hold Time for Segment NHOLD)')
    off = Float(1.0, desc='Objective function weighting factor for mission fuel \nThe function that is minimized is\n \n OBJ = OFG*GW \n + OFF*Fuel \n + OFM*VCMN*(Lift/Drag) \n + OFR*Range + OFC*Cost \n + OSFC*SFC \n + OFNOX*NOx \n + OFNF*(Flyover Noise) \n + OFNS*(Sideline Noise) \n + OFNFOM*(Noise Figure of Merit) \n + OFH*(Hold Time for Segment NHOLD)')
    ofm = Float(0.0, desc='Objective function weighting factor for Mach*(L/D), should be negative to maximize \nThe function that is minimized is\n \n OBJ = OFG*GW \n + OFF*Fuel \n + OFM*VCMN*(Lift/Drag) \n + OFR*Range + OFC*Cost \n + OSFC*SFC \n + OFNOX*NOx \n + OFNF*(Flyover Noise) \n + OFNS*(Sideline Noise) \n + OFNFOM*(Noise Figure of Merit) \n + OFH*(Hold Time for Segment NHOLD)')
    ofr = Float(0.0, desc='Objective function weighting factor for Range, should be negative to maximize. \nThe function that is minimized is\n \n OBJ = OFG*GW \n + OFF*Fuel \n + OFM*VCMN*(Lift/Drag) \n + OFR*Range + OFC*Cost \n + OSFC*SFC \n + OFNOX*NOx \n + OFNF*(Flyover Noise) \n + OFNS*(Sideline Noise) \n + OFNFOM*(Noise Figure of Merit) \n + OFH*(Hold Time for Segment NHOLD)')
    ofc = Float(0.0, desc='Objective function weighting factor for Cost \nThe function that is minimized is\n \n OBJ = OFG*GW \n + OFF*Fuel \n + OFM*VCMN*(Lift/Drag) \n + OFR*Range + OFC*Cost \n + OSFC*SFC \n + OFNOX*NOx \n + OFNF*(Flyover Noise) \n + OFNS*(Sideline Noise) \n + OFNFOM*(Noise Figure of Merit) \n + OFH*(Hold Time for Segment NHOLD)')
    osfc = Float(0.0, desc='Objective function weighting factor for Specific Fuel Consumption at the engine design point.  Generally used only for engine design cases (IANAL = 4). \nThe function that is minimized is\n \n OBJ = OFG*GW \n + OFF*Fuel \n + OFM*VCMN*(Lift/Drag) \n + OFR*Range + OFC*Cost \n + OSFC*SFC \n + OFNOX*NOx \n + OFNF*(Flyover Noise) \n + OFNS*(Sideline Noise) \n + OFNFOM*(Noise Figure of Merit) \n + OFH*(Hold Time for Segment NHOLD)')
    ofnox = Float(0.0, desc='Objective function weighting factor for NOx emissions \nThe function that is minimized is\n \n OBJ = OFG*GW \n + OFF*Fuel \n + OFM*VCMN*(Lift/Drag) \n + OFR*Range + OFC*Cost \n + OSFC*SFC \n + OFNOX*NOx \n + OFNF*(Flyover Noise) \n + OFNS*(Sideline Noise) \n + OFNFOM*(Noise Figure of Merit) \n + OFH*(Hold Time for Segment NHOLD)')
    ofnf = Float(0.0, desc='Objective function weighting factor for flyover noise (used primarily for contour plots) \nThe function that is minimized is\n \n OBJ = OFG*GW \n + OFF*Fuel \n + OFM*VCMN*(Lift/Drag) \n + OFR*Range + OFC*Cost \n + OSFC*SFC \n + OFNOX*NOx \n + OFNF*(Flyover Noise) \n + OFNS*(Sideline Noise) \n + OFNFOM*(Noise Figure of Merit) \n + OFH*(Hold Time for Segment NHOLD)')
    ofns = Float(0.0, desc='Objective function weighting factor for sideline noise (used primarily for contour plots) \nThe function that is minimized is\n \n OBJ = OFG*GW \n + OFF*Fuel \n + OFM*VCMN*(Lift/Drag) \n + OFR*Range + OFC*Cost \n + OSFC*SFC \n + OFNOX*NOx \n + OFNF*(Flyover Noise) \n + OFNS*(Sideline Noise) \n + OFNFOM*(Noise Figure of Merit) \n + OFH*(Hold Time for Segment NHOLD)')
    ofnfom = Float(0.0, desc='Objective function weighting factor for noise figure of merit \nThe function that is minimized is\n \n OBJ = OFG*GW \n + OFF*Fuel \n + OFM*VCMN*(Lift/Drag) \n + OFR*Range + OFC*Cost \n + OSFC*SFC \n + OFNOX*NOx \n + OFNF*(Flyover Noise) \n + OFNS*(Sideline Noise) \n + OFNFOM*(Noise Figure of Merit) \n + OFH*(Hold Time for Segment NHOLD)')
    oarea = Float(0.0, desc='Objective function weighting factor for area of noise footprint (not implemented) \nThe function that is minimized is\n \n OBJ = OFG*GW \n + OFF*Fuel \n + OFM*VCMN*(Lift/Drag) \n + OFR*Range + OFC*Cost \n + OSFC*SFC \n + OFNOX*NOx \n + OFNF*(Flyover Noise) \n + OFNS*(Sideline Noise) \n + OFNFOM*(Noise Figure of Merit) \n + OFH*(Hold Time for Segment NHOLD)')
    ofh = Float(0.0, desc='Objective function weighting factor for hold time for segment NHOLD (See Namelist &MISSIN) \nThe function that is minimized is\n \n OBJ = OFG*GW \n + OFF*Fuel \n + OFM*VCMN*(Lift/Drag) \n + OFR*Range + OFC*Cost \n + OSFC*SFC \n + OFNOX*NOx \n + OFNF*(Flyover Noise) \n + OFNS*(Sideline Noise) \n + OFNFOM*(Noise Figure of Merit) \n + OFH*(Hold Time for Segment NHOLD)')


class FlopsWrapper_input_confin_Design_Variables(VariableTree):
    """Container for input.confin.Design_Variables"""

    # OpenMDAO Public Variables
    gw = Array(dtype=numpy_float64, units='lb', desc='GW(0)=Ramp weight (Required.  If IRW = 1, a good initial guess must be input.)\nGW(1)=Activity status, active if > 0\nGW(2)=Lower bound\nGW(3)=Upper bound\nGW(4)=Optimization scale factor')
    ar = Array(dtype=numpy_float64, desc='AR(0)=Wing aspect ratio\nAR(1)=Activity status, active if > 0\nAR(2)=Lower bound\nAR(3)=Upper bound\nAR(4)=Optimization scale factor')
    thrust = Array(dtype=numpy_float64, units='lb', desc='THRUST(0)=Maximum rated thrust per engine, or thrust-weight ratio if TWR = -1.\nTHRUST(1)=Activity status, active if > 0\nTHRUST(2)=Lower bound\nTHRUST(3)=Upper bound\nTHRUST(4)=Optimization scale factor')
    sw = Array(dtype=numpy_float64, units='ft*ft', desc='SW(0)=Reference wing area, or wing loading if WSR = -1.\nSW(1)=Activity status, active if > 0\nSW(2)=Lower bound\nSW(3)=Upper bound\nSW(4)=Optimization scale factor')
    tr = Array(dtype=numpy_float64, desc='TR(0)=Taper ratio of the wing (Required)\nTR(1)=Activity status, active if > 0\nTR(2)=Lower bound\nTR(3)=Upper bound\nTR(4)=Optimization scale factor')
    sweep = Array(dtype=numpy_float64, units='deg', desc='SWEEP(0)=Quarter-chord sweep angle of the wing (Required)\nSWEEP(1)=Activity status, active if > 0\nSWEEP(2)=Lower bound\nSWEEP(3)=Upper bound\nSWEEP(4)=Optimization scale factor')
    tca = Array(dtype=numpy_float64, desc='TCA(0)=Wing thickness-chord ratio (weighted average) (Required)\nTCA(1)=Activity status, active if > 0\nTCA(2)=Lower bound\nTCA(3)=Upper bound\nTCA(4)=Optimization scale factor')
    vcmn = Array(dtype=numpy_float64, desc='VCMN(0)=Cruise Mach number (Required)\nVCMN(1)=Activity status, active if > 0\nVCMN(2)=Lower bound\nVCMN(3)=Upper bound\nVCMN(4)=Optimization scale factor')
    ch = Array(dtype=numpy_float64, units='ft', desc='CH(0)=Maximum cruise altitude (Required)\nCH(1)=Activity status, active if > 0\nCH(2)=Lower bound\nCH(3)=Upper bound\nCH(4)=Optimization scale factor')
    varth = Array(dtype=numpy_float64, desc='VARTH(0)=Thrust derating factor for takeoff noise Fraction of full thrust used in takeoff\nVARTH(1)=Activity status, active if > 0\nVARTH(2)=Lower bound\nVARTH(3)=Upper bound\nVARTH(4)=Optimization scale factor')
    rotvel = Array(dtype=numpy_float64, desc='ROTVEL(0)=Rotation velocity for takeoff noise abatement (default is minimum required to meet takeoff performance constraints)\nROTVEL(1)=Activity status, active if > 0\nROTVEL(2)=Lower bound\nROTVEL(3)=Upper bound\nROTVEL(4)=Optimization scale factor')
    plr = Array(dtype=numpy_float64, desc='PLR(0)=Thrust fraction after programmed lapse rate (default thrust is specified in each segment)\nPLR(1)=Activity status, active if > 0\nPLR(2)=Lower bound\nPLR(3)=Upper bound\nPLR(4)=Optimization scale factor')
    etit = Array(dtype=numpy_float64, units='degR', desc='ETIT(0)=Engine design point turbine entry temperature\nETIT(1)=Activity status, active if > 0\nETIT(2)=Lower bound\nETIT(3)=Upper bound\nETIT(4)=Optimization scale factor')
    eopr = Array(dtype=numpy_float64, desc='EOPR(0)=Overall pressure ratio\nEOPR(1)=Activity status, active if > 0\nEOPR(2)=Lower bound\nEOPR(3)=Upper bound\nEOPR(4)=Optimization scale factor')
    efpr = Array(dtype=numpy_float64, desc='EFPR(0)=Fan pressure ratio (turbofans only)\nEFPR(1)=Activity status, active if > 0\nEFPR(2)=Lower bound\nEFPR(3)=Upper bound\nEFPR(4)=Optimization scale factor')
    ebpr = Array(dtype=numpy_float64, desc='EBPR(0)=Bypass ratio (turbofans only)\nEBPR(1)=Activity status, active if > 0\nEBPR(2)=Lower bound\nEBPR(3)=Upper bound\nEBPR(4)=Optimization scale factor')
    ettr = Array(dtype=numpy_float64, desc='ETTR(0)=Engine throttle ratio defined as the ratio of the maximum allowable turbine inlet temperature divided by the design point turbine inlet temperature.\nIf ETTR is greater than ETIT, it is assumed to be the maximum allowable turbine inlet temperature.\nETTR(1)=Activity status, active if > 0\nETTR(2)=Lower bound\nETTR(3)=Upper bound\nETTR(4)=Optimization scale factor')
    ebla = Array(dtype=numpy_float64, units='deg', desc='EBLA(0)=Blade angle for fixed pitch propeller\nEBLA(1)=Activity status, active if > 0\nEBLA(2)=Lower bound\nEBLA(3)=Upper bound\nEBLA(4)=Optimization scale factor')


class FlopsWrapper_input_confin_Basic(VariableTree):
    """Container for input.confin.Basic"""

    # OpenMDAO Public Variables
    desrng = Float(0.0, desc='Design range (or endurance).  See INDR in Namelist &MISSIN)\nRequired - if IRW = 2 in Namelist &MISSIN, the range is computed, but a reasonable guess must still be input')
    wsr = Float(0.0, desc='Required wing loading if > 0.\nDo not set WSR > 0 during optimization or if wing area is being varied.\nInterpret SW as wing loading for parametric variation if = -1.\nDo not use for optimization.')
    twr = Float(0.0, desc='Required total thrust-weight ratio if > 0.\nDo not set TWR > 0 during optimization or if thrust is being varied.\nInterpret THRUST as thrust-weight ratio for parametric variation if = -1.\nDo not use for optimization.')
    htvc = Float(0.0, desc='Modified horizontal tail volume coefficient.\nIf HTVC > 0., SHT = HTVC * SW * Sqrt(SW/AR) / XL (This overrides any input value for SHT)\nIf HTVC = 1., the horizontal tail volume coefficient calculated from the input values of SHT, SW, AR and XL will be maintained.')
    vtvc = Float(0.0, desc='Modified vertical tail volume coefficient.\nIf VTVC > 0., SVT = VTVC * SW * Sqrt(SW*AR) / XL (This overrides any input value for SVT)\nIf VTVC = 1., the vertical tail volume coefficient calculated from the input values of SVT, SW, AR and XL will be maintained.')
    pglov = Float(0.0, desc='Fixed ratio of glove area to wing area (GLOV/SW).\nIf PGLOV > 0., GLOV will change if SW changes.')
    fixspn = Float(0.0, units='ft', desc='Special Option - Fixed wing span.  If the wing area is being varied or optimized, the wing aspect ratio will be adjusted to maintain a constant span.')
    fixful = Float(0.0, units='lb', desc='Special Option - Fixed mission fuel.  Allows specification of mission fuel.\nSince this fuel is normally a fall out (what is left over after OWE and payload are subtracted from the gross weight), this option requires iterating on the gross weight until the mission fuel = FIXFUL.  Gross weight cannot be an active design variable or used in a parametric variation, and IRW must be 2 in Namelist &MISSIN.')


class FlopsWrapper_input_confin(VariableTree):
    """Container for input.confin"""

    def __init__(self, *args, **kwargs):
        """Constructor for the FlopsWrapper_input_confin component"""

        super(FlopsWrapper_input_confin, self).__init__(*args, **kwargs)

        # VariableTrees
        self.add('Basic',  FlopsWrapper_input_confin_Basic())
        self.add('Design_Variables',  FlopsWrapper_input_confin_Design_Variables())
        self.add('Objective',  FlopsWrapper_input_confin_Objective())


class FlopsWrapper_input_asclin(VariableTree):
    """Container for input.asclin"""

    # OpenMDAO Public Variables
    sref = Float(0.0, units='ft*ft', desc='Wing area on which aerodynamic input is based (Default = SW, Namelist &CONFIN). If different from SW, aerodynamics will be scaled.')
    tref = Float(0.0, units='lb', desc='Engine thrust corresponding to nacelle size used in generating aerodynamic input data (Default = THRUST, Namelist &CONFIN). If different from THRUST, aerodynamic data will be modified.')
    awetn = Float(0.0, desc='Nacelle wetted area/SREF')
    eltot = Float(0.0, units='ft', desc='Total configuration length (Default = fuselage length)')
    voltot = Float(0.0, units='ft*ft*ft', desc='Total configuration volume')
    awett = Array(dtype=numpy_float64, desc='Total wetted area/SREF.  For variable geometry aircraft, up to NMP values may be input')
    awetw = Array(dtype=numpy_float64, desc='Wing wetted area/SREF')
    elw = Array(dtype=numpy_float64, units='ft', desc='Total length of exposed wing')
    volw = Array(dtype=numpy_float64, units='ft*ft*ft', desc='Total volume of exposed wing')
    form = Array(dtype=numpy_float64, desc='Subsonic form factor for total configuration')
    eql = Array(dtype=numpy_float64, units='ft', desc='Equivalent friction length for total baseline configuration.  If EQL is omitted, skin friction drag is computed from component data')
    cdwav = Array(dtype=numpy_float64, desc='Wave drag coefficients (NMP values)')
    dcdnac = Array(dtype=numpy_float64, desc='Delta wave drag coefficients, nacelles on - nacelles off')


class FlopsWrapper_input_aero_data(VariableTree):
    """Container for input.aero_data"""

    # OpenMDAO Public Variables
    aerodat = Str(iotype='in')


class FlopsWrapper_input_aerin_Takeoff_Landing(VariableTree):
    """Container for input.aerin.Takeoff_Landing"""

    # OpenMDAO Public Variables
    wratio = Float(0.0, desc='Ratio of maximum landing weight to maximum takeoff weight (Default = WLDG/GW if WLDG is input, otherwise for supersonic aircraft Default = 1. - .00009*DESRNG, for subsonic aircraft Default = 1. - .00004*DESRNG)')
    vappr = Float(150.0, units='nmi', desc='Maximum allowable landing approach velocity')
    flto = Float(12000.0, units='ft', desc='Maximum allowable takeoff field length')
    flldg = Float(0.0, units='ft', desc='Maximum allowable landing field length')
    cltom = Float(2.0, desc='Maximum CL in takeoff configuration')
    clldm = Float(3.0, desc='Maximum CL in landing configuration')
    clapp = Float(0.0, desc='Approach CL')
    dratio = Float(1.0, desc='Takeoff and landing air density ratio')
    elodss = Float(0.0, desc='Lift-Drag ratio for second segment climb (Default is internally computed)')
    elodma = Float(0.0, desc='Lift-Drag ratio for missed approach climb (Default is internally computed)')
    thrss = Float(0.0, units='lb', desc='Thrust per baseline engine for second segment climb (Default = THRUST, Namelist &CONFIN)')
    thrma = Float(0.0, units='lb', desc='Thrust per baseline engine for missed approach climb (Default = THRSS)')
    throff = Float(0.0, units='lb', desc='Thrust per baseline engine for takeoff (Default = THRSS)')


class FlopsWrapper_input_aerin_Internal_Aero(VariableTree):
    """Container for input.aerin.Internal_Aero"""

    # OpenMDAO Public Variables
    cam = Float(0.0, desc='Maximum camber at 70% semispan, percent of local chord')
    sbase = Float(0.0, units='ft*ft', desc='Aircraft base area (total exit cross-section area minus inlet capture areas for internally mounted engines)')
    aitek = Float(1.0, desc='Airfoil technology parameter.  Use 1 for conventional wing and 2 for advanced technology wing')
    modaro = Enum(0, (0,1), desc='Data tables in EDET are to be modified, Namelist &ARIDE will be read in', aliases=('No', 'Yes'))
    fcldes = Float(-1.0, desc='Fixed design lift coefficient.  If input, overrides design CL computed by EDET.')
    fmdes = Float(-1.0, desc='Fixed design Mach number.  If input, overrides design Mach number computed by EDET.')
    xllam = Enum(0, (0,1), desc='Use 0 for Turbulent flow and 1 for Laminar Flow', aliases=('Turbulent', 'Laminar'))
    truw = Float(0.0, desc='Percent LF wing upper surface')
    trlw = Float(0.0, desc='Percent LF wing low surface')
    truh = Float(0.0, desc='Percent LF horizontal tail upper surface')
    trlh = Float(0.0, desc='Percent LF horizontal tail lower surface')
    truv = Float(0.0, desc='Percent LF vertical tail upper surface')
    trlv = Float(0.0, desc='Percent LF vertical tail lower surface')
    trub = Float(0.0, desc='Percent LF fuselage upper surface')
    trlb = Float(0.0, desc='Percent LF fuselage lower surface')
    trun = Float(0.0, desc='Percent LF nacelle upper surface')
    trln = Float(0.0, desc='Percent LF nacelle lower surface')
    truc = Float(0.0, desc='Percent LF canard upper surface')
    trlc = Float(0.0, desc='Percent LF canard lower surface')
    e = Float(1.0, desc='Aerodynamic efficiency factor: use 1 for normal wing efficiency; normal wing efficiency modified for taper ratio and aspect ratio plus E if < 0; Otherwise, normal wing efficiency multiplied by E')
    swetw = Float(1.0, units='ft*ft', desc='Wing wetted area')
    sweth = Float(1.0, units='ft*ft', desc='Horizontal tail wetted area')
    swetv = Float(1.0, units='ft*ft', desc='Vertical tail wetted area')
    swetf = Float(1.0, units='ft*ft', desc='Fuselage wetted area')
    swetn = Float(1.0, units='ft*ft', desc='Nacelle wetted area')
    swetc = Float(1.0, units='ft*ft', desc='Canard wetted area')


class FlopsWrapper_input_aerin_Basic(VariableTree):
    """Container for input.aerin.Basic"""

    # OpenMDAO Public Variables
    myaero = Enum(0, (0,1,2,3,4), desc='Controls type of user-supplied aerodynamic data\n= 0, Drag polars are computed internally\n= 1, Aerodynamic Data will be read in\n= 2, Scalable Aerodynamic Data will be input (Namelist &ASCLIN required)\n= 3, Special parabolic Aerodynamic Data format (Namelist &RFHIN required)\n= 4, Use aerodynamic response surface - available only in DOSS version', aliases=('Internal', 'Fixed input', 'Scalable input', 'Parabolic', 'Response surface'))
    iwave = Enum(0, (0,1), desc='Controls Wave Drag Data input type\n= 1, Input Wave Drag Data will be formatted\n= 0, Otherwise', aliases=('No', 'Yes'))
    fwave = Float(1.0, desc='Wave drag factor - multiplies input values of wave drag from formatted aerodynamic data or Namelist &ASCLIN')
    itpaer = Enum(2, (1,2,3), desc='Aerodynamic data interpolation switch\n= 1, Linear - Use if aerodynamic data is irregular.  This is usually indicated by strange climb, descent or cruise profiles.\n= 2, Parabolic\n= 3, Parabolic interpolation for CL, linear interpolation for Mach number and altitude.', aliases=('Linear', 'Parabolic', 'Combination'))
    ibo = Enum(0, (0,1), desc='Format indicator for input aerodynamic matrices\n= 1, A new line is started for each Mach number for Cards 4 and for each altitude for Cards 8\n= 0, Data is continuous, 10 to a line', aliases=('Continuous', '1 Mach/line'))


class FlopsWrapper_input_aerin(VariableTree):
    """Container for input.aerin"""

    def __init__(self, *args, **kwargs):
        """Constructor for the FlopsWrapper_input_aerin component"""

        super(FlopsWrapper_input_aerin, self).__init__(*args, **kwargs)

        # VariableTrees
        self.add('Basic',  FlopsWrapper_input_aerin_Basic())
        self.add('Internal_Aero',  FlopsWrapper_input_aerin_Internal_Aero())
        self.add('Takeoff_Landing',  FlopsWrapper_input_aerin_Takeoff_Landing())


class FlopsWrapper_input(VariableTree):
    """Container for input"""

    # OpenMDAO Public Variables
    title = Str('', desc='Any alphanumeric title')

    def __init__(self, *args, **kwargs):
        """Constructor for the FlopsWrapper_input component"""

        super(FlopsWrapper_input, self).__init__(*args, **kwargs)

        # VariableTrees
        self.add('aerin',  FlopsWrapper_input_aerin())
        self.add('aero_data',  FlopsWrapper_input_aero_data())
        self.add('asclin',  FlopsWrapper_input_asclin())
        self.add('confin',  FlopsWrapper_input_confin())
        self.add('costin',  FlopsWrapper_input_costin())
        self.add('engdin',  FlopsWrapper_input_engdin())
        self.add('engine',  FlopsWrapper_input_engine())
        self.add('engine_deck',  FlopsWrapper_input_engine_deck())
        self.add('fusein',  FlopsWrapper_input_fusein())
        self.add('missin',  FlopsWrapper_input_missin())
        self.add('mission_definition',  FlopsWrapper_input_mission_definition())
        self.add('nacell',  FlopsWrapper_input_nacell())
        self.add('noisin',  FlopsWrapper_input_noisin())
        self.add('option',  FlopsWrapper_input_option())
        self.add('proin',  FlopsWrapper_input_proin())
        self.add('rfhin',  FlopsWrapper_input_rfhin())
        self.add('syntin',  FlopsWrapper_input_syntin())
        self.add('tolin',  FlopsWrapper_input_tolin())
        self.add('wtin',  FlopsWrapper_input_wtin())

        
# pylint: enable-msg=C0301,C0324,R0903

class FlopsWrapper(ExternalCode):
    """Wrapper for FlopsWrapper"""

    # OpenMDAO Public Variables
    ERROR = Str('none', iotype='out', desc='Error message for FLOPS failures')
    HINT = Str('none', iotype='out', desc='Hint for resolving error')
    npcon = Int(0, iotype='in', desc='Number of PCONIN namelists to be created')
    nseg = Int(0, iotype='in', desc='Number of SEGIN namelists to be created')
    nrerun = Int(0, iotype='in', desc='Number of RERUN namelists to be created')
    npcons = Array(iotype='in', dtype=numpy_int64, desc='Number of PCONIN ' +
                   'namelists to be created with each RERUN namelist')
    
    # Slots for Variable Trees
    input = Slot(FlopsWrapper_input, iotype='in')
    output = Slot(FlopsWrapper_output, iotype='out')
    
    # This stuff is defined in ExternalCode. I'm preserving it to keep a record
    # of the var names that were used in the MC Java wrapper.
    # ----
    #execute_cmd = Str('flops', iotype='in', desc='Command for executing FLOPS')

    def __init__(self, *args, **kwargs):
        """Constructor for the FlopsWrapper component"""

        super(FlopsWrapper, self).__init__(*args, **kwargs)

        # VariableTrees
        self.add('input',  FlopsWrapper_input(iotype='in'))
        self.add('output',  FlopsWrapper_output(iotype='out'))
        
        # External Code public variables
        self.stdin = 'flops.inp'
        self.stdout = 'flops.out'
        self.stderr = 'flops.err'
        self.command = ['flops']
        
        self.external_files = [
            FileMetadata(path=self.stdin, input=True),
            FileMetadata(path=self.stdout),
            FileMetadata(path=self.stderr),
        ]
        
        # This stuff is global in the Java wrap. 
        # These are used when adding and removing certain segments.
        self.nseg0 = 0
        self.npcon0 = 0
        self.nrern0 = 0
        self.npcons0 = []
        self.npcons0.append(0)
        self.nmseg = 0

    def execute(self):
        """Run Flops."""
        
        #Prepare the input files for Flops
        self.generate_input()
        
        #Run Flops via ExternalCode's execute function
        super(FlopsWrapper, self).execute()

        #Parse the outut files from Flops
        self.parse_output()
        
    def generate_input(self):
        """Creates the FLOPS input file(s) namelists."""
        
        sb = Namelist(self)
        sb.set_filename(self.stdin)
        
        # Write the Title Card
        sb.set_title(self.input.title)
        
        #-------------------
        # Namelist &OPTION
        #-------------------
        
        sb.add_group('OPTION')
        sb.add_comment("\n  ! Program Control, Execution, Analysis and Plot Option Data")
        
        iopt = self.input.option.Program_Control.iopt
        ianal = self.input.option.Program_Control.ianal
        ineng = self.input.option.Program_Control.ineng
        itakof = self.input.option.Program_Control.itakof
        iland = self.input.option.Program_Control.iland
        nopro = self.input.option.Program_Control.nopro
        noise = self.input.option.Program_Control.noise
        icost = self.input.option.Program_Control.icost
        ifite = self.input.option.Program_Control.ifite
        mywts = self.input.wtin.Basic.mywts
        
        sb.add_container("input.option.Program_Control")

        sb.add_comment("\n  ! Plot files for XFLOPS Graphical Interface Postprocessor (MSMPLOT)")
        sb.add_var("input.option.Plot_Files.ixfl")

        sb.add_comment("\n  ! Takeoff and Climb Profile File for Noise Calculations (NPROF)")
        sb.add_var("input.option.Plot_Files.npfile")

        sb.add_comment("\n  ! Drag Polar Plot File (POLPLOT)")
        sb.add_var("input.option.Plot_Files.ipolp")
        sb.add_var("input.option.Plot_Files.polalt")
        
        nmach = len(self.input.option.Plot_Files.pmach)
        if nmach > 0:
            sb.add_newvar("nmach", nmach)
            sb.add_var("input.option.Plot_Files.pmach")

        sb.add_comment("\n  ! Engine Performance Data Plot File (THRPLOT)")
        sb.add_var("input.option.Plot_Files.ipltth")

        sb.add_comment("\n  ! Design History Plot File (HISPLOT)")
        sb.add_var("input.option.Plot_Files.iplths")

        ipltps = len(self.input.option.Excess_Power_Plot.pltnz)
        if ipltps > 0:
            sb.add_comment("\n  ! Excess Power Plot File (PSPLOT)")
            sb.add_newvar("ipltps", ipltps)
            sb.add_container("input.option.Excess_Power_Plot")
            
        # Plotfile names
        sb.add_comment("\n  ! Plotfile Names")
        if self.input.option.Plot_Files.cnfile:
            sb.add_var("input.option.Plot_Files.cnfile")
        if self.input.option.Plot_Files.msfile:
            sb.add_var("input.option.Plot_Files.msfile")
        if self.input.option.Plot_Files.crfile:
            sb.add_var("input.option.Plot_Files.crfile")
        if self.input.option.Plot_Files.tofile :
            sb.add_var("input.option.Plot_Files.tofile ")
        if self.input.option.Plot_Files.nofile :
            sb.add_var("input.option.Plot_Files.nofile ")
        if self.input.option.Plot_Files.apfile :
            sb.add_var("input.option.Plot_Files.apfile ")
        if self.input.option.Plot_Files.thfile :
            sb.add_var("input.option.Plot_Files.thfile ")
        if self.input.option.Plot_Files.hsfile :
            sb.add_var("input.option.Plot_Files.hsfile ")
        if self.input.option.Plot_Files.psfile :
            sb.add_var("input.option.Plot_Files.psfile ")
            
        #-------------------
        # Namelist &WTIN
        #-------------------
        
        sb.add_group('WTIN')

        sb.add_comment("\n  ! Geometric, Weight, Balance and Inertia Data")
        sb.add_container("input.wtin.Basic")

        sb.add_comment("\n  ! Special Option for Operating Weight Empty Calculations")
        sb.add_container("input.wtin.OEW_Calculations")

        sb.add_comment("\n  ! Wing Data")
        sb.add_container("input.wtin.Wing_Data")

        netaw = len(self.input.wtin.Detailed_Wing.etaw)
        if netaw > 0:
            sb.add_comment("\n  ! Detailed Wing Data")
            sb.add_newvar("netaw", netaw)
            sb.add_var("input.wtin.Detailed_Wing.etaw")
            sb.add_var("input.wtin.Detailed_Wing.chd")
            sb.add_var("input.wtin.Detailed_Wing.toc")
            sb.add_var("input.wtin.Detailed_Wing.swl")
            sb.add_var("input.wtin.Detailed_Wing.etae")
            sb.add_var("input.wtin.Detailed_Wing.pctl")
            sb.add_var("input.wtin.Detailed_Wing.arref")
            sb.add_var("input.wtin.Detailed_Wing.tcref")
            sb.add_var("input.wtin.Detailed_Wing.nstd")
            
            pdist = self.input.wtin.Detailed_Wing.pdist
            sb.add_var("input.wtin.Detailed_Wing.pdist")
            if pdist < 0.0001:
                sb.add_var("input.wtin.Detailed_Wing.etap")
                sb.add_var("input.wtin.Detailed_Wing.pval")

        sb.add_comment("\n  ! Tails, Fins, Canards")
        sb.add_comment("\n  ! Horizontal Tail Data")
        sb.add_var("input.wtin.Tails_Fins.sht")
        sb.add_var("input.wtin.Tails_Fins.swpht")
        sb.add_var("input.wtin.Tails_Fins.arht")
        sb.add_var("input.wtin.Tails_Fins.trht")
        sb.add_var("input.wtin.Tails_Fins.tcht")
        sb.add_var("input.wtin.Tails_Fins.hht")
            
        nvert = self.input.wtin.Tails_Fins.nvert
        if nvert != 0:
            sb.add_comment("\n  ! Vertical Tail Data")
            sb.add_var("input.wtin.Tails_Fins.nvert")
            sb.add_var("input.wtin.Tails_Fins.svt")
            sb.add_var("input.wtin.Tails_Fins.swpvt")
            sb.add_var("input.wtin.Tails_Fins.arvt")
            sb.add_var("input.wtin.Tails_Fins.trvt")
            sb.add_var("input.wtin.Tails_Fins.tcvt")
            
        nfin = self.input.wtin.Tails_Fins.nfin
        if nfin != 0:
            sb.add_comment("\n  ! Fin Data")
            sb.add_var("input.wtin.Tails_Fins.nfin")
            sb.add_var("input.wtin.Tails_Fins.sfin")
            sb.add_var("input.wtin.Tails_Fins.arfin")
            sb.add_var("input.wtin.Tails_Fins.trfin")
            sb.add_var("input.wtin.Tails_Fins.swpfin")
            sb.add_var("input.wtin.Tails_Fins.tcfin")

        scan = self.input.wtin.Tails_Fins.scan
        if scan != 0:
            sb.add_comment("\n  ! Canard Data")
            sb.add_var("input.wtin.Tails_Fins.scan")
            sb.add_var("input.wtin.Tails_Fins.swpcan")
            sb.add_var("input.wtin.Tails_Fins.arcan")
            sb.add_var("input.wtin.Tails_Fins.trcan")
            sb.add_var("input.wtin.Tails_Fins.tccan")

        sb.add_comment("\n  ! Fuselage Data")
        sb.add_container("input.wtin.Fuselage")

        sb.add_comment("\n  ! Landing Gear Data")
        sb.add_container("input.wtin.Landing_Gear")

        sb.add_comment("\n  ! Propulsion System Data")
        sb.add_container("input.wtin.Propulsion")

        sb.add_comment("\n  ! Fuel System Data")
        sb.add_var("input.wtin.Fuel_System.ntank")
        sb.add_var("input.wtin.Fuel_System.fulwmx")
        sb.add_var("input.wtin.Fuel_System.fulden")
        sb.add_var("input.wtin.Fuel_System.fulfmx")
        sb.add_var("input.wtin.Fuel_System.ifufu")
        sb.add_var("input.wtin.Fuel_System.fulaux")

        fuscla = self.input.wtin.Fuel_System.fuscla
        if fuscla > 0.000001:
            sb.add_comment("\n  ! Special method for scaling wing fuel capacity")
            sb.add_var("input.wtin.Fuel_System.fuelrf")
            sb.add_var("input.wtin.Fuel_System.fswref")
            sb.add_var("input.wtin.Fuel_System.fuscla")
            sb.add_var("input.wtin.Fuel_System.fusclb")

        sb.add_comment("\n  ! Crew and Payload Data")
        sb.add_container("input.wtin.Crew_Payload")

        sb.add_comment("\n  ! Override Parameters")
        sb.add_container("input.wtin.Override")

        sb.add_comment("\n  ! Center of Gravity (C.G.) Data")
        sb.add_container("input.wtin.Center_of_Gravity")

        inrtia = self.input.wtin.Inertia.inrtia
        if inrtia != 0:
            sb.add_comment("\n  ! Inertia Data")
            sb.add_newvar("inrtia", inrtia)
            sb.add_var("input.wtin.Inertia.zht")
            sb.add_var("input.wtin.Inertia.zvt")
            sb.add_var("input.wtin.Inertia.zfin")
            sb.add_var("input.wtin.Inertia.yfin")
            sb.add_var("input.wtin.Inertia.zef")
            sb.add_var("input.wtin.Inertia.yef")
            sb.add_var("input.wtin.Inertia.zea")
            sb.add_var("input.wtin.Inertia.yea")
            sb.add_var("input.wtin.Inertia.zbw")
            sb.add_var("input.wtin.Inertia.zap")
            sb.add_var("input.wtin.Inertia.zrvt")
            sb.add_var("input.wtin.Inertia.ymlg")
            sb.add_var("input.wtin.Inertia.yfuse")
            sb.add_var("input.wtin.Inertia.yvert")
            sb.add_var("input.wtin.Inertia.swtff")
            sb.add_var("input.wtin.Inertia.tcr")
            sb.add_var("input.wtin.Inertia.tct")
            sb.add_var("input.wtin.Inertia.incpay")
            
            l = len(self.input.wtin.Inertia.tx)
            sb.add_newvar("itank", l)
            if l > 0:
                sb.add_var("input.wtin.Inertia.tx")
                sb.add_var("input.wtin.Inertia.ty")
                sb.add_var("input.wtin.Inertia.tz")

            j = len(self.input.wtin.Inertia.tl)
            if j > 0:
                sb.add_var("input.wtin.Inertia.tl")
                sb.add_var("input.wtin.Inertia.tw")
                sb.add_var("input.wtin.Inertia.td")

            j = self.input.wtin.Inertia.tf.shape[0]
            sb.add_newvar("nfcon", j)
            if l*j > 0:
                sb.add_var("input.wtin.Inertia.tf")

        #-------------------
        # Namelist &FUSEIN
        #-------------------
        
        # Namelist &FUSEIN is only required if XL=0 or IFITE=3.
        xl = self.input.wtin.Fuselage.xl
        if xl < 0.0000001 or ifite == 3:
            
            sb.add_group('FUSEIN')
            sb.add_comment("\n  ! Fuselage Design Data")
            sb.add_container("input.fusein.Basic")
            sb.add_container("input.fusein.BWB")
            
        #-------------------
        # Namelist &CONFIN
        #-------------------
        
        sb.add_group('CONFIN')
        sb.add_container("input.confin.Basic")

        # MC Flops wrapper didn't write these out if iopt was less than 3
        # I changed it to match expected behavior when comparing manual FLOPS
        # if iopt >= 3:
        sb.add_comment("\n  ! Objective Function Definition")
        sb.add_container("input.confin.Objective")
            
        sb.add_comment("\n  ! Design Variables")
        sb.add_var("input.confin.Design_Variables.gw")
        sb.add_var("input.confin.Design_Variables.ar")
        sb.add_var("input.confin.Design_Variables.thrust")
        sb.add_var("input.confin.Design_Variables.sw")
        sb.add_var("input.confin.Design_Variables.tr")
        sb.add_var("input.confin.Design_Variables.sweep")
        sb.add_var("input.confin.Design_Variables.tca")
        sb.add_var("input.confin.Design_Variables.vcmn")
        sb.add_var("input.confin.Design_Variables.ch")
        sb.add_var("input.confin.Design_Variables.varth")
        sb.add_var("input.confin.Design_Variables.rotvel")
        sb.add_var("input.confin.Design_Variables.plr")
        
        igenen = self.input.engdin.Basic.igenen
        if igenen in (1, -2):
            sb.add_comment("\n  ! Engine Design Variables")
            sb.add_var("input.confin.Design_Variables.etit")
            sb.add_var("input.confin.Design_Variables.eopr")
            sb.add_var("input.confin.Design_Variables.efpr")
            sb.add_var("input.confin.Design_Variables.ebpr")
            sb.add_var("input.confin.Design_Variables.ettr")
            sb.add_var("input.confin.Design_Variables.ebla")

        #-------------------
        # Namelist &AERIN
        #-------------------

        sb.add_group('AERIN')

        myaero = self.input.aerin.Basic.myaero
        iwave = self.input.aerin.Basic.iwave
        if myaero != 0:
            sb.add_comment("\n  ! Externally Computed Aerodynamics")
            sb.add_var("input.aerin.Basic.myaero")
            sb.add_var("input.aerin.Basic.iwave")
            if iwave != 0:
                sb.add_var("input.aerin.Basic.fwave")
            sb.add_var("input.aerin.Basic.itpaer")
            sb.add_var("input.aerin.Basic.ibo")
        else:
            sb.add_comment("\n  ! Internally Computed Aerodynamics")
            sb.add_container("input.aerin.Internal_Aero")

        sb.add_container("input.aerin.Takeoff_Landing")

        #-------------------
        # Namelist &COSTIN
        #-------------------

        # Namelist &COSTIN is only required if ICOST=1.
        if icost != 0:
            sb.add_group('COSTIN')
            
            sb.add_comment("\n  ! Cost Calculation Data")
            sb.add_container("input.costin.Basic")
            sb.add_comment("\n  ! Mission Performance Data")
            sb.add_container("input.costin.Mission_Performance")
            sb.add_comment("\n  ! Cost Technology Parameters")
            sb.add_container("input.costin.Cost_Technology")

        #-------------------
        # Namelist &ENGDIN
        #-------------------

        # Namelist &ENGDIN is only required in IANAL=3 or 4 or INENG=1.
        if ianal in (3, 4) or ineng == 1:
            sb.add_group('ENGDIN')
            
            sb.add_comment("\n  ! Engine Deck Control, Scaling and Usage Data")
            sb.add_var("input.engdin.Basic.ngprt")
            sb.add_var("input.engdin.Basic.igenen")
            sb.add_var("input.engdin.Basic.extfac")
            sb.add_var("input.engdin.Basic.fffsub")
            sb.add_var("input.engdin.Basic.fffsup")
            sb.add_var("input.engdin.Basic.idle")
            sb.add_var("input.engdin.Basic.noneg")
            sb.add_var("input.engdin.Basic.fidmin")
            sb.add_var("input.engdin.Basic.fidmax")
            sb.add_var("input.engdin.Basic.ixtrap")
            sb.add_var("input.engdin.Basic.ifill")
            sb.add_var("input.engdin.Basic.maxcr")
            sb.add_var("input.engdin.Basic.nox")
            
            npcode =  len(self.input.engdin.Basic.pcode)
            if npcode > 0:
                sb.add_newvar("npcode", npcode)
                sb.add_var("input.engdin.Basic.pcode")
                
            sb.add_var("input.engdin.Basic.boost")
            sb.add_var("input.engdin.Basic.igeo")
            sb.add_var("input.engdin.Special_Options.dffac")
            sb.add_var("input.engdin.Special_Options.fffac")
            
            if igenen in (1, -2):
                j =  len(self.input.engdin.Special_Options.emach)
                l =  self.input.engdin.Special_Options.alt.shape[0]
                if j > 0:
                    # TODO - Find out about fake 2d for new FLOPS double prop
                    # capability.
                    sb.add_var("input.engdin.Special_Options.emach")
                    if l*j > 0:
                        # TODO - Find out about fake 3d for new FLOPS double prop
                        # capability.
                        sb.add_var("input.engdin.Special_Options.alt")
                                  
            insdrg =  self.input.engdin.Special_Options.insdrg
            if insdrg != 0:
                sb.add_comment("\n  ! Nozzle installation drag using table look-up")
                sb.add_newvar("insdrg", insdrg)
                sb.add_var("input.engdin.Special_Options.nab")
                sb.add_var("input.engdin.Special_Options.nabref")
                sb.add_var("input.engdin.Special_Options.a10")
                sb.add_var("input.engdin.Special_Options.a10ref")
                sb.add_var("input.engdin.Special_Options.a9ref")
                sb.add_var("input.engdin.Special_Options.xnoz")
                sb.add_var("input.engdin.Special_Options.xnref")
                sb.add_var("input.engdin.Special_Options.rcrv")
                
                # TODO - rawInputFile( cdfile, "ENDRAG" );
                #cdfile.open
                
            # Write out the eifile. This is a new addition.
            sb.add_var("input.engdin.eifile")


            #----------------------
            # Namelist Engine deck
            #----------------------
    
            # Insert the engine deck into the flops input file
    
            # If IGENEN=0 the engine deck is part of the input file, otherwise it is an
            # external file.
            
            engine_deck  = self.input.engine_deck.engdek
            if igenen in (0, -2):
                # engine_deck contains the raw engine deck
                sb.add_group(engine_deck)
            else:
                # engine_deck contains the name of the engine deck file
                if engine_deck:
                    sb.add_var("input.engine_deck.engdek")

        #-------------------
        # Namelist &ENGINE
        #-------------------

        # Namelist &ENGINE is only required if IGENEN=-2 or 1.
        if igenen in (-2, 1):
            
            sb.add_group('ENGINE')

            nginwt =  self.input.engine.Engine_Weight.nginwt
            ieng = self.input.engine.Basic.ieng
            
            sb.add_var("input.engine.Basic.ieng")
            sb.add_var("input.engine.Basic.iprint")
            sb.add_var("input.engine.Basic.gendek")
            sb.add_var("input.engine.Basic.ithrot")
            sb.add_var("input.engine.Basic.npab")
            sb.add_var("input.engine.Basic.npdry")
            sb.add_var("input.engine.Basic.xidle")
            sb.add_var("input.engine.Basic.nitmax")
            
            if self.input.engine.Basic.xmmax > 0:
                sb.add_var("input.engine.Basic.xmmax")
            if self.input.engine.Basic.amax > 0:
                sb.add_var("input.engine.Basic.amax")
            if self.input.engine.Basic.xminc > 0:
                sb.add_var("input.engine.Basic.xminc")
            if self.input.engine.Basic.ainc > 0:
                sb.add_var("input.engine.Basic.ainc")
            if self.input.engine.Basic.qmin > 0:
                sb.add_var("input.engine.Basic.qmin")
            if self.input.engine.Basic.qmax > 0:
                sb.add_var("input.engine.Basic.qmax")
                
            sb.add_newvar("nginwt", nginwt)
            sb.add_container("input.engine.Noise_Data")
            
            if self.input.engine.Design_Point.desfn > 0:
                sb.add_var("input.engine.Design_Point.desfn")
            if self.input.engine.Design_Point.xmdes > 0:
                sb.add_var("input.engine.Design_Point.xmdes")
            if self.input.engine.Design_Point.xades > 0:
                sb.add_var("input.engine.Design_Point.xades")
                
            sb.add_var("input.engine.Design_Point.oprdes")
            sb.add_var("input.engine.Design_Point.fprdes")
            sb.add_var("input.engine.Design_Point.bprdes")
            sb.add_var("input.engine.Design_Point.tetdes")
            sb.add_var("input.engine.Design_Point.ttrdes")
            sb.add_var("input.engine.Other.hpcpr")
            sb.add_var("input.engine.Other.aburn")
            sb.add_var("input.engine.Other.dburn")
            sb.add_var("input.engine.Other.effab")
            sb.add_var("input.engine.Other.tabmax")
            sb.add_var("input.engine.Other.ven")
            sb.add_var("input.engine.Other.costbl")
            sb.add_var("input.engine.Other.fanbl")
            sb.add_var("input.engine.Other.hpext")
            sb.add_var("input.engine.Other.wcool")
            sb.add_var("input.engine.Other.fhv")
            sb.add_var("input.engine.Other.dtce")
            sb.add_var("input.engine.Other.alc")
            sb.add_var("input.engine.Other.year")
            sb.add_comment("\n  ! Installation effects")
            sb.add_var("input.engine.Other.boat")
            sb.add_var("input.engine.Other.ajmax")
            
            if self.input.engine.Other.spill:
                sb.add_comment("\n  ! Installation effects")
                sb.add_var("input.engine.Other.spill")
                sb.add_var("input.engine.Other.lip")
                sb.add_var("input.engine.Other.blmax")
                sb.add_var("input.engine.Other.spldes")
                sb.add_var("input.engine.Other.aminds")
                sb.add_var("input.engine.Other.alinds")
                
            sb.add_var("input.engine.Other.etaprp")
            sb.add_var("input.engine.Other.shpowa")
            sb.add_comment("\n  ! Engine operating constraints")
            sb.add_var("input.engine.Other.cdtmax")
            sb.add_var("input.engine.Other.cdpmax")
            sb.add_var("input.engine.Other.vjmax")
            sb.add_var("input.engine.Other.stmin")
            sb.add_var("input.engine.Other.armax")
            sb.add_var("input.engine.Other.limcd")
            
            if nginwt != 0:
                sb.add_comment("\n  ! Engine Weight Calculation Data")
                sb.add_var("input.engine.Engine_Weight.iwtprt")
                sb.add_var("input.engine.Engine_Weight.iwtplt")
                sb.add_var("input.engine.Engine_Weight.gratio")
                sb.add_var("input.engine.Engine_Weight.utip1")
                sb.add_var("input.engine.Engine_Weight.rh2t1")
                sb.add_var("input.engine.Engine_Weight.igvw")
                sb.add_var("input.engine.Engine_Weight.trbrpm")
                sb.add_var("input.engine.Engine_Weight.trban2")
                sb.add_var("input.engine.Engine_Weight.trbstr")
                sb.add_var("input.engine.Engine_Weight.cmpan2")
                sb.add_var("input.engine.Engine_Weight.cmpstr")
                sb.add_var("input.engine.Engine_Weight.vjpnlt")
                sb.add_var("input.engine.Engine_Weight.wtebu")
                sb.add_var("input.engine.Engine_Weight.wtcon")

            if ieng == 101:
                sb.add_var("input.engine.IC_Engine.ncyl")
                sb.add_var("input.engine.IC_Engine.deshp")
                sb.add_var("input.engine.IC_Engine.alcrit")
                sb.add_var("input.engine.IC_Engine.sfcmax")
                sb.add_var("input.engine.IC_Engine.sfcmin")
                sb.add_var("input.engine.IC_Engine.pwrmin")
                sb.add_var("input.engine.IC_Engine.engspd")
                sb.add_var("input.engine.IC_Engine.prpspd")
      
            if ieng == 101 or igenen == -2 and nginwt > 0:
                sb.add_var("input.engine.IC_Engine.iwc")
                sb.add_var("input.engine.IC_Engine.ecid")
                sb.add_var("input.engine.IC_Engine.ecr")

            if ieng == 101 or igenen == -2:
                sb.add_var("input.engine.IC_Engine.eht")
                sb.add_var("input.engine.IC_Engine.ewid")
                sb.add_var("input.engine.IC_Engine.elen")
                sb.add_var("input.engine.IC_Engine.ntyp")
                sb.add_var("input.engine.IC_Engine.af")
                sb.add_var("input.engine.IC_Engine.cli")
                sb.add_var("input.engine.IC_Engine.blang")
                sb.add_var("input.engine.IC_Engine.dprop")
                sb.add_var("input.engine.IC_Engine.nblade")
                sb.add_var("input.engine.IC_Engine.gbloss")
         
            nrpm =  len(self.input.engine.IC_Engine.arrpm)
            if nrpm > 0:
                sb.add_comment("  ! power curve input data")
                sb.add_newvar("nrpm", nrpm)
                sb.add_var("input.engine.IC_Engine.arrpm")
                sb.add_var("input.engine.IC_Engine.arpwr")
                sb.add_var("input.engine.IC_Engine.arful")
                if self.input.engine.IC_Engine.lfuun != 0:
                    sb.add_var("input.engine.IC_Engine.lfuun")
                    sb.add_var("input.engine.IC_Engine.feng")
               
            sb.add_var("input.engine.IC_Engine.fprop")
            sb.add_var("input.engine.IC_Engine.fgbox")

            ifile = self.input.engine.ifile
            tfile = self.input.engine.tfile
      
            # The name of the engine cycle definition file to be read in is
            # set by the value of if IENG.
            filenames = { 0: "MYCYCL",
                          1: "TURJET",
                          2: "TFNSEP",
                          3: "TFNMIX",
                          4: "TURPRP",
                          5: "TBYPAS",
                          6: "TFNSP3",
                          7: "TFNMX3",
                          8: "TFN3SH",
                          9: "TURJT2",
                          101: "MYCYCL" }
            try:
                ifilNam = filenames[ieng]
            except KeyError:
                msg = "Illegal value %s for input.engine.Basic.IENG" % ieng
                raise KeyError(msg)
                
            # TODO - rawInputFile( ifile, ifilNam )
            # TODO - rawInputFile( tfile, "ENGTAB" )
            sb.add_newvar("tfile", tfile)
            sb.add_newvar("ifile", ifilNam)

            #-------------------
            # Namelist &NACELL
            #-------------------

            # Namelist &NACELL is only required if NGINWT != 0
            # (note:, still in IGENEN=-2 or 1.)
            if nginwt != 0:
            
                sb.add_group('NACELL')
                sb.add_comment("\n  ! Data for Computation of Nacelle Weight.")
                sb.add_container("input.nacell")
            
        #-------------------
        # Namelist &MISSIN
        #-------------------

        # Namelist &MISSIN is only required if IANAL=3
        
        npcon = self.npcon

        if ianal == 3:
            
            sb.add_group('MISSIN')
            
            sb.add_comment("\n  ! Performance Controls and Factors and Mission Segment Definition")
            sb.add_var("input.missin.Basic.indr")
            sb.add_var("input.missin.Basic.fact")
            sb.add_var("input.missin.Basic.fleak")
            sb.add_var("input.missin.Basic.fcdo")
            sb.add_var("input.missin.Basic.fcdi")
            sb.add_var("input.missin.Basic.fcdsub")
            sb.add_var("input.missin.Basic.fcdsup")
            sb.add_var("input.missin.Basic.iskal")
            sb.add_var("input.missin.Basic.owfact")
            sb.add_var("input.missin.Basic.iflag")
            sb.add_var("input.missin.Basic.msumpt")
            sb.add_var("input.missin.Basic.dtc")
            sb.add_var("input.missin.Basic.irw")
            sb.add_var("input.missin.Basic.rtol")
            sb.add_var("input.missin.Basic.nhold")
            sb.add_var("input.missin.Basic.iata")
            sb.add_var("input.missin.Basic.tlwind")
            sb.add_var("input.missin.Basic.dwt")
            
            if len(self.input.missin.Basic.offdr) > 0:
                sb.add_var("input.missin.Basic.offdr")
                
            sb.add_var("input.missin.Basic.idoq")
            sb.add_newvar("npcon", npcon)
            
            nsout =  self.input.missin.Basic.nsout
            if nsout > 0:
                sb.add_comment("\n  ! Combat Radius Mission\n")
                sb.add_newvar("nsout", nsout)
                sb.add_var("input.missin.Basic.nsadj")
                sb.add_var("input.missin.Basic.mirror")

            i =  len(self.input.missin.Store_Drag.stma)
            if i > 0:
                sb.add_comment("\n  ! Store Drags")
                sb.add_container("input.missin.Store_Drag")

            sb.add_var("input.missin.User_Weights.mywts")
            if mywts == 1:
                sb.add_comment("\n  ! User-Specified Weights")
                sb.add_var("input.missin.User_Weights.rampwt")
                sb.add_var("input.missin.User_Weights.dowe")
                sb.add_var("input.missin.User_Weights.paylod")
                sb.add_var("input.missin.User_Weights.fuemax")
      
            sb.add_comment("\n  ! Ground Operations and Takeoff and Approach Allowances")
            sb.add_container("input.missin.Ground_Operations")
            
            if len(self.input.missin.Turn_Segments.xnz) > 0:
                sb.add_var("input.missin.Turn_Segments.xnz")
            if len(self.input.missin.Turn_Segments.xcl) > 0:
                sb.add_var("input.missin.Turn_Segments.xcl")
            if len(self.input.missin.Turn_Segments.xmach) > 0:
                sb.add_var("input.missin.Turn_Segments.xmach")

            nclimb = max( len(self.input.missin.Climb.clmmin),
                          len(self.input.missin.Climb.clmmax),
                          len(self.input.missin.Climb.clamax),
                          len(self.input.missin.Climb.nincl),
                          len(self.input.missin.Climb.fwf),
                          len(self.input.missin.Climb.ncrcl),
                          len(self.input.missin.Climb.cldcd),
                          len(self.input.missin.Climb.ippcl),
                          len(self.input.missin.Climb.maxcl) )
            
            # TODO - Ask Karl or Jeff about this
            # I've removed ioc and ifeath from this. These are parameters, so
            # their "length" should have nothing to do with how many Cruise
            # Schedules are in the model.
            ncruse = max( len(self.input.missin.Cruise.crmach),
                          len(self.input.missin.Cruise.cralt),
                          len(self.input.missin.Cruise.crdcd),
                          len(self.input.missin.Cruise.flrcr),
                          len(self.input.missin.Cruise.crmmin),
                          len(self.input.missin.Cruise.crclmx),
                          len(self.input.missin.Cruise.hpmin),
                          len(self.input.missin.Cruise.ffuel),
                          len(self.input.missin.Cruise.fnox),
                          len(self.input.missin.Cruise.feathf),
                          len(self.input.missin.Cruise.cdfeth) )

            nql = len(self.input.missin.Climb.qlalt)
            ns = len(self.input.missin.Descent.adtab)

            sb.add_comment("\n  ! Climb Schedule Definition")
            sb.add_newvar("nclimb", nclimb)
            sb.add_var("input.missin.Climb.clmmin")
            sb.add_var("input.missin.Climb.clmmax")
            sb.add_var("input.missin.Climb.clamin")
            sb.add_var("input.missin.Climb.clamax")
            sb.add_var("input.missin.Climb.nincl")
            sb.add_var("input.missin.Climb.fwf")
            sb.add_var("input.missin.Climb.ncrcl")
            sb.add_var("input.missin.Climb.cldcd")
            sb.add_var("input.missin.Climb.ippcl")
            sb.add_var("input.missin.Climb.maxcl")
            sb.add_var("input.missin.Climb.keasvc")
            
            actab = self.input.missin.Climb.actab
            no = actab.shape[1]
            if no == 0:
                no = actab.shape[0]
            elif no > 0:
                noval = ""
                for i in range(0, nclimb):
                    if actab.shape[1] > 0:
                        for j in range(0, actab.shape[1]):
                            if actab[i, j] >= 0.0:
                                n = j+1
                                noval += n + ", "
                            else:
                                break
                    else:
                        noval += "0, "
                        
                sb.add_newvar("no", noval)
                sb.add_var("input.missin.Climb.actab")
                sb.add_var("input.missin.Climb.vctab")

            sb.add_var("input.missin.Climb.ifaacl")
            sb.add_var("input.missin.Climb.ifaade")
            sb.add_var("input.missin.Climb.nodive")
            sb.add_var("input.missin.Climb.divlim")
            sb.add_var("input.missin.Climb.qlim")
            sb.add_var("input.missin.Climb.spdlim")
            if nql > 0:
                sb.add_var("input.missin.Climb.qlalt")
                sb.add_var("input.missin.Climb.vqlm")
      
            sb.add_comment("\n  ! Cruise Schedule Definition\n")
            sb.add_newvar("ncruse", ncruse)
            sb.add_var("input.missin.Cruise.ioc")
            sb.add_var("input.missin.Cruise.crmach")
            sb.add_var("input.missin.Cruise.cralt")
            sb.add_var("input.missin.Cruise.crdcd")
            sb.add_var("input.missin.Cruise.flrcr")
            sb.add_var("input.missin.Cruise.crmmin")
            sb.add_var("input.missin.Cruise.crclmx")
            sb.add_var("input.missin.Cruise.hpmin")
            sb.add_var("input.missin.Cruise.ffuel")
            sb.add_var("input.missin.Cruise.fnox")
            sb.add_var("input.missin.Cruise.ifeath")
            sb.add_var("input.missin.Cruise.feathf")
            sb.add_var("input.missin.Cruise.cdfeth")
            sb.add_var("input.missin.Cruise.dcwt")
            sb.add_var("input.missin.Cruise.rcin")
            if len(self.input.missin.Cruise.wtbm) > 0:
                sb.add_var("input.missin.Cruise.wtbm")
            if len(self.input.missin.Cruise.altbm) > 0:
                sb.add_var("input.missin.Cruise.altbm")
                
            sb.add_comment("\n  ! Descent Schedule Definition")
            sb.add_var("input.missin.Descent.ivs")
            sb.add_var("input.missin.Descent.decl")
            sb.add_var("input.missin.Descent.demmin")
            sb.add_var("input.missin.Descent.demmax")
            sb.add_var("input.missin.Descent.deamin")
            sb.add_var("input.missin.Descent.deamax")
            sb.add_var("input.missin.Descent.ninde")
            sb.add_var("input.missin.Descent.dedcd")
            sb.add_var("input.missin.Descent.rdlim")
            sb.add_var("input.missin.Descent.keasvd")
            if ns > 0:
                sb.add_newvar("ns", ns)
                sb.add_var("input.missin.Descent.adtab")
                sb.add_var("input.missin.Descent.vdtab")
      
            sb.add_container("input.missin.Reserve")

            #----------------------
            # Mission definition
            #----------------------

            mission = self.input.mission_definition.mission
            
            for seg in mission:
                sb.add_group(seg)

            self.nmseg = mission.count('CLIMB') + mission.count('CRUISE') + \
                         mission.count('REFUEL') + mission.count('RELEASE') + \
                         mission.count('ACCEL') + mission.count('TURN') + \
                         mission.count('COMBAT') + mission.count('HOLD') + \
                         mission.count('DESCENT')
            
        #-------------------
        # Namelist &PCONIN
        #-------------------

        # One or more &PCONIN namelists may have been created by the user.
        if npcon > 0 and ianal == 3:
            
            for i in range(0, npcon):

                sb.add_group('PCONIN')
                sb.add_comment("\n  ! Performance Constraint")
                
                if self.get("input.pconin%s.conalt" % (i)) >= 0.:
                    sb.add_var("input.pconin%s.conalt" % (i))
                if self.get("input.pconin%s.conmch" % (i)) >= 0.:
                    sb.add_var("input.pconin%s.conmch" % (i))
                if self.get("input.pconin%s.connz" % (i)) >= 0.:
                    sb.add_var("input.pconin%s.connz" % (i))
                if self.get("input.pconin%s.conpc" % (i)) > -10.:
                    sb.add_var("input.pconin%s.conpc" % (i))
                if self.get("input.pconin%s.conlim" % (i)) != -999.:
                    sb.add_var("input.pconin%s.conlim" % (i))
                if self.get("input.pconin%s.conaux" % (i)) > -1.:
                    sb.add_var("input.pconin%s.conaux" % (i))
                if self.get("input.pconin%s.neo" % (i)) >= 0:
                    sb.add_var("input.pconin%s.neo" % (i))
                if self.get("input.pconin%s.icstdg" % (i)) >= 0:
                    sb.add_var("input.pconin%s.icstdg" % (i))
                if self.get("input.pconin%s.conwt" % (i)) >= 0.:
                    sb.add_var("input.pconin%s.conwt" % (i))
                if self.get("input.pconin%s.iconsg" % (i)) >= 0:
                    sb.add_var("input.pconin%s.iconsg" % (i))
                if self.get("input.pconin%s.confm" % (i)) >= 0.:
                    sb.add_var("input.pconin%s.confm" % (i))
                if self.get("input.pconin%s.conwta" % (i)) != -999.:
                    sb.add_var("input.pconin%s.conwta" % (i))
                if self.get("input.pconin%s.icontp" % (i)) >= 0:
                    sb.add_var("input.pconin%s.icontp" % (i))
            
        #--------------------
        # Aerodynamic data
        #--------------------
        
        # Aerodynamic data are placed in the input file if MYAERO > 0.  If MYAERO=3,
        # insert the aerodynamic data after namelist &RFHIN (below), otherwise insert
        # them here.
        
        if myaero > 0 and myaero != 3 and ianal == 3:

            # aerodat contains the raw aero data
            sb.add_group(self.input.aero_data.aerodat)

        #-------------------
        # Namelist &RFHIN
        #-------------------

        # Namelist &RFHIN is only required if MYAERO=3.
        
        elif myaero == 3:
            
            sb.add_group('RFHIN')

            mmach = len(self.input.rfhin.tmach)
            sb.add_comment("  ! Aerodynamic Data for Parabolic Drag Polars")
            sb.add_newvar("mmach", mmach)
            sb.add_container("input.rfhin")

            # If MYAERO=3, insert the aerodynamic data here.  Otherwise it may have already
            # been inserted above.
            
            # aerodat contains the raw aero data
            sb.add_group(self.input.aero_data.aerodat)

            
        #-------------------
        # Namelist &ASCLIN
        #-------------------

        # Namelist &ASCLIN is only required if MYAERO=2.
        
        if myaero == 2:
            
            sb.add_group('ASCLIN')

            sb.add_comment("  ! Scaling Data for Lift Independent Drag")
            sb.add_var("input.asclin.sref")
            sb.add_var("input.asclin.tref")
            sb.add_var("input.asclin.awetn")
            sb.add_var("input.asclin.eltot")
            sb.add_var("input.asclin.voltot")
            
            if len(self.input.asclin.awett) > 0:
                sb.add_var("input.asclin.awett")
            if len(self.input.asclin.awetw) > 0:
                sb.add_var("input.asclin.awetw")
            if len(self.input.asclin.elw) > 0:
                sb.add_var("input.asclin.elw")
            if len(self.input.asclin.volw) > 0:
                sb.add_var("input.asclin.volw")
            if len(self.input.asclin.form) > 0:
                sb.add_var("input.asclin.form")
            if len(self.input.asclin.eql) > 0:
                sb.add_var("input.asclin.eql")
                
            ncdwav = len(self.input.asclin.cdwav)
            if ncdwav > 0:
                sb.add_var("input.asclin.cdwav")
                sb.add_var("input.asclin.dcdnac")

        #-------------------
        # Namelist &TOLIN
        #-------------------

        if itakof == 1 or iland == 1 or nopro == 1:
            
            sb.add_group('TOLIN')
            
            sb.add_var("input.tolin.Basic.apa")
            sb.add_var("input.tolin.Basic.dtct")
            if self.input.tolin.Basic.swref > 0:
                sb.add_var("input.tolin.Basic.swref")
            if self.input.tolin.Basic.arret > 0:
                sb.add_var("input.tolin.Basic.arret")
            sb.add_var("input.tolin.Basic.whgt")
            sb.add_var("input.tolin.Basic.alprun")
            sb.add_var("input.tolin.Basic.tinc")
            sb.add_var("input.tolin.Basic.rollmu")
            sb.add_var("input.tolin.Basic.brakmu")
            sb.add_var("input.tolin.Basic.cdgear")
            sb.add_var("input.tolin.Basic.cdeout")
            sb.add_var("input.tolin.Basic.clspol")
            sb.add_var("input.tolin.Basic.cdspol")
            sb.add_var("input.tolin.Basic.incgef")
            sb.add_var("input.tolin.Basic.argef")
            sb.add_var("input.tolin.Basic.itime")
            
            sb.add_comment("\n  ! Thrust Reverser")
            sb.add_var("input.tolin.Thrust_Reverser.inthrv")
            sb.add_var("input.tolin.Thrust_Reverser.rvfact")
            if len(self.input.tolin.Thrust_Reverser.velrv) > 0:
                sb.add_var("input.tolin.Thrust_Reverser.velrv")
                sb.add_var("input.tolin.Thrust_Reverser.thrrv")
      
            sb.add_var("input.tolin.Thrust_Reverser.tirvrs")
            sb.add_var("input.tolin.Thrust_Reverser.revcut")
            sb.add_var("input.tolin.Thrust_Reverser.clrev")
            sb.add_var("input.tolin.Thrust_Reverser.cdrev")
            
            sb.add_comment("\n  ! Integration Intervals  (Default values will provide a precision of +/-.25 ft)")
            sb.add_container("input.tolin.Integration_Intervals")
            
            sb.add_comment("\n  ! Takeoff Data")
            if self.input.tolin.Takeoff.cltom > 0:
                sb.add_var("input.tolin.Takeoff.cltom")
            sb.add_var("input.tolin.Takeoff.cdmto")
            sb.add_var("input.tolin.Takeoff.fcdmto")
            sb.add_var("input.tolin.Takeoff.almxto")
            if self.input.tolin.Takeoff.obsto > 0:
                sb.add_var("input.tolin.Takeoff.obsto")
            sb.add_var("input.tolin.Takeoff.alpto")
            sb.add_var("input.tolin.Takeoff.clto")
            sb.add_var("input.tolin.Takeoff.cdto")
            sb.add_var("input.tolin.Takeoff.inthto")
            
            if len(self.input.tolin.Takeoff.velto) > 0:
                sb.add_var("input.tolin.Takeoff.velto")
                sb.add_var("input.tolin.Takeoff.thrto")
            if self.input.tolin.Takeoff.alprot > -99:
                sb.add_var("input.tolin.Takeoff.alprot")
                
            sb.add_var("input.tolin.Takeoff.vrotat")
            sb.add_var("input.tolin.Takeoff.vangl")
            sb.add_var("input.tolin.Takeoff.thfact")
            sb.add_var("input.tolin.Takeoff.ftocl")
            sb.add_var("input.tolin.Takeoff.ftocd")
            sb.add_var("input.tolin.Takeoff.igobs")
            sb.add_var("input.tolin.Takeoff.tdelg")
            sb.add_var("input.tolin.Takeoff.tigear")
            sb.add_var("input.tolin.Takeoff.ibal")
            sb.add_var("input.tolin.Takeoff.itxout")
            
            sb.add_comment("\n  ! Aborted Takeoff Data")
            sb.add_var("input.tolin.Takeoff.pilott")
            sb.add_var("input.tolin.Takeoff.tispa")
            sb.add_var("input.tolin.Takeoff.tibra")
            sb.add_var("input.tolin.Takeoff.tirva")
            sb.add_var("input.tolin.Takeoff.ispol")
            sb.add_var("input.tolin.Takeoff.irev")
            
            sb.add_comment("\n  ! Landing Data")
            if self.input.tolin.Landing.clldm > 0:
                sb.add_var("input.tolin.Landing.clldm")
            sb.add_var("input.tolin.Landing.cdmld")
            if self.input.tolin.Landing.fcdmld > 0:
                sb.add_var("input.tolin.Landing.fcdmld")
            sb.add_var("input.tolin.Landing.almxld")
            sb.add_var("input.tolin.Landing.obsld")
            sb.add_var("input.tolin.Landing.alpld")
            sb.add_var("input.tolin.Landing.clld")
            sb.add_var("input.tolin.Landing.cdld")
            sb.add_var("input.tolin.Landing.inthld")
            if len(self.input.tolin.Landing.velld) > 0:
                sb.add_var("input.tolin.Landing.velld")
                sb.add_var("input.tolin.Landing.thrld")

            sb.add_var("input.tolin.Landing.thrld")
            if self.input.tolin.Landing.thdry > 0:
                sb.add_var("input.tolin.Landing.thdry")
            sb.add_var("input.tolin.Landing.aprhgt")
            sb.add_var("input.tolin.Landing.aprang")
            sb.add_var("input.tolin.Landing.fldcl")
            sb.add_var("input.tolin.Landing.fldcd")
            sb.add_var("input.tolin.Landing.tdsink")
            if self.input.tolin.Landing.vangld > 0:
                sb.add_var("input.tolin.Landing.vangld")
            sb.add_var("input.tolin.Landing.noflar")
            sb.add_var("input.tolin.Landing.tispol")
            sb.add_var("input.tolin.Landing.ticut")
            sb.add_var("input.tolin.Landing.tibrak")
            sb.add_var("input.tolin.Landing.acclim")
            if self.input.tolin.Landing.magrup > 0:
                sb.add_var("input.tolin.Landing.magrup")

        #-------------------
        # Namelist &PROIN
        #-------------------

        # Namelist &PROIN is only required if NOPRO=1.
        if nopro > 0:
            
            npol = len(self.input.proin.dflap)
            
            sb.add_group('PROIN')
            sb.add_var("input.proin.npol")

            if npol > 0:
                sb.add_var("input.proin.alpro")
                sb.add_var("input.proin.clpro")
                sb.add_var("input.proin.cdpro")
                sb.add_var("input.proin.dflap")

            sb.add_var("input.proin.ntime")
            sb.add_var("input.proin.ipcmax")
            sb.add_var("input.proin.txf")
            sb.add_var("input.proin.alpmin")
            sb.add_var("input.proin.gamlim")
            
            inm = self.input.proin.inm
            if inm == 1:
                sb.add_var("input.proin.inm")
                sb.add_var("input.proin.iatr")
                sb.add_var("input.proin.fzf")
                sb.add_var("input.proin.thclmb")
                sb.add_var("input.proin.flapid")

        #-------------------
        # Namelist &SEGIN
        #-------------------

        # One or more &SEGIN namelists may have been created by the user.
        #nseg = self.nseg
        if nopro > 0 and self.nseg0 > 0:
            
            for i in range(0, self.nseg0):

                key    = self.get("input.segin%s.key" % (i))
                nflap  = self.get("input.segin%s.nflap" % (i))
                ifix   = self.get("input.segin%s.ifix" % (i))
                engscl = self.get("input.segin%s.engscl" % (i))
                afix   = self.get("input.segin%s.afix" % (i))
                gfix   = self.get("input.segin%s.gfix" % (i))
                vfix   = self.get("input.segin%s.vfix" % (i))
                hstop  = self.get("input.segin%s.hstop" % (i))
                dstop  = self.get("input.segin%s.dstop" % (i))
                tstop  = self.get("input.segin%s.tstop" % (i))
                vstop  = self.get("input.segin%s.vstop" % (i))
                hmin   = self.get("input.segin%s.hmin" % (i))
                sprate = self.get("input.segin%s.sprate" % (i))
                iplr   = self.get("input.segin%s.iplr" % (i))
                delt   = self.get("input.segin%s.delt" % (i))
                grdaeo = self.get("input.segin%s.grdaeo" % (i))
                grdoeo = self.get("input.segin%s.grdoeo" % (i))

                sb.add_group('SEGIN')
                sb.add_newvar("key", key)
                
                if nflap > 0:
                    sb.add_newvar("nflap", nflap)
                if ifix > 0:
                    sb.add_newvar("ifix", ifix)
                if engscl >= 0.:
                    sb.add_newvar("engscl", engscl)
                if afix > -10.:
                    sb.add_newvar("afix", afix)
                if gfix > -10.:
                    sb.add_newvar("gfix", gfix)
                if vfix > 0.:
                    sb.add_newvar("vfix", vfix)
                if hstop > 0.:
                    sb.add_newvar("hstop", hstop)
                if dstop > 0.:
                    sb.add_newvar("dstop", dstop)
                if tstop > 0.:
                    sb.add_newvar("tstop", tstop)
                if vstop > 0.:
                    sb.add_newvar("vstop", vstop)
                if hmin > 0.:
                    sb.add_newvar("hmin", hmin)
                if sprate >= 0.:
                    sb.add_newvar("sprate", sprate)
                if iplr >= 0.:
                    sb.add_newvar("iplr", iplr)
                if delt > 0.:
                    sb.add_newvar("delt", delt)
                if grdaeo > -1.:
                    sb.add_newvar("grdaeo", grdaeo)
                if grdoeo > -1.:
                    sb.add_newvar("grdoeo", grdoeo)

        #-------------------
        # Namelist &NOISIN
        #-------------------

        # Namelist &NOISIN is only required if NOISIN=1.
        if noise == 1:
            
            sb.add_group('NOISIN')

            sb.add_comment("\n  ! Data for Noise Calculations\n  ! Noise regulation control")
            sb.add_var("input.noisin.Basic.iepn")
            sb.add_var("input.noisin.Basic.depnt")
            sb.add_var("input.noisin.Basic.depns")
            sb.add_var("input.noisin.Basic.depnl")
            sb.add_var("input.noisin.Basic.itrade")
            
            sb.add_comment("\n  ! Noise sources to be included")
            ijet = self.input.noisin.Basic.ijet
            ifan = self.input.noisin.Basic.ifan
            icore = self.input.noisin.Basic.icore
            iturb = self.input.noisin.Basic.iturb
            iprop = self.input.noisin.Basic.iprop
            iflap = self.input.noisin.Basic.iflap
            iairf = self.input.noisin.Basic.iairf
            igear = self.input.noisin.Basic.igear
            ishld = self.input.noisin.Propagation.ishld
            ignd = self.input.noisin.Propagation.ignd
            if ijet > 0:
                sb.add_newvar("ijet", ijet)
            if ifan > 0:
                sb.add_newvar("ifan", ifan)
            if icore > 0:
                sb.add_newvar("icore", icore)
            if iturb > 0:
                sb.add_newvar("iturb", iturb)
            if iprop > 0:
                sb.add_newvar("iprop", iprop)
            if iflap > 0:
                sb.add_newvar("iflap", iflap)
            if iairf > 0:
                sb.add_newvar("iairf", iairf)
            if igear > 0:
                sb.add_newvar("igear", igear)
                
            sb.add_comment("\n  ! Noise Propagation Corrections")
            sb.add_var("input.noisin.Propagation.isupp")
            sb.add_var("input.noisin.Propagation.idop")
            sb.add_newvar("ignd", ignd)
            sb.add_var("input.noisin.Propagation.iatm")
            sb.add_var("input.noisin.Propagation.iega")
            sb.add_newvar("ishld", ishld)
            sb.add_var("input.noisin.Propagation.deldb")
            sb.add_var("input.noisin.Propagation.heng")
            sb.add_var("input.noisin.Propagation.filbw")
            sb.add_var("input.noisin.Propagation.tdi")
            sb.add_var("input.noisin.Propagation.rh")
            
            sb.add_comment("\n  ! Observer Locations")
            nob = len(self.input.noisin.Observers.xo)
            if nob > 0:
                sb.add_newvar("nob", nob)
                sb.add_var("input.noisin.Observers.xo")
                sb.add_var("input.noisin.Observers.yo")

            sb.add_var("input.noisin.Observers.zo")
            sb.add_var("input.noisin.Observers.ndprt")
            sb.add_var("input.noisin.Observers.ifoot")
            sb.add_var("input.noisin.Observers.igeom")
            if self.input.noisin.Observers.thrn > 0:
                sb.add_var("input.noisin.Observers.thrn")
                
            sb.add_var("input.noisin.Observers.icorr")
            sb.add_var("input.noisin.Observers.tcorxp")
            
            nparam = len(self.input.noisin.Engine_Parameters.aepp)
            if nparam > 0:
                sb.add_comment("\n  ! Engine Noise Parameters")
                sb.add_newvar("nparam", nparam)
                sb.add_container("input.noisin.Engine_Parameters")

            if ijet != 0:
                sb.add_comment("\n  ! Jet Noise Input Data")
                sb.add_var("input.noisin.Jet.inoz")
                sb.add_var("input.noisin.Jet.iplug")
                sb.add_var("input.noisin.Jet.islot")
                sb.add_var("input.noisin.Jet.iaz")
                sb.add_var("input.noisin.Jet.dbaz")
                sb.add_var("input.noisin.Jet.ejdop")
                sb.add_var("input.noisin.Jet.zmdc")
                sb.add_var("input.noisin.Jet.gammac")
                sb.add_var("input.noisin.Jet.gasrc")
                sb.add_var("input.noisin.Jet.annht")
                sb.add_var("input.noisin.Jet.zmdf")
                sb.add_var("input.noisin.Jet.gammap")
                sb.add_var("input.noisin.Jet.gasrf")
                sb.add_var("input.noisin.Jet.annhtf")
                if self.input.noisin.Jet.dhc > 0:
                    sb.add_var("input.noisin.Jet.dhc")
                sb.add_var("input.noisin.Jet.dhf")
                sb.add_var("input.noisin.Jet.zl2")
                sb.add_var("input.noisin.Jet.ifwd")
                sb.add_var("input.noisin.Jet.ishock")
                sb.add_var("input.noisin.Jet.zjsupp")

            if ijet == 5:
                sb.add_comment("\n  ! Jet Noise Input Data for MSjet")
                sb.add_container("input.noisin.MSJet")

            if ifan > 0:
                sb.add_comment("\n  ! Fan Noise Data")
                sb.add_var("input.noisin.Fan.igv")
                sb.add_var("input.noisin.Fan.ifd")
                sb.add_var("input.noisin.Fan.iexh")
                sb.add_var("input.noisin.Fan.nfh")
                
                if self.input.noisin.Fan.nstg > 0:
                    sb.add_var("input.noisin.Fan.nstg")
                    
                sb.add_var("input.noisin.Fan.suppin")
                sb.add_var("input.noisin.Fan.suppex")
                sb.add_var("input.noisin.Fan.methtip")
                sb.add_var("input.noisin.Fan.icomb")
                sb.add_var("input.noisin.Fan.decmpt")
                sb.add_var("input.noisin.Fan.gammaf")
                
                if self.input.noisin.Fan.nbl > 0:
                    sb.add_var("input.noisin.Fan.nbl")
                if self.input.noisin.Fan.nvan > 0:
                    sb.add_var("input.noisin.Fan.nvan")
                if self.input.noisin.Fan.fandia > 0:
                    sb.add_var("input.noisin.Fan.fandia")
                if self.input.noisin.Fan.fanhub > 0:
                    sb.add_var("input.noisin.Fan.fanhub")
                if self.input.noisin.Fan.tipmd > 0:
                    sb.add_var("input.noisin.Fan.tipmd")
                    
                sb.add_var("input.noisin.Fan.rss")
                sb.add_var("input.noisin.Fan.efdop")
                sb.add_var("input.noisin.Fan.faneff")
                
                if self.input.noisin.Fan.nbl2 > 0:
                    sb.add_var("input.noisin.Fan.nbl2")
                if self.input.noisin.Fan.nvan2 > 0:
                    sb.add_var("input.noisin.Fan.nvan2")
                if self.input.noisin.Fan.fand2 > 0:
                    sb.add_var("input.noisin.Fan.fand2")
                if self.input.noisin.Fan.tipmd2 > 0:
                    sb.add_var("input.noisin.Fan.tipmd2")
                    
                sb.add_var("input.noisin.Fan.rss2")
                sb.add_var("input.noisin.Fan.efdop2")
                sb.add_var("input.noisin.Fan.fanef2")
                    
                if self.input.noisin.Fan.trat > 0:
                    sb.add_var("input.noisin.Fan.trat")
                if igenen not in [1, -2] and self.input.noisin.Fan.prat > 0:
                    sb.add_var("input.noisin.Fan.prat")

            if icore > 0:
                sb.add_comment("\n  ! Core Noise Data")
                sb.add_var("input.noisin.Core.csupp")
                sb.add_var("input.noisin.Core.gamma")
                sb.add_var("input.noisin.Core.imod")
                if self.input.noisin.Core.dtemd > 0:
                    sb.add_var("input.noisin.Core.dtemd")
                sb.add_var("input.noisin.Core.ecdop")

            if iturb > 0:
                sb.add_comment("\n  ! Core Noise Data")
                sb.add_var("input.noisin.Turbine.tsupp")
                if self.input.noisin.Turbine.tbndia > 0:
                    sb.add_var("input.noisin.Turbine.tbndia")
                sb.add_var("input.noisin.Turbine.gear")
                sb.add_var("input.noisin.Turbine.cs")
                if self.input.noisin.Turbine.nblr > 0:
                    sb.add_var("input.noisin.Turbine.nblr")
                sb.add_var("input.noisin.Turbine.ityptb")
                sb.add_var("input.noisin.Turbine.etdop")

            if iprop > 0:
                sb.add_comment("\n  ! Propeller Noise Data")
                sb.add_container("input.noisin.Propeller")

            if ishld > 0:
                sb.add_comment("\n  ! Shielding Effects Data")
                sb.add_container("input.noisin.Shielding")

            if iflap > 0:
                sb.add_comment("\n  ! Flap Noise Data")
                sb.add_container("input.noisin.Flap_Noise")

            if iairf > 0:
                sb.add_comment("\n  ! Flap Noise Data")
                sb.add_container("input.noisin.Airframe")

            if ignd > 0:
                sb.add_comment("\n  ! Ground Reflection Effects Data")
                sb.add_var("input.noisin.Ground_Effects.itone")
                
                nht = len(self.input.noisin.Ground_Effects.dk)
                if nht > 0:
                    sb.add_newvar("nht", nht)
                    sb.add_var("input.noisin.Ground_Effects.dk")

        #-------------------
        # Namelist &SYNTIN
        #-------------------

        # Namelist &SYNTIN is only required if IOPT=3.
        if iopt == 3:
            
            sb.add_group('SYNTIN')

            if self.input.syntin.Variables.desrng > 0:
                sb.add_var("input.syntin.Variables.desrng")
            if self.input.syntin.Variables.vappr > 0:
                sb.add_var("input.syntin.Variables.vappr")
            if self.input.syntin.Variables.flto > 0:
                sb.add_var("input.syntin.Variables.flto")
            if self.input.syntin.Variables.flldg > 0:
                sb.add_var("input.syntin.Variables.flldg")
                
            sb.add_var("input.syntin.Variables.exfcap")
            if igenen == 1:
                if self.input.syntin.Variables.cdtmax > 0:
                    sb.add_var("input.syntin.Variables.cdtmax")
                if self.input.syntin.Variables.cdpmax > 0:
                    sb.add_var("input.syntin.Variables.cdpmax")
                if self.input.syntin.Variables.vjmax > 0:
                    sb.add_var("input.syntin.Variables.vjmax")
                if self.input.syntin.Variables.stmin > 0:
                    sb.add_var("input.syntin.Variables.stmin")
                if self.input.syntin.Variables.armax > 0:
                    sb.add_var("input.syntin.Variables.armax")

            sb.add_var("input.syntin.Variables.gnox")
            sb.add_var("input.syntin.Variables.roclim")
            sb.add_var("input.syntin.Variables.dhdtlm")
            sb.add_var("input.syntin.Variables.tmglim")
            sb.add_var("input.syntin.Variables.ig")
            sb.add_var("input.syntin.Variables.ibfgs")
            sb.add_var("input.syntin.Variables.itfine")
                
            sb.add_comment("\n  ! Optimization Control")
            sb.add_var("input.syntin.Optimization_Control.ndd")
            sb.add_var("input.syntin.Optimization_Control.rk")
            sb.add_var("input.syntin.Optimization_Control.fdd")
            
            if self.input.syntin.Optimization_Control.nlin > 0:
                sb.add_var("input.syntin.Optimization_Control.nlin")
                
            sb.add_var("input.syntin.Optimization_Control.nstep")
            sb.add_var("input.syntin.Optimization_Control.ef")
            sb.add_var("input.syntin.Optimization_Control.eps")
            sb.add_var("input.syntin.Optimization_Control.amult")
            sb.add_var("input.syntin.Optimization_Control.dep")
            sb.add_var("input.syntin.Optimization_Control.accux")
            sb.add_var("input.syntin.Optimization_Control.glm")
            
            if len(self.input.syntin.Optimization_Control.gfact) > 0:
                sb.add_var("input.syntin.Optimization_Control.gfact")
                
            sb.add_var("input.syntin.Optimization_Control.autscl")
            sb.add_var("input.syntin.Optimization_Control.icent")
            sb.add_var("input.syntin.Optimization_Control.rhomin")
            sb.add_var("input.syntin.Optimization_Control.rhomax")
            sb.add_var("input.syntin.Optimization_Control.rhodel")
            sb.add_var("input.syntin.Optimization_Control.itmax")
            sb.add_var("input.syntin.Optimization_Control.jprnt")
            sb.add_var("input.syntin.Optimization_Control.rdfun")
            sb.add_var("input.syntin.Optimization_Control.adfun")

        #-------------------
        # Namelist &RERUN
        #-------------------

        # One or more &RERUN namelists may have been created by the user.
        
        #nrerun = self.nrerun
        if self.nrern0 > 0:
            
            for i in range(0, self.nrern0):

                sb.add_group('RERUN')

                re_desrng = self.get("input.rerun%s.desrng" % (i))
                re_mywts  = self.get("input.rerun%s.mywts" % (i))
                re_rampwt = self.get("input.rerun%s.rampwt" % (i))
                re_dowe   = self.get("input.rerun%s.dowe" % (i))
                re_paylod = self.get("input.rerun%s.paylod" % (i))
                re_fuemax = self.get("input.rerun%s.fuemax" % (i))
                re_itakof = self.get("input.rerun%s.itakof" % (i))
                re_iland  = self.get("input.rerun%s.iland" % (i))
                re_nopro  = self.get("input.rerun%s.nopro" % (i))
                re_noise  = self.get("input.rerun%s.noise" % (i))
                re_icost  = self.get("input.rerun%s.icost" % (i))
                re_wsr    = self.get("input.rerun%s.wsr" % (i))
                re_twr    = self.get("input.rerun%s.twr" % (i))

                if re_desrng > 0.:
                    sb.add_var("input.rerun%s.desrng" % (i))
                if re_mywts >= 0:
                    sb.add_var("input.rerun%s.mywts" % (i))
                if re_rampwt >= 0.:
                    sb.add_var("input.rerun%s.rampwt" % (i))
                if re_dowe > 0.:
                    sb.add_var("input.rerun%s.dowe" % (i))
                if re_paylod > 0.:
                    sb.add_var("input.rerun%s.paylod" % (i))
                if re_fuemax > 0.:
                    sb.add_var("input.rerun%s.fuemax" % (i))
                if re_itakof == 0:
                    sb.add_var("input.rerun%s.itakof" % (i))
                if re_iland == 0:
                    sb.add_var("input.rerun%s.iland" % (i))
                if re_nopro == 0:
                    sb.add_var("input.rerun%s.nopro" % (i))
                if re_noise == 0:
                    sb.add_var("input.rerun%s.noise" % (i))
                if re_icost == 0:
                    sb.add_var("input.rerun%s.icost" % (i))
                if re_wsr == 0.:
                    sb.add_var("input.rerun%s.wsr" % (i))
                if re_twr == 0.:
                    sb.add_var("input.rerun%s.twr" % (i))

                re_indr   = self.get("input.rerun%s.missin.Basic.indr" % (i))
                re_fact   = self.get("input.rerun%s.missin.Basic.fact" % (i))
                re_fleak  = self.get("input.rerun%s.missin.Basic.fleak" % (i))
                re_fcdo   = self.get("input.rerun%s.missin.Basic.fcdo" % (i))
                re_fcdi   = self.get("input.rerun%s.missin.Basic.fcdi" % (i))
                re_fcdsub = self.get("input.rerun%s.missin.Basic.fcdsub" % (i))
                re_fcdsup = self.get("input.rerun%s.missin.Basic.fcdsup" % (i))
                re_iskal  = self.get("input.rerun%s.missin.Basic.iskal" % (i))
                re_owfact = self.get("input.rerun%s.missin.Basic.owfact" % (i))
                re_iflag  = self.get("input.rerun%s.missin.Basic.iflag" % (i))
                re_msumpt = self.get("input.rerun%s.missin.Basic.msumpt" % (i))
                re_dtc    = self.get("input.rerun%s.missin.Basic.dtc" % (i))
                re_irw    = self.get("input.rerun%s.missin.Basic.irw" % (i))
                re_rtol   = self.get("input.rerun%s.missin.Basic.rtol" % (i))
                re_nhold  = self.get("input.rerun%s.missin.Basic.nhold" % (i))
                re_iata   = self.get("input.rerun%s.missin.Basic.iata" % (i))
                re_tlwind = self.get("input.rerun%s.missin.Basic.tlwind" % (i))

                sb.add_group('MISSIN')

                if re_indr != -999:
                    sb.add_var("input.rerun%s.missin.Basic.indr" % (i))
                if re_fact != -999.:
                    sb.add_var("input.rerun%s.missin.Basic.fact" % (i))
                if re_fleak != -999.:
                    sb.add_var("input.rerun%s.missin.Basic.fleak" % (i))
                if re_fcdo != -999.:
                    sb.add_var("input.rerun%s.missin.Basic.fcdo" % (i))
                if re_fcdi != -999.:
                    sb.add_var("input.rerun%s.missin.Basic.fcdi" % (i))
                if re_fcdsub != -999.:
                    sb.add_var("input.rerun%s.missin.Basic.fcdsub" % (i))
                if re_fcdsup != -999.:
                    sb.add_var("input.rerun%s.missin.Basic.fcdsup" % (i))
                if re_iskal != -999:
                    sb.add_var("input.rerun%s.missin.Basic.iskal" % (i))
                if re_owfact != -999.:
                    sb.add_var("input.rerun%s.missin.Basic.owfact" % (i))
                if re_iflag != -999:
                    sb.add_var("input.rerun%s.missin.Basic.iflag" % (i))
                if re_msumpt != -999:
                    sb.add_var("input.rerun%s.missin.Basic.msumpt" % (i))
                if re_dtc != -999.:
                    sb.add_var("input.rerun%s.missin.Basic.dtc" % (i))
                if re_irw != -999:
                    sb.add_var("input.rerun%s.missin.Basic.irw" % (i))
                if re_rtol != -999.:
                    sb.add_var("input.rerun%s.missin.Basic.rtol" % (i))
                if re_nhold != -999:
                    sb.add_var("input.rerun%s.missin.Basic.nhold" % (i))
                if re_iata != -999:
                    sb.add_var("input.rerun%s.missin.Basic.iata" % (i))
                if re_tlwind != -999.:
                    sb.add_var("input.rerun%s.missin.Basic.tlwind" % (i))
                
                re_dwt    = self.get("input.rerun%s.missin.Basic.dwt" % (i))
                re_offdr  = self.get("input.rerun%s.missin.Basic.offdr" % (i))
                re_idoq   = self.get("input.rerun%s.missin.Basic.idoq" % (i))
                re_nsout  = self.get("input.rerun%s.missin.Basic.nsout" % (i))
                re_nsadj  = self.get("input.rerun%s.missin.Basic.nsadj" % (i))
                re_mirror = self.get("input.rerun%s.missin.Basic.mirror" % (i))
                re_stma   = self.get("input.rerun%s.missin.Store_Drag.stma" % (i))
                re_cdst   = self.get("input.rerun%s.missin.Store_Drag.cdst" % (i))
                re_istcl  = self.get("input.rerun%s.missin.Store_Drag.istcl" % (i))
                re_istcr  = self.get("input.rerun%s.missin.Store_Drag.istcr" % (i))
                re_istde  = self.get("input.rerun%s.missin.Store_Drag.istde" % (i))
                re_mywts  = self.get("input.rerun%s.missin.User_Weights.mywts" % (i))
                re_rampwt = self.get("input.rerun%s.missin.User_Weights.rampwt" % (i))
                re_dowe   = self.get("input.rerun%s.missin.User_Weights.dowe" % (i))
                re_paylod = self.get("input.rerun%s.missin.User_Weights.paylod" % (i))
                re_fuemax = self.get("input.rerun%s.missin.User_Weights.fuemax" % (i))
                re_takotm = self.get("input.rerun%s.missin.Ground_Operations.takotm" % (i))
                re_taxotm = self.get("input.rerun%s.missin.Ground_Operations.taxotm" % (i))
                re_apprtm = self.get("input.rerun%s.missin.Ground_Operations.apprtm" % (i))
                re_appfff = self.get("input.rerun%s.missin.Ground_Operations.appfff" % (i))
                re_taxitm = self.get("input.rerun%s.missin.Ground_Operations.taxitm" % (i))
                re_ittff  = self.get("input.rerun%s.missin.Ground_Operations.ittff" % (i))
                re_takoff = self.get("input.rerun%s.missin.Ground_Operations.takoff" % (i))
                re_txfufl = self.get("input.rerun%s.missin.Ground_Operations.txfufl" % (i))
                re_ftkofl = self.get("input.rerun%s.missin.Ground_Operations.ftkofl" % (i))
                re_ftxofl = self.get("input.rerun%s.missin.Ground_Operations.ftxofl" % (i))
                re_ftxifl = self.get("input.rerun%s.missin.Ground_Operations.ftxifl" % (i))
                re_faprfl = self.get("input.rerun%s.missin.Ground_Operations.faprfl" % (i))
                re_xnz    = self.get("input.rerun%s.missin.Turn_Segments.xnz" % (i))
                re_xcl    = self.get("input.rerun%s.missin.Turn_Segments.xcl" % (i))
                re_xmach  = self.get("input.rerun%s.missin.Turn_Segments.xmach" % (i))
                re_nclimb = self.get("input.rerun%s.missin.Climb.nclimb" % (i))
                re_clmmin = self.get("input.rerun%s.missin.Climb.clmmin" % (i))
                re_clmmax = self.get("input.rerun%s.missin.Climb.clmmax" % (i))
                re_clamin = self.get("input.rerun%s.missin.Climb.clamin" % (i))
                re_clamax = self.get("input.rerun%s.missin.Climb.clamax" % (i))
                re_nincl  = self.get("input.rerun%s.missin.Climb.nincl" % (i))
                re_fwf    = self.get("input.rerun%s.missin.Climb.fwf" % (i))
                re_ncrcl  = self.get("input.rerun%s.missin.Climb.ncrcl" % (i))
                re_cldcd  = self.get("input.rerun%s.missin.Climb.cldcd" % (i))
                re_ippcl  = self.get("input.rerun%s.missin.Climb.ippcl" % (i))
                re_maxcl  = self.get("input.rerun%s.missin.Climb.maxcl" % (i))
                re_no     = self.get("input.rerun%s.missin.Climb.no" % (i))
                re_keasvc = self.get("input.rerun%s.missin.Climb.keasvc" % (i))
                re_actab  = self.get("input.rerun%s.missin.Climb.actab" % (i))
                re_vctab  = self.get("input.rerun%s.missin.Climb.vctab" % (i))
                re_ifaacl = self.get("input.rerun%s.missin.Climb.ifaacl" % (i))
                re_ifaade = self.get("input.rerun%s.missin.Climb.ifaade" % (i))
                re_nodive = self.get("input.rerun%s.missin.Climb.nodive" % (i))
                re_divlim = self.get("input.rerun%s.missin.Climb.divlim" % (i))
                re_qlim   = self.get("input.rerun%s.missin.Climb.qlim" % (i))
                re_spdlim = self.get("input.rerun%s.missin.Climb.spdlim" % (i))
                re_qlalt  = self.get("input.rerun%s.missin.Climb.qlalt" % (i))
                re_vqlm   = self.get("input.rerun%s.missin.Climb.vqlm" % (i))
                re_ioc    = self.get("input.rerun%s.missin.Cruise.ioc" % (i))
                re_crmach = self.get("input.rerun%s.missin.Cruise.crmach" % (i))
                re_cralt  = self.get("input.rerun%s.missin.Cruise.cralt" % (i))
                re_crdcd  = self.get("input.rerun%s.missin.Cruise.crdcd" % (i))
                re_flrcr  = self.get("input.rerun%s.missin.Cruise.flrcr" % (i))
                re_crmmin = self.get("input.rerun%s.missin.Cruise.crmmin" % (i))
                re_crclmx = self.get("input.rerun%s.missin.Cruise.crclmx" % (i))
                re_hpmin  = self.get("input.rerun%s.missin.Cruise.hpmin" % (i))
                re_ffuel  = self.get("input.rerun%s.missin.Cruise.ffuel" % (i))
                re_fnox   = self.get("input.rerun%s.missin.Cruise.fnox" % (i))
                re_ifeath = self.get("input.rerun%s.missin.Cruise.ifeath" % (i))
                re_feathf = self.get("input.rerun%s.missin.Cruise.feathf" % (i))
                re_cdfeth = self.get("input.rerun%s.missin.Cruise.cdfeth" % (i))
                re_dcwt   = self.get("input.rerun%s.missin.Cruise.dcwt" % (i))
                re_rcin   = self.get("input.rerun%s.missin.Cruise.rcin" % (i))
                re_wtbm   = self.get("input.rerun%s.missin.Cruise.wtbm" % (i))
                re_altbm  = self.get("input.rerun%s.missin.Cruise.altbm" % (i))
                re_ivs    = self.get("input.rerun%s.missin.Descent.ivs" % (i))
                re_decl   = self.get("input.rerun%s.missin.Descent.decl" % (i))
                re_demmin = self.get("input.rerun%s.missin.Descent.demmin" % (i))
                re_demmax = self.get("input.rerun%s.missin.Descent.demmax" % (i))
                re_deamin = self.get("input.rerun%s.missin.Descent.deamin" % (i))
                re_deamax = self.get("input.rerun%s.missin.Descent.deamax" % (i))
                re_ninde  = self.get("input.rerun%s.missin.Descent.ninde" % (i))
                re_dedcd  = self.get("input.rerun%s.missin.Descent.dedcd" % (i))
                re_rdlim  = self.get("input.rerun%s.missin.Descent.rdlim" % (i))
                re_ns     = self.get("input.rerun%s.missin.Descent.ns" % (i))
                re_irs    = self.get("input.rerun%s.missin.Reserve.irs" % (i))
                re_resrfu = self.get("input.rerun%s.missin.Reserve.resrfu" % (i))
                re_restrp = self.get("input.rerun%s.missin.Reserve.restrp" % (i))
                re_timmap = self.get("input.rerun%s.missin.Reserve.timmap" % (i))
                re_altran = self.get("input.rerun%s.missin.Reserve.altran" % (i))
                re_nclres = self.get("input.rerun%s.missin.Reserve.nclres" % (i))
                re_ncrres = self.get("input.rerun%s.missin.Reserve.ncrres" % (i))
                re_sremch = self.get("input.rerun%s.missin.Reserve.sremch" % (i))
                re_eremch = self.get("input.rerun%s.missin.Reserve.eremch" % (i))
                re_srealt = self.get("input.rerun%s.missin.Reserve.srealt" % (i))
                re_erealt = self.get("input.rerun%s.missin.Reserve.erealt" % (i))
                re_holdtm = self.get("input.rerun%s.missin.Reserve.holdtm" % (i))
                re_ncrhol = self.get("input.rerun%s.missin.Reserve.ncrhol" % (i))
                re_ihopos = self.get("input.rerun%s.missin.Reserve.ihopos" % (i))
                re_icron  = self.get("input.rerun%s.missin.Reserve.icron" % (i))
                re_thold  = self.get("input.rerun%s.missin.Reserve.thold" % (i))
                re_ncrth  = self.get("input.rerun%s.missin.Reserve.ncrth" % (i))

                if re_dwt != -999.:
                    sb.add_var("input.rerun%s.missin.Basic.dwt" % (i))
                if len(re_offdr) > 0:
                    sb.add_var("input.rerun%s.missin.Basic.offdr" % (i))
                if re_idoq != -999:
                    sb.add_var("input.rerun%s.missin.Basic.idoq" % (i))
                if re_nsout != -999:
                    sb.add_var("input.rerun%s.missin.Basic.nsout" % (i))
                if re_nsadj != -999:
                    sb.add_var("input.rerun%s.missin.Basic.nsadj" % (i))
                if re_mirror != -999:
                    sb.add_var("input.rerun%s.missin.Basic.mirror" % (i))
                if len(re_stma) > 0:
                    sb.add_var("input.rerun%s.missin.Store_Drag.stma" % (i))
                if len(re_cdst) > 0:
                    sb.add_var("input.rerun%s.missin.Store_Drag.cdst" % (i))
                if len(re_istcl) > 0:
                    sb.add_var("input.rerun%s.missin.Store_Drag.istcl" % (i))
                if len(re_istcr) > 0:
                    sb.add_var("input.rerun%s.missin.Store_Drag.istcr" % (i))
                if re_istde != -999:
                    sb.add_var("input.rerun%s.missin.Store_Drag.istde" % (i))
                if re_mywts != -999:
                    sb.add_var("input.rerun%s.missin.User_Weights.mywts" % (i))
                if re_rampwt != -999.:
                    sb.add_var("input.rerun%s.missin.User_Weights.rampwt" % (i))
                if re_dowe != -999.:
                    sb.add_var("input.rerun%s.missin.User_Weights.dowe" % (i))
                if re_paylod != -999.:
                    sb.add_var("input.rerun%s.missin.User_Weights.paylod" % (i))
                if re_fuemax != -999.:
                    sb.add_var("input.rerun%s.missin.User_Weights.fuemax" % (i))
                if re_takotm != -999.:
                    sb.add_var("input.rerun%s.missin.Ground_Operations.takotm" % (i))
                if re_taxotm != -999.:
                    sb.add_var("input.rerun%s.missin.Ground_Operations.taxotm" % (i))
                if re_apprtm != -999.:
                    sb.add_var("input.rerun%s.missin.Ground_Operations.apprtm" % (i))
                if re_appfff != -999.:
                    sb.add_var("input.rerun%s.missin.Ground_Operations.appfff" % (i))
                if re_taxitm != -999.:
                    sb.add_var("input.rerun%s.missin.Ground_Operations.taxitm" % (i))
                if re_ittff != -999:
                    sb.add_var("input.rerun%s.missin.Ground_Operations.ittff" % (i))
                if re_takoff != -999.:
                    sb.add_var("input.rerun%s.missin.Ground_Operations.takoff" % (i))
                if re_txfufl != -999.:
                    sb.add_var("input.rerun%s.missin.Ground_Operations.txfufl" % (i))
                if re_ftkofl != -999.:
                    sb.add_var("input.rerun%s.missin.Ground_Operations.ftkofl" % (i))
                if re_ftxofl != -999.:
                    sb.add_var("input.rerun%s.missin.Ground_Operations.ftxofl" % (i))
                if re_ftxifl != -999.:
                    sb.add_var("input.rerun%s.missin.Ground_Operations.ftxifl" % (i))
                if re_faprfl != -999.:
                    sb.add_var("input.rerun%s.missin.Ground_Operations.faprfl" % (i))
                if len(re_xnz) > 0:
                    sb.add_var("input.rerun%s.missin.Turn_Segments.xnz" % (i))
                if len(re_xcl) > 0:
                    sb.add_var("input.rerun%s.missin.Turn_Segments.xcl" % (i))
                if len(re_xmach) > 0:
                    sb.add_var("input.rerun%s.missin.Turn_Segments.xmach" % (i))
                if re_nclimb > 0:
                    sb.add_var("input.rerun%s.missin.Climb.nclimb" % (i))
                if len(re_clmmin) > 0:
                    sb.add_var("input.rerun%s.missin.Climb.clmmin" % (i))
                if len(re_clmmax) > 0:
                    sb.add_var("input.rerun%s.missin.Climb.clmmax" % (i))
                if len(re_clamin) > 0:
                    sb.add_var("input.rerun%s.missin.Climb.clamin" % (i))
                if len(re_clamax) > 0:
                    sb.add_var("input.rerun%s.missin.Climb.clamax" % (i))
                if len(re_nincl) > 0:
                    sb.add_var("input.rerun%s.missin.Climb.nincl" % (i))
                if len(re_fwf) > 0:
                    sb.add_var("input.rerun%s.missin.Climb.fwf" % (i))
                if len(re_ncrcl) > 0:
                    sb.add_var("input.rerun%s.missin.Climb.ncrcl" % (i))
                if len(re_cldcd) > 0:
                    sb.add_var("input.rerun%s.missin.Climb.cldcd" % (i))
                if len(re_ippcl) > 0:
                    sb.add_var("input.rerun%s.missin.Climb.ippcl" % (i))
                if len(re_maxcl) > 0:
                    sb.add_var("input.rerun%s.missin.Climb.maxcl" % (i))
                if len(re_no) > 0:
                    sb.add_var("input.rerun%s.missin.Climb.no" % (i))
                if re_keasvc != -999:
                    sb.add_var("input.rerun%s.missin.Climb.keasvc" % (i))
                if len(re_actab) > 0:
                    sb.add_var2d("input.rerun%s.missin.Climb.actab" % (i))
                if len(re_vctab) > 0:
                    sb.add_var2d("input.rerun%s.missin.Climb.vctab" % (i))
                if re_ifaacl != -999:
                    sb.add_var("input.rerun%s.missin.Climb.ifaacl" % (i))
                if re_ifaade != -999:
                    sb.add_var("input.rerun%s.missin.Climb.ifaade" % (i))
                if re_nodive != -999:
                    sb.add_var("input.rerun%s.missin.Climb.nodive" % (i))
                if re_divlim != -999.:
                    sb.add_var("input.rerun%s.missin.Climb.divlim" % (i))
                if re_qlim != -999.:
                    sb.add_var("input.rerun%s.missin.Climb.qlim" % (i))
                if re_spdlim != -999.:
                    sb.add_var("input.rerun%s.missin.Climb.spdlim" % (i))
                if len(re_qlalt) > 0:
                    sb.add_var("input.rerun%s.missin.Climb.qlalt" % (i))
                if len(re_vqlm) > 0:
                    sb.add_var("input.rerun%s.missin.Climb.vqlm" % (i))
                if len(re_ioc) > 0:
                    sb.add_var("input.rerun%s.missin.Cruise.ioc" % (i))
                if len(re_crmach) > 0:
                    sb.add_var("input.rerun%s.missin.Cruise.crmach" % (i))
                if len(re_cralt) > 0:
                    sb.add_var("input.rerun%s.missin.Cruise.cralt" % (i))
                if len(re_crdcd) > 0:
                    sb.add_var("input.rerun%s.missin.Cruise.crdcd" % (i))
                if len(re_flrcr) > 0:
                    sb.add_var("input.rerun%s.missin.Cruise.flrcr" % (i))
                if len(re_crmmin) > 0:
                    sb.add_var("input.rerun%s.missin.Cruise.crmmin" % (i))
                if len(re_crclmx) > 0:
                    sb.add_var("input.rerun%s.missin.Cruise.crclmx" % (i))
                if len(re_hpmin) > 0:
                    sb.add_var("input.rerun%s.missin.Cruise.hpmin" % (i))
                if len(re_ffuel) > 0:
                    sb.add_var("input.rerun%s.missin.Cruise.ffuel" % (i))
                if len(re_fnox) > 0:
                    sb.add_var("input.rerun%s.missin.Cruise.fnox" % (i))
                if len(re_ifeath) > 0:
                    sb.add_var("input.rerun%s.missin.Cruise.ifeath" % (i))
                if len(re_feathf) > 0:
                    sb.add_var("input.rerun%s.missin.Cruise.feathf" % (i))
                if len(re_cdfeth) > 0:
                    sb.add_var("input.rerun%s.missin.Cruise.cdfeth" % (i))
                if re_dcwt != -999.:
                    sb.add_var("input.rerun%s.missin.Cruise.dcwt" % (i))
                if re_rcin != -999.:
                    sb.add_var("input.rerun%s.missin.Cruise.rcin" % (i))
                if len(re_wtbm) > 0:
                    sb.add_var("input.rerun%s.missin.Cruise.wtbm" % (i))
                if len(re_altbm) > 0:
                    sb.add_var("input.rerun%s.missin.Cruise.altbm" % (i))
                if re_ivs != -999:
                    sb.add_var("input.rerun%s.missin.Descent.ivs" % (i))
                if re_decl != -999.:
                    sb.add_var("input.rerun%s.missin.Descent.decl" % (i))
                if re_demmin != -999.:
                    sb.add_var("input.rerun%s.missin.Descent.demmin" % (i))
                if re_demmax != -999.:
                    sb.add_var("input.rerun%s.missin.Descent.demmax" % (i))
                if re_deamin != -999.:
                    sb.add_var("input.rerun%s.missin.Descent.deamin" % (i))
                if re_deamax != -999.:
                    sb.add_var("input.rerun%s.missin.Descent.deamax" % (i))
                if re_ninde != -999:
                    sb.add_var("input.rerun%s.missin.Descent.ninde" % (i))
                if re_dedcd != -999.:
                    sb.add_var("input.rerun%s.missin.Descent.dedcd" % (i))
                if re_rdlim != -999.:
                    sb.add_var("input.rerun%s.missin.Descent.rdlim" % (i))
                    
                ns = len(self.get("input.rerun%s.missin.Descent.adtab" % (i)))
                if  ns > 0:
                    sb.add_comment("\n  ! Input Descent Schedule\n")
                    sb.add_newvar('ns', ns)
                    sb.add_var("input.rerun%s.missin.Descent.keasvd" % (i))
                    sb.add_var("input.rerun%s.missin.Descent.adtab" % (i))
                    sb.add_var("input.rerun%s.missin.Descent.vdtab" % (i))

                if re_irs != -999:
                    sb.add_var("input.rerun%s.missin.Reserve.irs" % (i))
                if re_resrfu != -999.:
                    sb.add_var("input.rerun%s.missin.Reserve.resrfu" % (i))
                if re_restrp != -999.:
                    sb.add_var("input.rerun%s.missin.Reserve.restrp" % (i))
                if re_timmap != -999.:
                    sb.add_var("input.rerun%s.missin.Reserve.timmap" % (i))
                if re_altran != -999.:
                    sb.add_var("input.rerun%s.missin.Reserve.altran" % (i))
                if re_nclres != -999:
                    sb.add_var("input.rerun%s.missin.Reserve.nclres" % (i))
                if re_ncrres != -999:
                    sb.add_var("input.rerun%s.missin.Reserve.ncrres" % (i))
                if re_sremch != -999.:
                    sb.add_var("input.rerun%s.missin.Reserve.sremch" % (i))
                if re_eremch != -999.:
                    sb.add_var("input.rerun%s.missin.Reserve.eremch" % (i))
                if re_srealt != -999.:
                    sb.add_var("input.rerun%s.missin.Reserve.srealt" % (i))
                if re_erealt != -999.:
                    sb.add_var("input.rerun%s.missin.Reserve.erealt" % (i))
                if re_holdtm != -999.:
                    sb.add_var("input.rerun%s.missin.Reserve.holdtm" % (i))
                if re_ncrhol != -999:
                    sb.add_var("input.rerun%s.missin.Reserve.ncrhol" % (i))
                if re_ihopos != -999:
                    sb.add_var("input.rerun%s.missin.Reserve.ihopos" % (i))
                if re_icron != -999:
                    sb.add_var("input.rerun%s.missin.Reserve.icron" % (i))
                if re_thold != -999.:
                    sb.add_var("input.rerun%s.missin.Reserve.thold" % (i))
                if re_ncrth != -999:
                    sb.add_var("input.rerun%s.missin.Reserve.ncrth" % (i))
                sb.add_newvar("NPCON", self.npcons0[i])

                # Insert the new mission definition.
                #infile = self.get("input.rerun%s.mission" % (i)).open()
                #mission = infile.read()
                #infile.close()            
                #sb.add_comment(mission)
                
                # Get the mission definition
                
                mission = self.get("input.rerun%s.mission_definition" % i)
                
                for seg in mission:
                    sb.add_group(seg)
    
                # Insert the &PCONIN namelists
                for j in range(0, self.npcons0[i]):

                    re_conalt = self.get("input.rerun%s.pconin%s.conalt" % (i, j)) 
                    re_conmch = self.get("input.rerun%s.pconin%s.conmch" % (i, j)) 
                    re_connz  = self.get("input.rerun%s.pconin%s.connz" % (i, j)) 
                    re_conpc  = self.get("input.rerun%s.pconin%s.conpc" % (i, j)) 
                    re_conlim = self.get("input.rerun%s.pconin%s.conlim" % (i, j)) 
                    re_conaux = self.get("input.rerun%s.pconin%s.conaux" % (i, j)) 
                    re_neo    = self.get("input.rerun%s.pconin%s.neo" % (i, j)) 
                    re_icstdg = self.get("input.rerun%s.pconin%s.icstdg" % (i, j)) 
                    re_conwt  = self.get("input.rerun%s.pconin%s.conwt" % (i, j)) 
                    re_iconsg = self.get("input.rerun%s.pconin%s.iconsg" % (i, j)) 
                    re_confm  = self.get("input.rerun%s.pconin%s.confm" % (i, j)) 
                    re_conwta = self.get("input.rerun%s.pconin%s.conwta" % (i, j)) 
                    re_icontp = self.get("input.rerun%s.pconin%s.icontp" % (i, j))

                    sb.add_group('PCONIN')

                    if  re_conalt >= 0.:
                        sb.add_newvar("CONALT", re_conalt)
                    if  re_conmch >= 0.:
                        sb.add_newvar("CONMCH", re_conmch)
                    if  re_connz >= 0.:
                        sb.add_newvar("CONNZ", re_connz)
                    if  re_conpc > -10.:
                        sb.add_newvar("CONPC", re_conpc)
                    if  re_conlim != -999.:
                        sb.add_newvar("CONLIM", re_conlim)
                    if  re_conaux > -1.:
                        sb.add_newvar("CONAUX", re_conaux)
                    if  re_neo >= 0:
                        sb.append("NEO", re_neo)
                    if  re_icstdg >= 0:
                        sb.add_newvar("ICSTDG", re_icstdg)
                    if  re_conwt >= 0.:
                        sb.add_newvar("CONWT", re_conwt)
                    if  re_iconsg >= 0:
                        sb.add_newvar("ICONSG", re_iconsg)
                    if  re_confm >= 0.:
                        sb.add_newvar("CONFM", re_confm)
                    if  re_conwta != -999.:
                        sb.add_newvar("CONWTA", re_conwta)
                    if  re_icontp >= 0:
                        sb.add_newvar("ICONTP", re_icontp)
                    
        # Generate the input file for FLOPS
        sb.generate()

    def parse_output(self):
        """Parses the FLOPS output file(s) and populates the component
        outputs with the data.
        """

        out = FileParser()
        out.set_file(self.stdout)
       
        # added error check Thu Nov 15 2007
        ERROR = self.ERROR
        HINT  = self.HINT

        # Check for namelist read error
        # Throw new Exception for fatal errors
        # Continue processing for FLOPS failures (may want to return error 
        # codes to optimizers sometime in the future)
        out.set_delimiters(" ")
        
        try:
            out.mark_anchor("ERROR READING NAMELIST")
        except RuntimeError:
            pass
        else:
            ERROR = out.transfer_line(0)
            raise RuntimeError('Error during FLOPS execution.\n %s' % ERROR)

        out.reset_anchor()
        try:
            out.mark_anchor("ERROR READING AERODYNAMIC")
        except RuntimeError:
            pass
        else:
            ERROR = out.transfer_line(0)
            raise RuntimeError('Error during FLOPS execution.\n %s' % ERROR)

        out.reset_anchor()
        try:
            out.mark_anchor("* * * ENGINE DECK MISSING * * *")
        except RuntimeError:
            pass        
        else:
            ERROR = out.transfer_line(0)
            raise RuntimeError('Error during FLOPS execution.\n %s' % ERROR + \
                  '\n\nCheck links from "Engine" to "Flops". Make sure EIFILE' + \
                  'points to an existing file (default is "ENGDECK.txt" in UserDir.\n\n*****************')

        out.reset_anchor()
        try:
            out.mark_anchor("* * * ONLY ONE ALTITUDE FOR MACH NUMBER")
        except RuntimeError:
            pass        
        else:
            ERROR = out.transfer_line(0)
            
            # TODO - Why does MC wrapper do this?
            # commented out for now
            #self.output.Performance.range = 0.
            #self.output.Performance.rampwt = 0.
            #self.output.Performance.fuel = 0.
            
            raise RuntimeError('Error during FLOPS execution.\n %s' % ERROR)
            
        out.reset_anchor()
        try:
            out.mark_anchor("* * * ILLEGAL DATA IN ENGINE DECK * * *")
        except RuntimeError:
            pass
        else:
            ERROR = out.transfer_line(0)
            raise RuntimeError('Error during FLOPS execution.\n %s' % ERROR)

        out.reset_anchor()
        try:
            #out.mark_anchor("ERROR READING MISSION DEFINITION DATA FROM UNIT")
            # Loosened this up to find any read error; i've found others
            out.mark_anchor("ERROR READING")
        except RuntimeError:
            pass
        else:
            ERROR = out.transfer_line(0)
            raise RuntimeError('Error reading a file during FLOPS execution.\n %s' % ERROR)

        out.reset_anchor()
        try:
            out.mark_anchor("ERROR IN SEGMENT INPUT DATA")
        except RuntimeError:
            pass
        else:
            ERROR = out.transfer_line(0)
            raise RuntimeError('Error during FLOPS execution.\n %s' % ERROR)

        
        # Modified this section Fri Mar  5 15:05:09 EST 2010
        # there could be failures that recover during optimization

        iopt = self.input.option.Program_Control.iopt
        
        out.reset_anchor()
        try:
            if iopt != 3:
                out.mark_anchor("TITLE, BEGIN OUTPUT OF RESULTS")
            else:
                out.mark_anchor("FINAL ANALYSIS")
                
        except RuntimeError:
            
            # Check invalid results
            errorArray = [
               "* * * ENGINE DECK MISSING * * *",
               "NO WEIGHT AVAILABLE FOR FUEL",
               "FAILURE FOR CLIMB SEGMENT",
               "FAILURE FOR CRUISE CONDITION",
               "FAILURE FOR DESCENT SEGMENT",
               "ANALYSIS COULD NOT RECOVER",
               "INITIAL DESIGN UNACCEPTABLE"
               ]
            descArray = [
               "Check links from \"Engine\" to \"Flops\". Make sure EIFILE points to an existing file (default is \"ENGDECK.txt\" in UserDir",
               "Try increasing gross weight (confin.variables.GW1)",
               "Try increasing thrust and/or wing area and see flops.man",
               "Try increasing thrust and/or wing area and see flops.man",
               "Check thrust at flight idle. May need to set IDLE to 1 and see flops.man",
               "Try tweaking SYNTIN inputs to resolve this (AnalysisControl.syntin.control). Also check for other nonfatal failures like failed missed approach climb criterion.",
               "Make sure any initial design variable are within the upper and lower bounds"
               ]
            
            for i in range(0, len(errorArray)):
                try:
                    out.reset_anchor()
                    out.mark_anchor(errorArray[i])
                    ERROR = out.transfer_line(0)
                    HINT = descArray[i]
                    self.output.Performance.range = 0.
                    self.output.Performance.rampwt = 0.
                    self.output.Performance.fuel = 0.
                    break
                except RuntimeError:
                    ERROR = "None"
                    HINT = "n/a"

        
        iopt   = self.input.option.Program_Control.iopt
        ianal  = self.input.option.Program_Control.ianal
        ifite  = self.input.option.Program_Control.ifite
        mywts  = self.input.wtin.Basic.mywts
        inrtia = self.input.wtin.Inertia.inrtia
        msumpt = self.input.missin.Basic.msumpt
        noffdr = len(self.input.missin.Basic.offdr)
        
        out.reset_anchor()

        if ifite == 3:
            out.mark_anchor("PRESSURIZED CABIN DIMENSIONS FOR A")
            self.output.Geometry.BWB.xlp    = out.transfer_var(1, 5)
            self.output.Geometry.BWB.xlw    = out.transfer_var(2, 6)
            self.output.Geometry.BWB.wf     = out.transfer_var(3, 5)
            self.output.Geometry.BWB.acabin = out.transfer_var(4, 4)
            self.output.Geometry.BWB.nbaw   = out.transfer_var(5, 5)
            self.output.Geometry.BWB.bayw   = out.transfer_var(6, 5)
            self.output.Geometry.BWB.nlava  = out.transfer_var(7, 5)
            self.output.Geometry.BWB.ngally = out.transfer_var(8, 5)
            self.output.Geometry.BWB.nclset = out.transfer_var(9, 5)
            self.output.Geometry.BWB.xl     = out.transfer_var(10, 5)
            self.output.Geometry.BWB.df     = out.transfer_var(11, 5)

        out.reset_anchor()
        out.mark_anchor("FUSELAGE DATA")
        
        self.output.Geometry.xl  = out.transfer_var(2, 4)
        self.output.Geometry.wf  = out.transfer_var(3, 4)
        self.output.Geometry.df  = out.transfer_var(4, 4)
        self.output.Geometry.xlp = out.transfer_var(6, 5)

        out.reset_anchor()
        out.mark_anchor( "CREW AND PAYLOAD DATA" )

        if ifite != 1:
            self.output.Payload.npf    = out.transfer_var(1, 5)
            self.output.Payload.npb    = out.transfer_var(2, 4)
            self.output.Payload.npt    = out.transfer_var(3, 4)
            self.output.Payload.nstu   = out.transfer_var(4, 3)
            self.output.Payload.ngalc  = out.transfer_var(5, 4)
            self.output.Payload.wppass = out.transfer_var(7, 5)
            self.output.Payload.bpp    = out.transfer_var(8, 5)
            self.output.Payload.cargow = out.transfer_var(9, 5)
            self.output.Payload.cargof = out.transfer_var(10, 5)
        else:
            self.output.Payload.cargow = out.transfer_var(2, 6)
            self.output.Payload.cargof = out.transfer_var(3, 6)

        out.reset_anchor()
        out.mark_anchor( "CARGO AND BAGGAGE CONTAIN." )
        self.output.Payload.wcon = out.transfer_var(0, 6)

        if mywts == 0:
            out.reset_anchor()
            out.mark_anchor( "CREW AND BAGGAGE-FLIGHT" )
            self.output.Payload.nflcr = out.transfer_var(0, 4)
            if ifite != 1:
                self.output.Payload.nstuag = out.transfer_var(1, 2)

        if iopt == 3:
            # In optimization mode, find the last design mission
            nos = 0
            while True:
                try:
                    out.reset_anchor()
                    out.mark_anchor( "#OBJ/VAR/CONSTR SUMMARY", 
                                  noffdr+nos+1+self.nrern0 )
                except RuntimeError:
                    break
                else:
                    nos += 1
                    
            nit = noffdr + nos
        else:
            nit = nos = 1
                    
        if nit > 0:

            # Read output from the weights module

            if mywts == 0:
                
                out.reset_anchor()
                try:
                    out.mark_anchor( "WING SPAN               ", nos)
                except RuntimeError:
                    ndd = self.input.syntin.Optimization_Control.ndd
                    if ndd == 0:
                        msg = "\n\n***************** \n\n"
                        msg += "There was only one iteration in optimization mode \n\n"
                        msg += "and we happen to be looking for the final solution, which isn't there. \n\n" 
                        msg += "ndd = %" % ndd + "\n\n"
                        msg += "Try setting flops.input.syntin.Optimization_Control.ndd to 3 or 4.\n\n"
                        msg += "*****************"
                        raise RuntimeError(msg)
                    else:
                        msg = "\n\n***************** \n\n"
                        msg += "There was only one iteration in optimization mode \n\n"
                        msg += "and we happen to be looking for the final solution, which isn't there. \n\n" 
                        msg += "Something is wrong here and someone needs to figure it out before we can proceed.\n\n"
                        msg += "*****************"
                        raise RuntimeError(msg)

                self.output.Geometry.span    = out.transfer_var(0, 3)
                self.output.Geometry.glov    = out.transfer_var(1, 4)
                self.output.Geometry.sht     = out.transfer_var(3, 4)
                self.output.Geometry.svt     = out.transfer_var(5, 4)
                self.output.Geometry.xnac    = out.transfer_var(8, 3)
                self.output.Geometry.dnac    = out.transfer_var(9, 3)
                self.output.Geometry.xmlg    = out.transfer_var(11, 5)
                self.output.Geometry.xnlg    = out.transfer_var(12, 5)
            
                self.output.Weight.wldg    = out.transfer_var(14, 4)
                self.output.Weight.fultot  = out.transfer_var(19, 4)
                self.output.Weight.exsful  = out.transfer_var(20, 4)
            
                out.reset_anchor()
                out.mark_anchor( "WING BENDING FACTOR", nos)
            
                self.output.Weight.Wing.w  = out.transfer_var(0, 4)
                self.output.Weight.Wing.ew = out.transfer_var(1, 5)
                self.output.Weight.Wing.w1 = out.transfer_var(4, 3)
                self.output.Weight.Wing.w2 = out.transfer_var(5, 3)
                self.output.Weight.Wing.w3 = out.transfer_var(6, 3)
            
                # Read mass and balance summary data

                out.reset_anchor()
                out.mark_anchor( "MASS AND BALANCE SUMMARY", nos)

                if ifite == 1:
                    self.output.Weight.frwi    = out.transfer_keyvar("WING ", 2)
                    self.output.Weight.frht    = out.transfer_keyvar("HORIZONTAL TAIL ", 2)
                    self.output.Weight.frvt    = out.transfer_keyvar("VERTICAL TAIL ", 2)
                    self.output.Weight.frfin   = out.transfer_keyvar("VERTICAL FIN ", 2)
                    self.output.Weight.frcan   = out.transfer_keyvar("CANARD ", 2)
                    self.output.Weight.frfu    = out.transfer_keyvar("FUSELAGE ", 2)
                    self.output.Weight.wlg     = out.transfer_keyvar("LANDING GEAR ", 2)
                    self.output.Weight.frna    = out.transfer_keyvar("NACELLE (AIR INDUCTION) ", 2)
                    self.output.Weight.wengt   = out.transfer_keyvar("ENGINES ", 2)
                    self.output.Weight.wthr    = out.transfer_keyvar("THRUST REVERSERS ", 2)
                    self.output.Weight.wpmisc  = out.transfer_keyvar("MISCELLANEOUS SYSTEMS ", 2)
                    self.output.Weight.wfsys   = out.transfer_keyvar("FUEL SYSTEM-TANKS AND PLUMBING ", 2)
                    self.output.Weight.frsc    = out.transfer_keyvar("SURFACE CONTROLS ", 2)
                    self.output.Weight.wapu    = out.transfer_keyvar("AUXILIARY POWER ", 2)
                    self.output.Weight.win     = out.transfer_keyvar("INSTRUMENTS ", 2)
                    self.output.Weight.whyd    = out.transfer_keyvar("HYDRAULICS ", 2)
                    self.output.Weight.welec   = out.transfer_keyvar("ELECTRICAL ", 2)
                    self.output.Weight.wavonc  = out.transfer_keyvar("AVIONICS ", 2)
                    self.output.Weight.wfurn   = out.transfer_keyvar("FURNISHINGS AND EQUIPMENT ", 2)
                    self.output.Weight.wac     = out.transfer_keyvar("AIR CONDITIONING ", 2)
                    self.output.Weight.wai     = out.transfer_keyvar("AUXILIARY GEAR ", 2)
                    self.output.Weight.wempty  = out.transfer_keyvar(" WEIGHT EMPTY ", 2)
                    self.output.Weight.wflcrbw = out.transfer_keyvar("CREW AND BAGGAGE-FLIGHT,", 3)
                    self.output.Weight.wuf     = out.transfer_keyvar("UNUSABLE FUEL ", 2)
                    self.output.Weight.woil    = out.transfer_keyvar("ENGINE OIL ", 2)
                    self.output.Weight.wsrv    = out.transfer_keyvar("AMMUNITION, ETC. ", 2)
                    self.output.Weight.wbomb   = out.transfer_keyvar("AUXILIARY TANKS ", 2)
                    self.output.Weight.dowe    = out.transfer_keyvar("OPERATING WEIGHT  ", 2)
                    self.output.Weight.zfw     = out.transfer_keyvar("ZERO FUEL WEIGHT ", 2)
                else:
                    self.output.Weight.frwi    = out.transfer_keyvar("WING ", 2)
                    self.output.Weight.frht    = out.transfer_keyvar("HORIZONTAL TAIL ", 2)
                    self.output.Weight.frvt    = out.transfer_keyvar("VERTICAL TAIL ", 2)
                    self.output.Weight.frfin   = out.transfer_keyvar("VERTICAL FIN ", 2)
                    self.output.Weight.frcan   = out.transfer_keyvar("CANARD ", 2)
                    self.output.Weight.frfu    = out.transfer_keyvar("FUSELAGE ", 2)
                    self.output.Weight.wlg     = out.transfer_keyvar("LANDING GEAR ", 2)
                    self.output.Weight.frna    = out.transfer_keyvar("NACELLE (AIR INDUCTION) ", 2)
                    self.output.Weight.wengt   = out.transfer_keyvar("ENGINES ", 2)
                    self.output.Weight.wthr    = out.transfer_keyvar("THRUST REVERSERS ", 2)
                    self.output.Weight.wpmisc  = out.transfer_keyvar("MISCELLANEOUS SYSTEMS ", 2)
                    self.output.Weight.wfsys   = out.transfer_keyvar("FUEL SYSTEM-TANKS AND PLUMBING ", 2)
                    self.output.Weight.frsc    = out.transfer_keyvar("SURFACE CONTROLS ", 2)
                    self.output.Weight.wapu    = out.transfer_keyvar("AUXILIARY POWER ", 2)
                    self.output.Weight.win     = out.transfer_keyvar("INSTRUMENTS ", 2)
                    self.output.Weight.whyd    = out.transfer_keyvar("HYDRAULICS ", 2)
                    self.output.Weight.welec   = out.transfer_keyvar("ELECTRICAL ", 2)
                    self.output.Weight.wavonc  = out.transfer_keyvar("AVIONICS ", 2)
                    self.output.Weight.wfurn   = out.transfer_keyvar("FURNISHINGS AND EQUIPMENT ", 2)
                    self.output.Weight.wac     = out.transfer_keyvar("AIR CONDITIONING ", 2)
                    self.output.Weight.wai     = out.transfer_keyvar("ANTI-ICING ", 2)
                    self.output.Weight.wempty  = out.transfer_keyvar(" WEIGHT EMPTY ", 2)
                    self.output.Weight.wflcrbw = out.transfer_keyvar("CREW AND BAGGAGE-FLIGHT,", 3)
                    self.output.Weight.wwstuab = out.transfer_keyvar("-CABIN, ", 3)
                    self.output.Weight.wuf     = out.transfer_keyvar("UNUSABLE FUEL ", 2)
                    self.output.Weight.woil    = out.transfer_keyvar("ENGINE OIL ", 2)
                    self.output.Weight.wsrv    = out.transfer_keyvar("PASSENGER SERVICE ", 2)
                    self.output.Weight.dowe    = out.transfer_keyvar("OPERATING WEIGHT  ", 2)
                    self.output.Weight.zfw     = out.transfer_keyvar("ZERO FUEL WEIGHT ", 2)

                # Read inertia data

                if inrtia > 0:
                    out.reset_anchor()
                    out.mark_anchor( "#  INERTIA DATA FOR AIRCRAFT", nos)

                    nfcon = self.input.wtin.Inertia.tf.shape[0]
                    
                    self.output.Weight.Inertia.cgx = zeros(1+nfcon)
                    self.output.Weight.Inertia.cgy = zeros(1+nfcon)
                    self.output.Weight.Inertia.cgz = zeros(1+nfcon)
                    self.output.Weight.Inertia.ixxroll = zeros(1+nfcon)
                    self.output.Weight.Inertia.ixxptch = zeros(1+nfcon)
                    self.output.Weight.Inertia.ixxyaw = zeros(1+nfcon)
                    self.output.Weight.Inertia.ixz = zeros(1+nfcon)

                    out.reset_anchor()
                    out.mark_anchor( " AIRCRAFT OWE OR ZFW", 1)
                    self.output.Weight.Inertia.cgx[0]  = out.transfer_var(0, 6)
                    self.output.Weight.Inertia.cgy[0]  = out.transfer_var(0, 7)
                    self.output.Weight.Inertia.cgz[0]  = out.transfer_var(0, 8)
                    
                    out.reset_anchor()
                    out.mark_anchor( " AIRCRAFT OWE OR ZFW", 2)
                    self.output.Weight.Inertia.ixxroll[0]  = out.transfer_var(0, 5)
                    self.output.Weight.Inertia.ixxptch[0]  = out.transfer_var(0, 6)
                    self.output.Weight.Inertia.ixxyaw[0]   = out.transfer_var(0, 7)
                    self.output.Weight.Inertia.ixz[0]      = out.transfer_var(0, 8)

                    out.reset_anchor()
                    if nfcon > 0:
                        for i in range(1, nfcon+1):
                            out.mark_anchor( "INERTIA DATA FOR FUEL CONDITION" )

                            out.mark_anchor( " TOTAL WEIGHT " )
                            self.output.Weight.Inertia.cgx[i]  = out.transfer_var(0, 4)
                            self.output.Weight.Inertia.cgy[i]  = out.transfer_var(0, 5)
                            self.output.Weight.Inertia.cgz[i]  = out.transfer_var(0, 6)

                            out.mark_anchor( " TOTAL AIRCRAFT " )
                            self.output.Weight.Inertia.ixxroll[i]  = out.transfer_var(0, 3)
                            self.output.Weight.Inertia.ixxptch[i]  = out.transfer_var(0, 4)
                            self.output.Weight.Inertia.ixxyaw[i]   = out.transfer_var(0, 5)
                            self.output.Weight.Inertia.ixz[i]      = out.transfer_var(0, 6)

            else:

                # set weights to zero
                self.output.Geometry.span  = 0.0
                self.output.Geometry.glov  = 0.0
                self.output.Geometry.sht   = 0.0
                self.output.Geometry.svt   = 0.0
                self.output.Geometry.xnac  = 0.0
                self.output.Geometry.dnac  = 0.0
                self.output.Geometry.xmlg  = 0.0
                self.output.Geometry.xnlg  = 0.0
                self.output.Weight.wldg    = 0.0
                self.output.Weight.fultot  = 0.0
                self.output.Weight.exsful  = 0.0
                self.output.Weight.frwi    = 0.0
                self.output.Weight.frht    = 0.0
                self.output.Weight.frvt    = 0.0
                self.output.Weight.frfin   = 0.0
                self.output.Weight.frcan   = 0.0
                self.output.Weight.frfu    = 0.0
                self.output.Weight.wlg     = 0.0
                self.output.Weight.frna    = 0.0
                self.output.Weight.wengt   = 0.0
                self.output.Weight.wthr    = 0.0
                self.output.Weight.wpmisc  = 0.0
                self.output.Weight.wfsys   = 0.0
                self.output.Weight.frsc    = 0.0
                self.output.Weight.wapu    = 0.0
                self.output.Weight.win     = 0.0
                self.output.Weight.whyd    = 0.0
                self.output.Weight.welec   = 0.0
                self.output.Weight.wavonc  = 0.0
                self.output.Weight.wfurn   = 0.0
                self.output.Weight.wac     = 0.0
                self.output.Weight.wai     = 0.0
                self.output.Weight.wempty  = 0.0
                self.output.Weight.wflcrbw = 0.0
                self.output.Weight.wwstuab = 0.0
                self.output.Weight.wuf     = 0.0
                self.output.Weight.woil    = 0.0
                self.output.Weight.wsrv    = 0.0
                self.output.Weight.dowe    = 0.0
                self.output.Weight.zfw     = 0.0
                self.output.Weight.wbomb   = 0.0

                # inertia data
                self.output.Weight.Inertia.cgx = zeros(0)
                self.output.Weight.Inertia.cgy = zeros(0)
                self.output.Weight.Inertia.cgz = zeros(0)
                self.output.Weight.Inertia.ixxroll = zeros(0)
                self.output.Weight.Inertia.ixxptch = zeros(0)
                self.output.Weight.Inertia.ixxyaw = zeros(0)
                self.output.Weight.Inertia.ixz = zeros(0)

            # Read performance contraints summary

            if self.npcon0 > 0 and ianal == 3:
                out.reset_anchor()
                out.mark_anchor( "PERFORMANCE CONSTRAINT SUMMARY", nos)
                
                out.set_delimiters("columns")
                self.output.Performance.Constraints.constraint = out.transfer_array(4, 16, 3+self.npcon0, 29)
                self.output.Performance.Constraints.value      = out.transfer_array(4, 32, 3+self.npcon0, 40)
                self.output.Performance.Constraints.units      = out.transfer_array(4, 41, 3+self.npcon0, 47)
                self.output.Performance.Constraints.limit      = out.transfer_array(4, 48, 3+self.npcon0, 56)
                
                weight = out.transfer_array(4, 56, 3+self.npcon0, 65)
                if isinstance(weight[0], str):
                    self.output.Performance.Constraints.location   = out.transfer_array(4, 58, 3+self.npcon0, 87)
                else:
                    self.output.Performance.Constraints.weight = weight
                    self.output.Performance.Constraints.mach   = out.transfer_array(4, 66, 3+self.npcon0, 74)
                    self.output.Performance.Constraints.alt    = out.transfer_array(4, 75, 3+self.npcon0, 85)
                    self.output.Performance.Constraints.g      = out.transfer_array(4, 86, 3+self.npcon0, 98)

                out.set_delimiters(" ")
                
            # Read sizing and performance results

            if ianal == 3:
                out.reset_anchor()
                out.mark_anchor( "CONFIGURATION DATA AFTER RESIZING (IF ANY)", nit)

                self.output.Weight.dowe   = out.transfer_var(2, 4)
                self.output.Weight.paylod = out.transfer_var(3, 2)
                self.output.Weight.fuel   = out.transfer_var(4, 3)
                self.output.Weight.rampwt = out.transfer_var(5, 3)
                self.output.Weight.wsr    = out.transfer_var(8, 3)
                self.output.Weight.thrso  = out.transfer_var(10, 4)
                self.output.Weight.esf    = out.transfer_var(11, 4)
                self.output.Weight.twr    = out.transfer_var(12, 3)
                
                self.output.Performance.thrso = self.output.Weight.thrso
                self.output.Performance.esf   = self.output.Weight.esf

            # Read detailed flight segment summary

            if ianal == 3 and msumpt > 0:
                out.reset_anchor()
                out.mark_anchor( "DETAILED FLIGHT SEGMENT SUMMARY")
                
                self.output.Performance.Segments.segment = zeros(self.nmseg)
                self.output.Performance.Segments.weights = zeros(self.nmseg)
                self.output.Performance.Segments.alts = zeros(self.nmseg)
                self.output.Performance.Segments.machs = zeros(self.nmseg)
                self.output.Performance.Segments.thrusts = zeros(self.nmseg)
                self.output.Performance.Segments.totmaxs = zeros(self.nmseg)
                self.output.Performance.Segments.lods = zeros(self.nmseg)
                self.output.Performance.Segments.sfcs = zeros(self.nmseg)
                self.output.Performance.Segments.engparms = zeros(self.nmseg)
                self.output.Performance.Segments.weighte = zeros(self.nmseg)
                self.output.Performance.Segments.alte = zeros(self.nmseg)
                self.output.Performance.Segments.mache = zeros(self.nmseg)
                self.output.Performance.Segments.thruste = zeros(self.nmseg)
                self.output.Performance.Segments.totmaxe = zeros(self.nmseg)
                self.output.Performance.Segments.lode = zeros(self.nmseg)
                self.output.Performance.Segments.sfce = zeros(self.nmseg)
                self.output.Performance.Segments.engparme = zeros(self.nmseg)
                
                for i in range(0, self.nmseg):
                    if i < 9:
                        out.mark_anchor( "SEGMENT  " + str(i+1) + "   ")
                    else:
                        out.mark_anchor( "SEGMENT " + str(i+1) + "   " )

                    self.output.Performance.Segments.segment[i]  = out.transfer_var(0, 3)
                    
                    self.output.Performance.Segments.weights[i]  = out.transfer_var(5, 1)
                    self.output.Performance.Segments.alts[i]     = out.transfer_var(5, 2)
                    self.output.Performance.Segments.machs[i]    = out.transfer_var(5, 3)
                    self.output.Performance.Segments.thrusts[i]  = out.transfer_var(5, 7)
                    self.output.Performance.Segments.lods[i]     = out.transfer_var(5, 12)
                    self.output.Performance.Segments.totmaxs[i]  = out.transfer_var(6, 6)
                    self.output.Performance.Segments.sfcs[i]     = out.transfer_var(6, 7)
                    self.output.Performance.Segments.engparms[i] = out.transfer_var(6, 13)

                    # This seems a bit klugey, but it actually works.
                    j = 0
                    while True:
                        try:
                            self.output.Performance.Segments.weighte[i]  = out.transfer_var(j+5, 1)
                            self.output.Performance.Segments.alte[i]     = out.transfer_var(j+5, 2)
                            self.output.Performance.Segments.mache[i]    = out.transfer_var(j+5, 3)
                            self.output.Performance.Segments.thruste[i]  = out.transfer_var(j+5, 7)
                            self.output.Performance.Segments.lode[i]     = out.transfer_var(j+5, 12)
                            self.output.Performance.Segments.totmaxe[i]  = out.transfer_var(j+6, 6)
                            self.output.Performance.Segments.sfce[i]     = out.transfer_var(j+6, 7)
                            self.output.Performance.Segments.engparme[i] = out.transfer_var(j+6, 13)
                            
                        except ValueError:
                            break
                        
                        j += 3

                # Read the mission summary

                out.reset_anchor()
                out.mark_anchor( "M I S S I O N   S U M M A R Y", nos)

                self.output.Performance.taxofl  = out.transfer_var(5, 4)

            # Read the objective, variable and constraint summary

            out.reset_anchor()
            out.mark_anchor( "#OBJ/VAR/CONSTR SUMMARY", nos)
            out.set_delimiters("columns")

            # Changed based on Karl's fix to bug I reported
            if ianal == 3:
                
                self.output.Performance.fuel    = out.transfer_var(3, 1, 10)
                self.output.Performance.range   = out.transfer_var(3, 11, 17)
                self.output.Performance.vapp    = out.transfer_var(3, 18, 23)

                # TODO - Again, there's got to be a better way
                try:
                    self.output.Performance.faroff = out.transfer_var(3, 24, 30)
                except RuntimeError, IndexError:
                    self.output.Performance.faroff = 1.0e10
                
                self.output.Performance.farldg   = out.transfer_var(3, 31, 37)
                self.output.Performance.amfor    = out.transfer_var(3, 38, 45)
                self.output.Performance.ssfor    = out.transfer_var(3, 46, 53)
    
                self.output.Geometry.ar    = out.transfer_var(3, 65, 70)
                self.output.Geometry.sw    = out.transfer_var(3, 80, 87)
                self.output.Geometry.tr    = out.transfer_var(3, 88, 93)
                self.output.Geometry.sweep = out.transfer_var(3, 94, 99)
                self.output.Geometry.tca   = out.transfer_var(3, 100, 106)

                if self.input.wtin.Basic.vmmo > 0.:
                    self.output.Performance.vmmo = self.input.wtin.Basic.vmmo
                else:
                    self.output.Performance.vmmo = out.transfer_var(3, 107, 112)

            if self.output.Weight.fuel == 0.:
                self.output.Weight.fuel = out.transfer_var(3, 1, 10)
                
            if self.output.Weight.rampwt == 0.:
                self.output.Weight.rampwt = out.transfer_var(3, 54, 64)
                
            if self.output.Weight.thrso == 0.:
                self.output.Weight.thrso = out.transfer_var(3, 72, 78)
                self.output.Weight.thrsop = self.output.Performance.thrso
                
            if self.output.Weight.wsr == 0.:
                self.output.Weight.wsr = out.transfer_var(3, 121, 126)
                
            if self.output.Weight.twr == 0.:
                self.output.Weight.twr = out.transfer_var(3, 127, 132)
                
            out.set_delimiters(" ")
                
            # Read off-design mission data

            if ianal == 3:
                
                ndim = 1 + noffdr + self.nrern0
                self.output.Econ.sl      = zeros(ndim)
                self.output.Econ.blockt  = zeros(ndim)
                self.output.Econ.blockf  = zeros(ndim)
                self.output.Econ.blockNx = zeros(ndim)
                self.output.Econ.wpayl   = zeros(ndim)
                self.output.Econ.wgross  = zeros(ndim)
                self.output.Econ.range   = zeros(ndim)
                self.output.Econ.vapp    = zeros(ndim)
                self.output.Econ.faroff  = zeros(ndim)
                self.output.Econ.farldg  = zeros(ndim)
                self.output.Econ.amfor   = zeros(ndim)
                self.output.Econ.ssfor   = zeros(ndim)

                for i in range(0, ndim):
                    
                    out.reset_anchor()
                    out.mark_anchor( "CONFIGURATION DATA AFTER RESIZING", (nos-1)*(1 + noffdr) + 1 + i)
                    
                    self.output.Econ.wpayl[i]  = out.transfer_var(3, 2)
                    self.output.Econ.wgross[i] = out.transfer_var(5, 3)
                    
                    out.mark_anchor( "DESIGN RANGE" )
                    self.output.Econ.sl[i] = out.transfer_var(0, 3)

                    out.mark_anchor( "BLOCK TIME =" )
                    self.output.Econ.blockt[i]  = out.transfer_var(0, 4)
                    self.output.Econ.blockf[i]  = out.transfer_var(1, 4)
                    self.output.Econ.blockNx[i] = out.transfer_var(2, 6)

                    out.mark_anchor( "#OBJ/VAR/CONSTR SUMMARY" );

                    out.set_delimiters("columns")
                    self.output.Econ.range[i] = out.transfer_var(3, 11, 17)
                    self.output.Econ.vapp[i] = out.transfer_var(3, 18, 23)
                    
                    try:
                        self.output.Econ.faroff[i] = out.transfer_var(3, 24, 30)
                    except RuntimeError, IndexError:
                        self.output.Econ.faroff[i] = 1.0e10
                        
                    self.output.Econ.farldg[i] = out.transfer_var(3, 31, 37)
                    self.output.Econ.amfor[i] = out.transfer_var(3, 38, 45)
                    self.output.Econ.ssfor[i] = out.transfer_var(3, 46, 53)

                    out.set_delimiters(" ")

                    
    def add_segin(self):
        """Adds a new SEGIN namelist."""
        
        name = "segin" + str(self.nseg0)
        self.nseg0 += 1
        comp = VariableTree()

        comp.add_trait('key', Str('CHAN', desc="Key word specifying reason for end of segment"))
        comp.add_trait('nflap', Int(-1, desc="Number of drag polar to use\nIf NFLAP = -1, default value or previous value is used"))
        comp.add_trait('ifix', Int(-1, desc="Constraints for climb segments after OBSTACLE\nIf IFIX = 0, default value or previous value is used" ))
        comp.add_trait('engscl', Float(-1., desc="Engine setting as a fraction of thrust at IPCMAX\nIf ENGSCL = -1., default value or previous value is used" ))
        comp.add_trait('afix', Float(-10., units='deg', desc="Fixed angle of attack for IFIX = 3 or 6\nIf AFIX = -10., final value from previous segment is used" ))
        comp.add_trait('gfix', Float(-10., units='deg', desc="Fixed flight path angle for IFIX = 2 or 4, or fixed cabin floor angle for IFIX = 5\nIf GFIX = -10., final value from previous segment is used" ))
        comp.add_trait('vfix', Float(-1., units='nmi/h', desc="Fixed velocity for IFIX = 1, 4 or 6\nIf VFIX = -1., final value from previous segment is used" ))
        comp.add_trait('hstop', Float(-1., units='ft', desc="Segment termination altitude\nIf HSTOP = -1., default value is used" ))
        comp.add_trait('dstop', Float(-1., units='ft', desc="Segment termination distance\nIf DSTOP = -1., value from following segment is used" ))
        comp.add_trait('tstop', Float(-1., units='s', desc="Segment termination time\nIf TSTOP = -1., value from following segment is used" ))
        comp.add_trait('vstop', Float(-1., units='nmi/h', desc="Segment termination velocity\nIf VSTOP = -1., default value is used" ))
        comp.add_trait('hmin', Float(-1., units='ft', desc="Minimum altitude for segment termination; overrides STOP variables above\nIf HMIN = -1., value is not used" ))
        comp.add_trait('sprate', Float(-1., desc="Thrust reduction rate during segments where the power setting is reduced\nIf SPRATE = -1., default value or previous value is used" ))
        comp.add_trait('iplr', Int(-1, desc="Programmed lapse rate switch for this segment\nIf IPLR = -1, default value is used" ))
        comp.add_trait('noycal', Int(-1, desc="Noise calculation switch - available only for simplified noise calculations in DOSS version\nIf NOYCAL = -1, default value is used" ))
        comp.add_trait('delt', Float(-1., units='s', desc="Time step for post OBSTACLE segments\nIf DELT = -1., default value is used" ))
        comp.add_trait('grdaeo', Float(-1., units='deg', desc="Flight path angle for CUTBACK with all engines operating\nIf GRDAEO = -1., default value is used" ))
        comp.add_trait('grdoeo', Float(-1., units='deg', desc="Flight path angle for CUTBACK with one engine out\nIf GRDOEO = -1., default value is used" ))
        
        self.input.add(name, comp)
        

    def remove_segin(self):
        """Removes a SEGIN namelist. Actually, it removes the most recently added SEGIN, as per the MC wrapper."""
        
        if self.nseg0 == 0:
            raise RuntimeError('No &SEGIN namelists to remove!')
        
        self.nseg0 += -1
        name = "segin" + str(self.nseg0)
        
        self.input.remove_container(name)
        

    def add_pconin(self):
        """Method to add a pconin* group to the list of input variables.  This method
        can be invoked multiple times to add as many pconin* groups as desired.
        The first group added is input.pconin0, the second is input.pconin1, etc.
        Local var self.npcon0 keeps track of the number of groups added."""

        if self.npcon0 == 30:
            raise RuntimeError('Maximum of 30 performance constraints')

        name = "pconin" + str(self.npcon0)
        self.npcon0 += 1
        comp = VariableTree()

        comp.add_trait('conalt', Float(-1., units='ft', desc="Altitude at which constraint is to be evaluated (Default = value from preceding constraint)" ))
        comp.add_trait('conmch', Float(-1., units='nmi/h', desc="Velocity at which constraint is to be evaluated, kts.  If less than or equal to 5., assumed to be Mach number (Default = value from preceding constraint)" ))
        
        if self.npcon0 == 1:
            comp.add_trait('connz', Float(1., desc="Load factor (Nz) at which constraint is to be evaluated, G's (Default = value from preceding constraint or 1.)" ))
            comp.add_trait('conpc', Float(1., desc="Engine power setting parameter\n< 1., Fraction of maximum available thrust\n= 1., Maximum thrust at this Mach number and altitude\n> 1., Power setting for engine deck (3. would indicate the third highest thrust)\n(Default = value from preceding constraint or 1.)" ))
            comp.add_trait('icstdg', Int(0, desc="Number of store drag schedule (see Namelist $MISSIN) to be applied to this constraint (Default = value from preceding constraint or 0)" ))
        else:
            comp.add_trait('connz', Float(-1., desc="Load factor (Nz) at which constraint is to be evaluated, G's (Default = value from preceding constraint or 1.)" ))
            comp.add_trait('conpc', Float(-10., desc="Engine power setting parameter\n< 1., Fraction of maximum available thrust\n= 1., Maximum thrust at this Mach number and altitude\n> 1., Power setting for engine deck (3. would indicate the third highest thrust)\n(Default = value from preceding constraint or 1.)" ))
            comp.add_trait('icstdg', Int(-1, desc="Number of store drag schedule (see Namelist $MISSIN) to be applied to this constraint (Default = value from preceding constraint or 0)" ))

        comp.add_trait('conlim', Float(-999., desc="Constraint minimum or maximum value" ))
        comp.add_trait('conaux', Float(-1., desc="Additional constraint parameter" ))
        comp.add_trait('neo', Int(-1, desc="Number of engines operating (Default = value from preceding constraint or all)" ))
        comp.add_trait('conwt', Float(-1., units='lb', desc="Fixed weight (Default = value from preceding constraint)" ))
        comp.add_trait('iconsg', Int(-1, desc="Weight at start of mission segment ICONSG is used (Default = value from preceding constraint)" ))
        comp.add_trait('confm', Float(-1., desc="Fuel multiplier or fraction of fuel burned (Default = value from preceding constraint)" ))
        comp.add_trait('conwta', Float(-999., units='lb', desc="Delta weight (Default = value from preceding constraint)" ))
        comp.add_trait('icontp', Enum(-1, (-1,5,6,7,8,9,10,11,12,13,16,17,20,30), desc="Type of constraint (Default = value from preceding constraint)", \
                                      aliases=("Previous","Min. climb rate","Max. time-to-climb","Max. time-to-distance","Min. sustained load factor","Min. instant. load factor","Min. turn rate","Max. turn radius","Min. excess energy","Min. climb ceiling","Max. accel./decel. time","Min. max. speed","Min. energy bleed rate","Min. thrust margin")))
            
        self.input.add(name, comp)
        

    def remove_pconin(self):
        """Removes a PCONIN namelist. Actually, it removes the most recently added PCONIN, as per the MC wrapper."""
        
        if self.npcon0 == 0:
            raise RuntimeError('No &PCONIN namelists to remove!')
        
        self.npcon0 += -1
        name = "pconin" + str(self.npcon0)
        
        self.input.remove_container(name)
        

    def add_rerunpconin(self, i):
        """Method to add a pconin* group to the list of input variables, within an
        existing rerun* group .  This method can be invoked multiple times to add
        as many pconin* groups as desired.  Local array self.npcons keeps track of the
        number of groups added to each rerun*."""

        if self.npcons0[i] == 30:
            raise RuntimeError('Maximum of 30 performance constraints')
        
        rerun_name = "rerun" + str(i)
        
        if not hasattr(self.input,rerun_name):
            raise RuntimeError('Attempted to add a PCONIN group to a nonexistant RERUN group')

        name = "pconin" + str(self.npcons0[i])
        self.npcons0[i] += 1
        comp = VariableTree()

        comp.add_trait('conalt', Float(-1., units='ft', desc="Altitude at which constraint is to be evaluated (Default = value from preceding constraint)" ))
        comp.add_trait('conmch', Float(-1., units='nmi/h', desc="Velocity at which constraint is to be evaluated, kts.  If less than or equal to 5., assumed to be Mach number (Default = value from preceding constraint)" ))
        comp.add_trait('connz', Float(-1., desc="Load factor (Nz) at which constraint is to be evaluated, G's (Default = value from preceding constraint or 1.)" ))
        comp.add_trait('conpc', Float(-10., desc="Engine power setting parameter\n< 1., Fraction of maximum available thrust\n= 1., Maximum thrust at this Mach number and altitude\n> 1., Power setting for engine deck (3. would indicate the third highest thrust)\n(Default = value from preceding constraint or 1.)" ))
        comp.add_trait('icstdg', Int(-1, desc="Number of store drag schedule (see Namelist $MISSIN) to be applied to this constraint (Default = value from preceding constraint or 0)" ))
        comp.add_trait('conlim', Float(-999., desc="Constraint minimum or maximum value" ))
        comp.add_trait('conaux', Float(-1., desc="Additional constraint parameter" ))
        comp.add_trait('neo', Int(-1, desc="Number of engines operating (Default = value from preceding constraint or all)" ))
        comp.add_trait('conwt', Float(-1., units='lb', desc="Fixed weight (Default = value from preceding constraint)" ))
        comp.add_trait('iconsg', Int(-1, desc="Weight at start of mission segment ICONSG is used (Default = value from preceding constraint)" ))
        comp.add_trait('confm', Float(-1., desc="Fuel multiplier or fraction of fuel burned (Default = value from preceding constraint)" ))
        comp.add_trait('conwta', Float(-999., units='lb', desc="Delta weight (Default = value from preceding constraint)" ))
        comp.add_trait('icontp', Enum(-1, (-1,5,6,7,8,9,10,11,12,13,16,17,20,30), desc="Type of constraint (Default = value from preceding constraint)", \
                                      aliases=("Previous","Min. climb rate","Max. time-to-climb","Max. time-to-distance","Min. sustained load factor","Min. instant. load factor","Min. turn rate","Max. turn radius","Min. excess energy","Min. climb ceiling","Max. accel./decel. time","Min. max. speed","Min. energy bleed rate","Min. thrust margin")))

        temp = getattr(self.input, rerun_name)
        temp.add(name, comp)
        

    def remove_rerunpconin(self, i):
        """Removes a PCONIN from an existing RERUN group. Actually, it removes
        the most recently added PCONIN, as per the MC wrapper."""
        
        if self.npcons0[i] == 0:
            raise RuntimeError('No &PCONIN namelists to remove!')
        
        self.npcons0[i] += -1
        rerun_name = "rerun" + str(i)
        
        if not hasattr(self.input,rerun_name):
            raise RuntimeError('Attempted to remove a PCONIN group to a nonexistant RERUN group')

        name = "pconin" + str(self.npcons0[i])
        
        temp = getattr(self.input, rerun_name)
        temp.remove_container(name)
        

    def add_rerun(self):
        """ Method to add a rerun* group to the list of input variables.  This method
        can be invoked multiple times to add as many rerun* groups as desired.
        The first group added is input.rerun0, the second is input.rerun1, etc.
        An additional missin group and mission definition file are also created
        within the new group.  Local var self.nrern0 keeps track of the number of
        groups added."""

        name = "rerun" + str(self.nrern0)
        self.nrern0 += 1
        self.npcons0.append(0)
        comp = VariableTree()

        comp.add_trait('desrng', Float(-1., units="nmi/s" ))
        comp.add_trait('mywts', Int(-1 ))
        comp.add_trait('rampwt', Float(-1., units="lb" ))
        comp.add_trait('dowe', Float(-1., units="lb" ))
        comp.add_trait('paylod', Float(-1., units="lb" ))
        comp.add_trait('fuemax', Float(-1., units="lb" ))
        comp.add_trait('itakof', Int(-1 ))
        comp.add_trait('iland', Int(-1 ))
        comp.add_trait('nopro', Int(-1 ))
        comp.add_trait('noise', Int(-1 ))
        comp.add_trait('icost', Int(-1 ))
        comp.add_trait('wsr', Float(-1. ))
        comp.add_trait('twr', Float(-1. ))
        
        comp.add('missin', VariableTree())
        comp.missin.add('Basic', VariableTree())
        comp.missin.Basic.add_trait('indr', Int(-999 ))
        comp.missin.Basic.add_trait('fact', Float(-999. ))
        comp.missin.Basic.add_trait('fleak', Float(-999. ))
        comp.missin.Basic.add_trait('fcdo', Float(-999. ))
        comp.missin.Basic.add_trait('fcdi', Float(-999. ))
        comp.missin.Basic.add_trait('fcdsub', Float(-999. ))
        comp.missin.Basic.add_trait('fcdsup', Float(-999. ))
        comp.missin.Basic.add_trait('iskal', Int(-999 ))
        comp.missin.Basic.add_trait('owfact', Float(-999. ))
        comp.missin.Basic.add_trait('iflag', Int(-999 ))
        comp.missin.Basic.add_trait('msumpt', Int(-999 ))
        comp.missin.Basic.add_trait('dtc', Float(-999. ))
        comp.missin.Basic.add_trait('irw', Int(-999 ))
        comp.missin.Basic.add_trait('rtol', Float(-999. ))
        comp.missin.Basic.add_trait('nhold', Int(-999 ))
        comp.missin.Basic.add_trait('iata', Int(-999 ))
        comp.missin.Basic.add_trait('tlwind', Float(-999. ))
        comp.missin.Basic.add_trait('dwt', Float(-999. ))
        comp.missin.Basic.add_trait('offdr', Array(dtype=numpy_float64 ))
        comp.missin.Basic.add_trait('idoq', Int(-999 ))
        comp.missin.Basic.add_trait('nsout', Int(-999 ))
        comp.missin.Basic.add_trait('nsadj', Int(-999 ))
        comp.missin.Basic.add_trait('mirror', Int(-999 ))

        comp.missin.add('Store_Drag', VariableTree())
        comp.missin.Store_Drag.add_trait('stma', Array(dtype=numpy_float64 ))
        comp.missin.Store_Drag.add_trait('cdst', Array(dtype=numpy_float64 ))
        comp.missin.Store_Drag.add_trait('istcl', Array(dtype=numpy_float64 ))
        comp.missin.Store_Drag.add_trait('istcr', Array(dtype=numpy_float64 ))
        comp.missin.Store_Drag.add_trait('istde', Int(-999 ))

        comp.missin.add('User_Weights', VariableTree())
        comp.missin.User_Weights.add_trait('mywts', Int(-999 ))
        comp.missin.User_Weights.add_trait('rampwt', Float(-999. ))
        comp.missin.User_Weights.add_trait('dowe', Float(-999. ))
        comp.missin.User_Weights.add_trait('paylod', Float(-999. ))
        comp.missin.User_Weights.add_trait('fuemax', Float(-999. ))

        comp.missin.add('Ground_Operations', VariableTree())
        comp.missin.Ground_Operations.add_trait('takotm', Float(-999. ))
        comp.missin.Ground_Operations.add_trait('taxotm', Float(-999. ))
        comp.missin.Ground_Operations.add_trait('apprtm', Float(-999. ))
        comp.missin.Ground_Operations.add_trait('appfff', Float(-999. ))
        comp.missin.Ground_Operations.add_trait('taxitm', Float(-999. ))
        comp.missin.Ground_Operations.add_trait('ittff', Int(-999 ))
        comp.missin.Ground_Operations.add_trait('takoff', Float(-999. ))
        comp.missin.Ground_Operations.add_trait('txfufl', Float(-999. ))
        comp.missin.Ground_Operations.add_trait('ftkofl', Float(-999. ))
        comp.missin.Ground_Operations.add_trait('ftxofl', Float(-999. ))
        comp.missin.Ground_Operations.add_trait('ftxifl', Float(-999. ))
        comp.missin.Ground_Operations.add_trait('faprfl', Float(-999. ))

        comp.missin.add('Turn_Segments', VariableTree())
        comp.missin.Turn_Segments.add_trait('xnz', Array(dtype=numpy_float64 ))
        comp.missin.Turn_Segments.add_trait('xcl', Array(dtype=numpy_float64 ))
        comp.missin.Turn_Segments.add_trait('xmach', Array(dtype=numpy_float64 ))

        comp.missin.add('Climb', VariableTree())
        comp.missin.Climb.add_trait('nclimb', Int(-999))
        comp.missin.Climb.add_trait('clmmin', Array(dtype=numpy_float64 ))
        comp.missin.Climb.add_trait('clmmax', Array(dtype=numpy_float64 ))
        comp.missin.Climb.add_trait('clamin', Array(dtype=numpy_float64 ))
        comp.missin.Climb.add_trait('clamax', Array(dtype=numpy_float64 ))
        comp.missin.Climb.add_trait('nincl', Array(dtype=numpy_int64 ))
        comp.missin.Climb.add_trait('fwf', Array(dtype=numpy_float64 ))
        comp.missin.Climb.add_trait('ncrcl', Array(dtype=numpy_int64 ))
        comp.missin.Climb.add_trait('cldcd', Array(dtype=numpy_float64 ))
        comp.missin.Climb.add_trait('ippcl', Array(dtype=numpy_int64 ))
        comp.missin.Climb.add_trait('maxcl', Array(dtype=numpy_int64 ))
        comp.missin.Climb.add_trait('no', Array(dtype=numpy_int64 ))
        comp.missin.Climb.add_trait('keasvc', Int(-999 ))
        comp.missin.Climb.add_trait('actab', Array(dtype=numpy_float64 ))
        comp.missin.Climb.add_trait('vctab', Array(dtype=numpy_float64 ))
        comp.missin.Climb.add_trait('ifaacl', Int(-999 ))
        comp.missin.Climb.add_trait('ifaade', Int(-999 ))
        comp.missin.Climb.add_trait('nodive', Int(-999 ))
        comp.missin.Climb.add_trait('divlim', Float(-999. ))
        comp.missin.Climb.add_trait('qlim', Float(-999. ))
        comp.missin.Climb.add_trait('spdlim', Float(-999. ))
        comp.missin.Climb.add_trait('nql', Int(-999 ))
        comp.missin.Climb.add_trait('qlalt', Array(dtype=numpy_float64 ))
        comp.missin.Climb.add_trait('vqlm', Array(dtype=numpy_float64 ))
        
        comp.missin.add('Cruise', VariableTree())
        comp.missin.Cruise.add_trait('ncruse', Int(-999 ))
        comp.missin.Cruise.add_trait('ioc', Array(dtype=numpy_int64 ))
        comp.missin.Cruise.add_trait('crmach', Array(dtype=numpy_float64 ))
        comp.missin.Cruise.add_trait('cralt', Array(dtype=numpy_float64 ))
        comp.missin.Cruise.add_trait('crdcd', Array(dtype=numpy_float64 ))
        comp.missin.Cruise.add_trait('flrcr', Array(dtype=numpy_float64 ))
        comp.missin.Cruise.add_trait('crmmin', Array(dtype=numpy_float64 ))
        comp.missin.Cruise.add_trait('crclmx', Array(dtype=numpy_float64 ))
        comp.missin.Cruise.add_trait('hpmin', Array(dtype=numpy_float64 ))
        comp.missin.Cruise.add_trait('ffuel', Array(dtype=numpy_float64 ))
        comp.missin.Cruise.add_trait('fnox', Array(dtype=numpy_float64 ))
        comp.missin.Cruise.add_trait('ifeath', Array(dtype=numpy_int64 ))
        comp.missin.Cruise.add_trait('feathf', Array(dtype=numpy_float64 ))
        comp.missin.Cruise.add_trait('cdfeth', Array(dtype=numpy_float64 ))
        comp.missin.Cruise.add_trait('dcwt', Float(-999. ))
        comp.missin.Cruise.add_trait('rcin', Float(-999. ))
        comp.missin.Cruise.add_trait('wtbm', Array(dtype=numpy_float64 ))
        comp.missin.Cruise.add_trait('altbm', Array(dtype=numpy_float64 ))

        comp.missin.add('Descent', VariableTree())
        comp.missin.Descent.add_trait('ivs', Int(-999 ))
        comp.missin.Descent.add_trait('decl', Float(-999. ))
        comp.missin.Descent.add_trait('demmin', Float(-999. ))
        comp.missin.Descent.add_trait('demmax', Float(-999. ))
        comp.missin.Descent.add_trait('deamin', Float(-999. ))
        comp.missin.Descent.add_trait('deamax', Float(-999. ))
        comp.missin.Descent.add_trait('ninde', Int(-999 ))
        comp.missin.Descent.add_trait('dedcd', Float(-999. ))
        comp.missin.Descent.add_trait('rdlim', Float(-999. ))
        comp.missin.Descent.add_trait('ns', Int(-999 ))
        comp.missin.Descent.add_trait('keasvd', Int(-999 ))
        comp.missin.Descent.add_trait('adtab', Array(dtype=numpy_float64 ))
        comp.missin.Descent.add_trait('vdtab', Array(dtype=numpy_float64 ))

        comp.missin.add('Reserve', VariableTree())
        comp.missin.Reserve.add_trait('irs', Int(-999 ))
        comp.missin.Reserve.add_trait('resrfu', Float(-999. ))
        comp.missin.Reserve.add_trait('restrp', Float(-999. ))
        comp.missin.Reserve.add_trait('timmap', Float(-999. ))
        comp.missin.Reserve.add_trait('altran', Float(-999. ))
        comp.missin.Reserve.add_trait('nclres', Int(-999 ))
        comp.missin.Reserve.add_trait('ncrres', Int(-999 ))
        comp.missin.Reserve.add_trait('sremch', Float(-999. ))
        comp.missin.Reserve.add_trait('eremch', Float(-999. ))
        comp.missin.Reserve.add_trait('srealt', Float(-999. ))
        comp.missin.Reserve.add_trait('erealt', Float(-999. ))
        comp.missin.Reserve.add_trait('holdtm', Float(-999. ))
        comp.missin.Reserve.add_trait('ncrhol', Int(-999 ))
        comp.missin.Reserve.add_trait('ihopos', Int(-999 ))
        comp.missin.Reserve.add_trait('icron', Int(-999 ))
        comp.missin.Reserve.add_trait('thold', Float(-999. ))
        comp.missin.Reserve.add_trait('ncrth', Int(-999 ))

        # New mission definition defaults to the original one
        comp.add_trait('mission_definition', List(iotype='in'))
        comp.mission_definition = self.input.mission_definition.mission
        
        self.input.add(name, comp)


    def remove_rerun(self):
        """Removes a Rerun namelist. Actually, it removes the most recently added Rerun, as per the MC wrapper."""
        
        if self.nrern0 == 0:
            raise RuntimeError('No &PCONIN namelists to remove!')
        
        self.nrern0 += -1
        name = "rerun" + str(self.nrern0)
        
        self.input.remove_container(name)
        self.npcons0 = self.npcons0[:-1]


    def reinitialize(self):
        """Method to add pconin*, segin* and rerun* groups to the list of input
        variables.  This method can be invoked by the user to add the appropriate
        number of groups based on input variables npcon, nseg, nrerun and
        npcons[]."""

        # Add or remove an appropriate number of pconin* groups to the input variable
        # list.

        n0 = self.npcon0
        n = self.npcon
        if n > n0:
            for i in range(0,n-n0):
                self.add_pconin()
        elif n < n0:
            for i in range(0,n0-n):
                self.remove_pconin()

        # Add or remove an appropriate number of segin* groups to the input variable
        # list.

        n0 = self.nseg0
        n = self.nseg
        if n > n0:
            for i in range(0,n-n0):
                self.add_segin()
        elif n < n0:
            for i in range(0,n0-n):
                self.remove_segin()

        # Add or remove an appropriate number of rerun* groups to the input variable
        # list.

        n0 = self.nrern0
        n = self.nrerun
        if n > n0:
            for i in range(0,n-n0):
                self.add_rerun()
        elif n < n0:
            for i in range(0,n0-n):
                self.remove_rerun()

        # Add or remove an appropriate number of rerun*.pconin* groups to the input
        # variable list.
        
        for i in range(0,self.nrern0):
            n0 = self.npcons0[i]
            n = self.npcons[i]
            if n > n0:
                for j in range(0,n-n0):
                    self.add_rerunpconin(i)
            elif n < n0:
                for j in range(0,n0-n):
                    self.remove_rerunpconin(i)        
                    

    def load_model(self, filename):
        """ Loads a FLOPS model from an existing input file."""
        
        sb = Namelist(self)
        sb.set_filename(filename)
        
        # Where each namelist goes in the component
        rule_dict = { "OPTION" : ["input.option.Program_Control", \
                                  "input.option.Plot_Files", \
                                  "input.option.Excess_Power_Plot"],
                      "WTIN" : [ "input.wtin.Basic", \
                                 "input.wtin.Center_of_Gravity", \
                                 "input.wtin.Crew_Payload", \
                                 "input.wtin.Detailed_Wing", \
                                 "input.wtin.Fuel_System", \
                                 "input.wtin.Fuselage", \
                                 "input.wtin.Inertia", \
                                 "input.wtin.Landing_Gear", \
                                 "input.wtin.OEW_Calculations", \
                                 "input.wtin.Override", \
                                 "input.wtin.Propulsion", \
                                 "input.wtin.Tails_Fins", \
                                 "input.wtin.Wing_Data"],
                      "CONFIN" : ["input.confin.Basic", \
                                  "input.confin.Design_Variables", \
                                  "input.confin.Objective"],
                      "AERIN" : ["input.aerin.Basic", \
                                 "input.aerin.Internal_Aero", \
                                 "input.aerin.Takeoff_Landing"],
                      "ENGDIN" : ["input.engdin", \
                                  "input.engdin.Basic", \
                                  "input.engdin.Special_Options"],
                      "MISSIN" : ["input.missin.Basic", \
                                  "input.missin.Climb", \
                                  "input.missin.Cruise", \
                                  "input.missin.Descent", \
                                  "input.missin.Ground_Operations", \
                                  "input.missin.Reserve", \
                                  "input.missin.Store_Drag", \
                                  "input.missin.Turn_Segments", \
                                  "input.missin.User_Weights", \
                                  "input.parent"],
                      "TOLIN" : ["input.tolin.Basic", \
                                 "input.tolin.Integration_Intervals", \
                                 "input.tolin.Landing", \
                                 "input.tolin.Takeoff", \
                                 "input.tolin.Thrust_Reverser"],
                      "NOISIN" : ["input.noisin.Airframe", \
                                  "input.noisin.Basic", \
                                  "input.noisin.Core", \
                                  "input.noisin.Engine_Parameters", \
                                  "input.noisin.Fan", \
                                  "input.noisin.Flap_Noise", \
                                  "input.noisin.Ground_Effects", \
                                  "input.noisin.Jet", \
                                  "input.noisin.MSJet", \
                                  "input.noisin.Observers", \
                                  "input.noisin.Propagation", \
                                  "input.noisin.Propeller", \
                                  "input.noisin.Shielding", \
                                  "input.noisin.Turbine"],
                      "COSTIN" : ["input.costin.Basic", \
                                  "input.costin.Cost_Technology", \
                                  "input.costin.Mission_Performance"],
                      "FUSEIN" : ["input.fusein.Basic", \
                                  "input.fusein.BWB"],
                      "ENGINE" : ["input.engine", \
                                  "input.engine.Basic", \
                                  "input.engine.Design_Point", \
                                  "input.engine.Engine_Weight", \
                                  "input.engine.IC_Engine", \
                                  "input.engine.Noise_Data", \
                                  "input.engine.Other"],
                      "SYNTIN" : ["input.syntin", \
                                  "input.syntin.Variables", \
                                  "input.syntin.Optimization_Control"],
                      "ASCLIN" : ["input.asclin"],
                      "NACELL" : ["input.nacell"],
                      "PROIN"  : ["input.proin"]
                    }
                     
        # Some variables aren't exposed in the OpenMDAO wrapper (e.g., array
        # sizes which aren't needed explicitly.)
        ignore = ["netaw", "itank", "nob", "nparam", "nfcon", "npcon"]
        
        sb.parse_file()
        self.input.title = sb.title
        empty_groups, unlisted_groups, unlinked_vars = \
                    sb.load_model(rule_dict, ignore)
        
        # The pconin groups are problematic, and have not been filled because
        # they aren't created yet. We can parse the unlisted_groups to see
        # which ones are in the input-file, and then add them to the component.
        
        # Rerun, Segin, and Pconin groups also do not have unique names. We give
        # them unique names in OpenMDAO.
        num_mission = 0
        if len(unlisted_groups) > 0:
            
            for i, group in unlisted_groups.iteritems():
                
                if group.lower().count('pconin'):
                    
                    self.add_pconin()
                    rule_dict = { "PCONIN" : ["input.pconin"+str(self.npcon0-1)] }
                    
                    ne, nu, nv = sb.load_model(rule_dict, ignore, i)
                    for var in nv:
                        unlinked_vars.append(var)
                        
                elif group.lower().count('rerun'):
                    
                    self.add_rerun()
                    stem = "input.rerun"+str(self.nrern0-1)
                    rule_dict = { "RERUN" : [stem] }
                    
                    ne, nu, nv = sb.load_model(rule_dict, ignore, i)
                    for var in nv:
                        unlinked_vars.append(var)

                elif group.lower().count('segin'):
                    
                    self.add_segin()
                    stem = "input.segin"+str(self.nseg0-1)
                    rule_dict = { "SEGIN" : [stem] }
                    
                    ne, nu, nv = sb.load_model(rule_dict, ignore, i)
                    for var in nv:
                        unlinked_vars.append(var)

                # Hopefully the missin namelist always follows its associated
                # rerun group.
                elif group.lower().count('missin'):
                    
                    rule_dict = { "MISSIN" : [stem+".missin.Basic",
                                              stem+".missin.Store_Drag",
                                              stem+".missin.User_Weights",
                                              stem+".missin.Ground_Operations",
                                              stem+".missin.Turn_Segments",
                                              stem+".missin.Climb",
                                              stem+".missin.Cruise",
                                              stem+".missin.Descent",
                                              stem+".missin.Reserve",] }
                    
                    ne, nu, nv = sb.load_model(rule_dict, ignore, i)
                    for var in nv:
                        unlinked_vars.append(var)
                        
                    num_mission += 1
                        

        # Mission segments are also a challenge.
        # The remaining empty groups should be mission segments or comments.
        
        missions = []
        if len(empty_groups) > 0:
            
            in_mission = False
            for group in empty_groups.values():
                
                group_name = group.strip().split(" ")[0]
                
                if group_name.lower() == 'start':
                    missions.append('START')
                    in_mission = True
                elif group_name.lower() == 'end':
                    missions.append('END')
                    in_mission = False
                elif in_mission == True:
                    
                    groups = ['climb', 'cruise', 'refuel', 'release', 'accel', \
                              'turn', 'combat', 'hold', 'descent']
                              
                    if group_name.lower() in groups: 
                        missions.append(group.upper())
                    else:
                        print "Warning: Ignoring unknonwn mission %s" % group

            # Fist, handle the standard run missions
            mission_count = 0
            mission_start = 0
            mission_end = 0
            for i, mission in enumerate(missions):
                if mission == 'END':
                    mission_end = i
                    mission_count += i+1
                    break
                
            self.input.mission_definition.mission = missions[:mission_end+1]
            
            # Next, handle the missions in the Rerun groups
            for j in range(0,self.nrern0):
                name = "rerun" + str(j)
                mission_start = mission_end+1
                for i, mission in enumerate(missions[mission_start:]):
                    if mission == 'END':
                        mission_end = i+mission_start
                        mission_count += i+1
                        break
                    
                self.set("input.%s.mission_definition" % name, \
                           missions[mission_start:mission_end+1])
                

        # Certain data files are sometimes jammed into the input file. We have
        # to jump through some hoops to detect and import this information.
        
        ndecks = 0
        if self.input.engdin.Basic.igenen in (0, -2):
            
            found = False
            engine_deck = ""
            for i, group in enumerate(sb.groups):
                
                if group.lower().strip() == 'engdin':
                    found = True
                    
                elif found == True:
                    
                    if len(sb.cards[i]) > 0:
                        break
                    
                    engine_deck += '%s\n' % group
                    ndecks += 1
                    
            self.input.engine_deck.engdek = engine_deck

        # Aero deck seems to fall after the mission segements
        if self.input.aerin.Basic.myaero > 0 and \
           self.input.aerin.Basic.myaero != 3 and \
           self.input.option.Program_Control.ianal == 3:
            
            found = False
            aerodat = ""
            for i, group in enumerate(sb.groups):
                
                if group.lower().strip() == 'end':
                    found = True
                    
                elif found == True:
                    
                    if len(sb.cards[i]) > 0:
                        break
                    
                    aerodat += '%s\n' % group
                    ndecks += 1
                    
            self.input.aero_data.aerodat = aerodat
            
        # Post process some stuff, mostly arrays 2D arrays that come over as 1D
        
        tf = self.input.wtin.Inertia.tf
        # TODO: tf can be input with 1st dim greater than one. Need to find out
        # how that is written / parsed.
        if tf.shape[0] > 0:
            self.set('input.wtin.Inertia.tf', array([tf]))
        
        # Report diagnostics and raise any exceptions.
            
        print "Empty Groups: %d, Unhandled Groups: %d, Unlinked Vars: %d" % \
              (len(empty_groups)-len(missions)-ndecks, \
               len(unlisted_groups)-self.npcon-self.nrern0-self.nseg0-num_mission, \
               len(unlinked_vars))
        
        #print empty_groups
        #print unlisted_groups
        

if __name__ == "__main__": # pragma: no cover         

    from openmdao.main.api import set_as_top
    from numpy import array
    
    flops_comp = set_as_top(FlopsWrapper())
    flops_comp.input.option.Program_Control.mprint = 1
    flops_comp.input.title = "Testing"

    #flops_comp.npcon = 1
    #flops_comp.nseg = 3
    #flops_comp.nrerun = 2
    #flops_comp.npcons = [3, 4]
    #flops_comp.reinitialize()
    
    flops_comp.run()
    
    
    
