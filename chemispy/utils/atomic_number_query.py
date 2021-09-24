class atomic_number_query:
    elements=[
              "Hydrogen",
              "Helium",
              "Lithium",
              "Beryllium",
              "Boron",
              "Carbon",
              "Nitrogen",
              "Oxygen",
              "Fluorine",
              "Neon",
              "Sodium",
              "Magnesium",
              "Aluminum",
              "Silicon",
              "Phosphorus",
              "Sulfur",
              "Chlorine",
              "Argon",
              "Potassium",
              "Calcium",
              "Scandium",
              "Titanium",
              "Vanadium",
              "Chromium",
              "Manganese",
              "Iron",
              "Cobalt",
              "Nickle",
              "Copper",
              "Zinc",
              "Gallium",
              "Germanium",
              "Arsenic",
              "Selenium",
              "Bromine",
              "Krypton",
              "Rubidium",
              "Strontium",
              "Yttrium",
              "Zirconium",
              "Niobium",
              "Molybdenum",
              "Technetium",
              "Ruthenium",
              "Rhodium",
              "Palladium",
              "Silver",
              "Cadmium",
              "Indium",
              "Tin",
              "Antimony",
              "Tellurium",
              "Iodine",
              "Xenon",
              "Caesium",
              "Barium",
              "Lanthanum",
              "Cerium",
              "Praseodymium",
              "Neodymium",
              "Promethium",
              "Samarium",
              "Europium",
              "Gadolinium",
              "Terbium",
              "Dysprosium",
              "Holmium",
              "Erbium",
              "Thulium",
              "Ytterbium",
              "Lutetium",
              "Hafnium",
              "Tantalum",
              "Tungsten",
              "Rhenium",
              "Osmium",
              "Iridium",
              "Plantinum",
              "Gold",
              "Mercury",
              "Thallium",
              "Lead",
              "Bismuth",
              "Polonium",
              "Astatine",
              "Radon",
              "Francium",
              "Radium",
              "Actinium",
              "Thorium",
              "Protactinium",
              "Uranium",
              "Neptunium",
              "Plutonium",
              "Americium",
              "Curium",
              "Berkelium",
              "Californium",
              "Einsteinium",
              "Fermium",
              "Mendelevium",
              "Nobelium",
              "Lawrencium",
              "Rutherfordium",
              "Dubnium",
              "Seaborgium",
              "Bohrium",
              "Hassium",
              "Meitnerium",
              "Darmstadtium",
              "Roentgenium",
              "Copernicium",
              "Unutrium",
              "Flerovium",
              "Upunpetium",
              "Livermorium",
              "Ununseptium",
              "Ununocium"
              ]
class query:
    def list_types():
        return atomic_number_query.elements
    def query_atomic_number( atomic_number = 1):
        atomic_query_range = range(1,119)
        if atomic_number not in atomic_query_range:
            print("Chem: Atomic number is not within the atomic query range!")
            exit(1)
        else:
            return atomic_number_query.elements[atomic_number-1]
            
            