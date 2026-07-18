# ==========================================================
# Plant Disease Knowledge Base
# Part 1
# Crops:
# Apple
# Blueberry
# Cherry
# ==========================================================

CLASS_NAMES = [

    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",

    "Blueberry___healthy",

    "Cherry_(including_sour)___Powdery_mildew",
    "Cherry_(including_sour)___healthy",

    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy",

    "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Grape___healthy",

    "Orange___Haunglongbing_(Citrus_greening)",

    "Peach___Bacterial_spot",
    "Peach___healthy",

    "Pepper,_bell___Bacterial_spot",
    "Pepper,_bell___healthy",

    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",

    "Raspberry___healthy",

    "Soybean___healthy",

    "Squash___Powdery_mildew",

    "Strawberry___Leaf_scorch",
    "Strawberry___healthy",

    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy"
]


DISEASE_INFO = {

    # ======================================================
    # APPLE
    # ======================================================

    "Apple___Apple_scab": {
        "crop": "Apple",
        "status": "Diseased",
        "disease": "Apple Scab",
        "severity": "Medium",
        "description":
            "Apple scab is one of the most common fungal diseases affecting apple trees. It infects leaves, fruits, and young shoots, reducing fruit quality and yield.",

        "symptoms": [
            "Olive-green or dark brown spots on leaves",
            "Velvety lesions on fruits",
            "Premature leaf drop",
            "Cracked and deformed apples"
        ],

        "causes": [
            "Venturia inaequalis fungus",
            "Wet spring weather",
            "Poor air circulation",
            "Infected fallen leaves"
        ],

        "prevention": [
            "Prune trees regularly",
            "Remove infected leaves",
            "Maintain proper spacing",
            "Use resistant apple varieties"
        ],

        "treatment": [
            "Apply fungicides during early growth",
            "Remove infected fruits",
            "Practice orchard sanitation"
        ]
    },

    "Apple___Black_rot": {

        "crop": "Apple",

        "status": "Diseased",

        "disease": "Black Rot",

        "severity": "High",

        "description":
            "Black rot is a destructive fungal disease that affects leaves, fruits, and branches of apple trees.",

        "symptoms": [
            "Purple spots on leaves",
            "Black rotten fruits",
            "Cankers on branches",
            "Leaf yellowing"
        ],

        "causes": [
            "Botryosphaeria obtusa fungus",
            "Warm humid weather",
            "Dead wood in orchard"
        ],

        "prevention": [
            "Remove dead branches",
            "Prune infected wood",
            "Maintain orchard hygiene"
        ],

        "treatment": [
            "Copper fungicides",
            "Protective fungicide sprays",
            "Destroy infected fruits"
        ]
    },

    "Apple___Cedar_apple_rust": {

        "crop": "Apple",

        "status": "Diseased",

        "disease": "Cedar Apple Rust",

        "severity": "Medium",

        "description":
            "A fungal disease requiring both apple and cedar trees to complete its life cycle.",

        "symptoms": [
            "Bright orange leaf spots",
            "Yellow halos",
            "Premature defoliation"
        ],

        "causes": [
            "Gymnosporangium juniperi-virginianae",
            "Nearby cedar trees"
        ],

        "prevention": [
            "Plant resistant cultivars",
            "Remove nearby infected cedar galls"
        ],

        "treatment": [
            "Apply fungicide before infection",
            "Remove infected leaves"
        ]
    },

    "Apple___healthy": {

        "crop": "Apple",

        "status": "Healthy",

        "disease": "Healthy Plant",

        "severity": "None",

        "description":
            "The apple plant appears healthy with no visible disease symptoms.",

        "symptoms": [
            "Healthy green foliage",
            "Normal fruit growth"
        ],

        "causes": [
            "Good agricultural practices"
        ],

        "prevention": [
            "Continue proper irrigation",
            "Regular pruning",
            "Balanced fertilization"
        ],

        "treatment": [
            "No treatment required"
        ]
    },

    # ======================================================
    # BLUEBERRY
    # ======================================================

    "Blueberry___healthy": {

        "crop": "Blueberry",

        "status": "Healthy",

        "disease": "Healthy Plant",

        "severity": "None",

        "description":
            "The blueberry plant appears healthy without visible disease.",

        "symptoms": [
            "Dark green leaves",
            "Healthy berry production"
        ],

        "causes": [
            "Proper plant management"
        ],

        "prevention": [
            "Maintain soil acidity",
            "Adequate watering",
            "Regular inspection"
        ],

        "treatment": [
            "No treatment required"
        ]
    },

    # ======================================================
    # CHERRY
    # ======================================================

    "Cherry_(including_sour)___Powdery_mildew": {

        "crop": "Cherry",

        "status": "Diseased",

        "disease": "Powdery Mildew",

        "severity": "Medium",

        "description":
            "Powdery mildew is a fungal disease that covers leaves with a white powder-like coating, reducing photosynthesis and fruit quality.",

        "symptoms": [
            "White powdery patches",
            "Leaf curling",
            "Reduced fruit quality",
            "Stunted shoots"
        ],

        "causes": [
            "Podosphaera fungus",
            "Humid weather",
            "Poor ventilation"
        ],

        "prevention": [
            "Improve air circulation",
            "Avoid excessive nitrogen",
            "Regular pruning"
        ],

        "treatment": [
            "Sulfur fungicides",
            "Neem oil spray",
            "Remove infected leaves"
        ]
    },

    "Cherry_(including_sour)___healthy": {

        "crop": "Cherry",

        "status": "Healthy",

        "disease": "Healthy Plant",

        "severity": "None",

        "description":
            "The cherry plant is healthy with vigorous growth and no disease symptoms.",

        "symptoms": [
            "Green healthy leaves",
            "Normal flowering",
            "Healthy fruit production"
        ],

        "causes": [
            "Proper orchard management"
        ],

        "prevention": [
            "Continue routine care",
            "Monitor pests",
            "Maintain balanced nutrition"
        ],

        "treatment": [
            "No treatment required"
        ]
    },
    # ======================================================
    # CORN (MAIZE)
    # ======================================================

    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {

        "crop": "Corn (Maize)",

        "status": "Diseased",

        "disease": "Cercospora Leaf Spot (Gray Leaf Spot)",

        "severity": "Medium",

        "description":
            "Gray Leaf Spot is one of the most economically important fungal diseases of corn. It reduces the photosynthetic area of leaves, resulting in lower grain yield.",

        "symptoms": [
            "Long rectangular gray or tan lesions",
            "Lesions parallel to leaf veins",
            "Premature drying of leaves",
            "Reduced grain filling"
        ],

        "causes": [
            "Cercospora zeae-maydis fungus",
            "Warm and humid weather",
            "Continuous corn cultivation",
            "Crop residue left in the field"
        ],

        "prevention": [
            "Rotate crops",
            "Use disease-resistant hybrids",
            "Remove infected crop residues",
            "Improve field airflow"
        ],

        "treatment": [
            "Apply foliar fungicides when necessary",
            "Monitor disease progression regularly"
        ]
    },

    "Corn_(maize)___Common_rust_": {

        "crop": "Corn (Maize)",

        "status": "Diseased",

        "disease": "Common Rust",

        "severity": "Medium",

        "description":
            "Common rust is a fungal disease that appears as reddish-brown pustules on corn leaves and can reduce yield under severe infection.",

        "symptoms": [
            "Small reddish-brown pustules",
            "Yellowing around pustules",
            "Reduced photosynthesis",
            "Premature leaf aging"
        ],

        "causes": [
            "Puccinia sorghi fungus",
            "Cool temperatures",
            "High humidity"
        ],

        "prevention": [
            "Plant resistant hybrids",
            "Monitor fields regularly",
            "Avoid excessive moisture"
        ],

        "treatment": [
            "Apply fungicides if infection becomes severe",
            "Remove heavily infected plants"
        ]
    },

    "Corn_(maize)___Northern_Leaf_Blight": {

        "crop": "Corn (Maize)",

        "status": "Diseased",

        "disease": "Northern Leaf Blight",

        "severity": "High",

        "description":
            "Northern Leaf Blight is a fungal disease that causes long gray-green lesions and significantly reduces crop productivity if left unmanaged.",

        "symptoms": [
            "Long cigar-shaped lesions",
            "Gray-green leaf spots",
            "Leaf drying",
            "Reduced grain production"
        ],

        "causes": [
            "Exserohilum turcicum fungus",
            "Cool and wet conditions",
            "Infected crop debris"
        ],

        "prevention": [
            "Crop rotation",
            "Disease-resistant hybrids",
            "Proper field sanitation"
        ],

        "treatment": [
            "Use recommended fungicides",
            "Remove infected residues after harvest"
        ]
    },

    "Corn_(maize)___healthy": {

        "crop": "Corn (Maize)",

        "status": "Healthy",

        "disease": "Healthy Plant",

        "severity": "None",

        "description":
            "The corn plant appears healthy with no visible disease symptoms.",

        "symptoms": [
            "Uniform green leaves",
            "Healthy stalk",
            "Normal ear development"
        ],

        "causes": [
            "Proper crop management"
        ],

        "prevention": [
            "Continue regular monitoring",
            "Maintain balanced fertilization",
            "Use quality irrigation practices"
        ],

        "treatment": [
            "No treatment required"
        ]
    },

    # ======================================================
    # GRAPE
    # ======================================================

    "Grape___Black_rot": {

        "crop": "Grape",

        "status": "Diseased",

        "disease": "Black Rot",

        "severity": "High",

        "description":
            "Black Rot is a serious fungal disease of grapevines that affects leaves, shoots, and berries, leading to significant yield losses.",

        "symptoms": [
            "Brown circular spots with black borders",
            "Black shriveled berries (mummies)",
            "Dark lesions on shoots"
        ],

        "causes": [
            "Guignardia bidwellii fungus",
            "Warm humid conditions",
            "Overwintering infected plant debris"
        ],

        "prevention": [
            "Prune infected vines",
            "Maintain vineyard sanitation",
            "Improve air circulation"
        ],

        "treatment": [
            "Apply fungicides during the growing season",
            "Remove infected fruit clusters"
        ]
    },

    "Grape___Esca_(Black_Measles)": {

        "crop": "Grape",

        "status": "Diseased",

        "disease": "Esca (Black Measles)",

        "severity": "High",

        "description":
            "Esca is a complex trunk disease that weakens grapevines and reduces their lifespan and productivity.",

        "symptoms": [
            "Tiger-stripe leaf pattern",
            "Dark spots on berries",
            "Wood decay",
            "Sudden vine collapse"
        ],

        "causes": [
            "Multiple wood-decaying fungi",
            "Pruning wounds",
            "Older vineyards"
        ],

        "prevention": [
            "Disinfect pruning tools",
            "Protect pruning wounds",
            "Remove infected wood"
        ],

        "treatment": [
            "Prune affected branches",
            "Replace severely infected vines"
        ]
    },

    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {

        "crop": "Grape",

        "status": "Diseased",

        "disease": "Leaf Blight",

        "severity": "Medium",

        "description":
            "Leaf blight affects grape leaves, reducing the plant's ability to photosynthesize efficiently.",

        "symptoms": [
            "Irregular brown lesions",
            "Leaf curling",
            "Premature leaf drop"
        ],

        "causes": [
            "Isariopsis fungus",
            "Warm humid weather",
            "Poor vineyard ventilation"
        ],

        "prevention": [
            "Prune dense foliage",
            "Avoid overhead irrigation",
            "Maintain vineyard cleanliness"
        ],

        "treatment": [
            "Use protective fungicides",
            "Remove infected leaves"
        ]
    },

    "Grape___healthy": {

        "crop": "Grape",

        "status": "Healthy",

        "disease": "Healthy Plant",

        "severity": "None",

        "description":
            "The grapevine appears healthy with vigorous growth and no visible signs of disease.",

        "symptoms": [
            "Healthy green leaves",
            "Normal grape clusters",
            "Strong vine growth"
        ],

        "causes": [
            "Proper vineyard management"
        ],

        "prevention": [
            "Regular pruning",
            "Balanced fertilization",
            "Routine disease monitoring"
        ],

        "treatment": [
            "No treatment required"
        ]
    },
        # ======================================================
    # ORANGE
    # ======================================================

    "Orange___Haunglongbing_(Citrus_greening)": {

        "crop": "Orange",

        "status": "Diseased",

        "disease": "Huanglongbing (Citrus Greening)",

        "severity": "Very High",

        "description":
            "Huanglongbing (HLB), also known as Citrus Greening, is one of the most devastating bacterial diseases affecting citrus crops. There is currently no complete cure once a tree becomes infected.",

        "symptoms": [
            "Yellow shoots",
            "Blotchy mottled leaves",
            "Small, misshapen fruits",
            "Green patches on ripe fruits",
            "Premature fruit drop"
        ],

        "causes": [
            "Candidatus Liberibacter bacteria",
            "Asian Citrus Psyllid insect"
        ],

        "prevention": [
            "Control psyllid population",
            "Use certified disease-free nursery plants",
            "Regular orchard inspection",
            "Remove infected trees"
        ],

        "treatment": [
            "No permanent cure available",
            "Control insect vectors",
            "Nutritional management",
            "Replace severely infected trees"
        ]
    },

    # ======================================================
    # PEACH
    # ======================================================

    "Peach___Bacterial_spot": {

        "crop": "Peach",

        "status": "Diseased",

        "disease": "Bacterial Spot",

        "severity": "Medium",

        "description":
            "Bacterial spot affects peach leaves, twigs, and fruits, reducing fruit quality and market value.",

        "symptoms": [
            "Small water-soaked spots",
            "Dark lesions on leaves",
            "Fruit cracking",
            "Premature leaf drop"
        ],

        "causes": [
            "Xanthomonas arboricola pv. pruni",
            "Warm rainy weather",
            "Wind-driven rain"
        ],

        "prevention": [
            "Use resistant cultivars",
            "Avoid overhead irrigation",
            "Prune infected branches"
        ],

        "treatment": [
            "Copper bactericides",
            "Proper pruning",
            "Maintain orchard sanitation"
        ]
    },

    "Peach___healthy": {

        "crop": "Peach",

        "status": "Healthy",

        "disease": "Healthy Plant",

        "severity": "None",

        "description":
            "The peach plant appears healthy without visible disease symptoms.",

        "symptoms": [
            "Healthy green leaves",
            "Normal fruit development",
            "Strong branch growth"
        ],

        "causes": [
            "Proper orchard management"
        ],

        "prevention": [
            "Continue regular care",
            "Balanced fertilization",
            "Routine monitoring"
        ],

        "treatment": [
            "No treatment required"
        ]
    },

    # ======================================================
    # BELL PEPPER
    # ======================================================

    "Pepper,_bell___Bacterial_spot": {

        "crop": "Bell Pepper",

        "status": "Diseased",

        "disease": "Bacterial Spot",

        "severity": "Medium",

        "description":
            "Bacterial Spot is a common disease affecting pepper plants. Severe infection may reduce both fruit quality and yield.",

        "symptoms": [
            "Dark leaf lesions",
            "Yellow halos",
            "Leaf drop",
            "Scabby fruit spots"
        ],

        "causes": [
            "Xanthomonas bacteria",
            "Warm humid conditions",
            "Contaminated seeds"
        ],

        "prevention": [
            "Use disease-free seeds",
            "Crop rotation",
            "Avoid working on wet plants"
        ],

        "treatment": [
            "Copper-based bactericides",
            "Destroy infected plants"
        ]
    },

    "Pepper,_bell___healthy": {

        "crop": "Bell Pepper",

        "status": "Healthy",

        "disease": "Healthy Plant",

        "severity": "None",

        "description":
            "The bell pepper plant appears healthy with no signs of disease.",

        "symptoms": [
            "Healthy leaves",
            "Normal flowering",
            "Healthy fruits"
        ],

        "causes": [
            "Good cultivation practices"
        ],

        "prevention": [
            "Maintain irrigation",
            "Balanced nutrients",
            "Regular pest monitoring"
        ],

        "treatment": [
            "No treatment required"
        ]
    },

    # ======================================================
    # POTATO
    # ======================================================

    "Potato___Early_blight": {

        "crop": "Potato",

        "status": "Diseased",

        "disease": "Early Blight",

        "severity": "Medium",

        "description":
            "Early Blight is a fungal disease that mainly attacks older potato leaves and can significantly reduce yield if not managed.",

        "symptoms": [
            "Brown circular lesions",
            "Concentric ring pattern",
            "Yellowing leaves",
            "Premature defoliation"
        ],

        "causes": [
            "Alternaria solani fungus",
            "Warm humid weather",
            "Poor crop rotation"
        ],

        "prevention": [
            "Practice crop rotation",
            "Avoid overhead watering",
            "Remove infected debris"
        ],

        "treatment": [
            "Apply chlorothalonil",
            "Apply mancozeb",
            "Remove infected leaves"
        ]
    },

    "Potato___Late_blight": {

        "crop": "Potato",

        "status": "Diseased",

        "disease": "Late Blight",

        "severity": "Very High",

        "description":
            "Late Blight is one of the most destructive potato diseases. Under favorable conditions it spreads rapidly and can destroy entire fields.",

        "symptoms": [
            "Large dark leaf lesions",
            "White fungal growth beneath leaves",
            "Stem infection",
            "Rotting tubers"
        ],

        "causes": [
            "Phytophthora infestans",
            "Cool humid weather",
            "Persistent rainfall"
        ],

        "prevention": [
            "Plant certified seed potatoes",
            "Improve field drainage",
            "Monitor crop regularly"
        ],

        "treatment": [
            "Metalaxyl fungicide",
            "Copper fungicides",
            "Destroy infected plants"
        ]
    },

    "Potato___healthy": {

        "crop": "Potato",

        "status": "Healthy",

        "disease": "Healthy Plant",

        "severity": "None",

        "description":
            "The potato plant appears healthy with vigorous foliage and no visible disease symptoms.",

        "symptoms": [
            "Green healthy leaves",
            "Strong stem growth",
            "Healthy tuber development"
        ],

        "causes": [
            "Proper field management"
        ],

        "prevention": [
            "Continue crop monitoring",
            "Balanced fertilization",
            "Maintain irrigation schedule"
        ],

        "treatment": [
            "No treatment required"
        ]
    },
        # ======================================================
    # RASPBERRY
    # ======================================================

    "Raspberry___healthy": {

        "crop": "Raspberry",

        "status": "Healthy",

        "disease": "Healthy Plant",

        "severity": "None",

        "description":
            "The raspberry plant appears healthy with no visible disease symptoms. The plant shows normal leaf development and fruit production.",

        "symptoms": [
            "Bright green leaves",
            "Strong cane growth",
            "Normal berry development",
            "No visible lesions"
        ],

        "causes": [
            "Proper cultivation practices",
            "Good soil and nutrient management"
        ],

        "prevention": [
            "Maintain proper irrigation",
            "Remove old plant debris",
            "Monitor pests regularly",
            "Provide adequate sunlight"
        ],

        "treatment": [
            "No treatment required"
        ]
    },


    # ======================================================
    # SOYBEAN
    # ======================================================

    "Soybean___healthy": {

        "crop": "Soybean",

        "status": "Healthy",

        "disease": "Healthy Plant",

        "severity": "None",

        "description":
            "The soybean plant is healthy and does not show any visible signs of disease or stress.",

        "symptoms": [
            "Healthy green leaves",
            "Normal plant height",
            "Good pod formation"
        ],

        "causes": [
            "Balanced soil nutrients",
            "Proper agricultural management"
        ],

        "prevention": [
            "Use quality seeds",
            "Maintain soil fertility",
            "Practice crop rotation",
            "Regular field inspection"
        ],

        "treatment": [
            "No treatment required"
        ]
    },


    # ======================================================
    # SQUASH
    # ======================================================

    "Squash___Powdery_mildew": {

        "crop": "Squash",

        "status": "Diseased",

        "disease": "Powdery Mildew",

        "severity": "Medium",

        "description":
            "Powdery mildew is a fungal disease that affects squash leaves and reduces photosynthesis, resulting in lower plant productivity.",

        "symptoms": [
            "White powder-like patches on leaves",
            "Leaf yellowing",
            "Leaf curling",
            "Reduced plant growth"
        ],

        "causes": [
            "Powdery mildew fungi",
            "High humidity",
            "Poor air circulation",
            "Dense planting"
        ],

        "prevention": [
            "Maintain proper spacing",
            "Improve air circulation",
            "Avoid excessive nitrogen fertilizer",
            "Water plants near the soil level"
        ],

        "treatment": [
            "Apply sulfur-based fungicides",
            "Use neem oil spray",
            "Remove severely infected leaves"
        ]
    },


    # ======================================================
    # STRAWBERRY
    # ======================================================

    "Strawberry___Leaf_scorch": {

        "crop": "Strawberry",

        "status": "Diseased",

        "disease": "Leaf Scorch",

        "severity": "Medium",

        "description":
            "Leaf Scorch is a fungal disease affecting strawberry leaves and reducing plant strength and fruit production.",

        "symptoms": [
            "Purple spots on leaves",
            "Brown leaf margins",
            "Leaf drying",
            "Reduced plant growth"
        ],

        "causes": [
            "Diplocarpon earlianum fungus",
            "Warm humid conditions",
            "Infected plant debris"
        ],

        "prevention": [
            "Remove infected leaves",
            "Avoid overcrowding",
            "Improve air circulation",
            "Use disease-free plants"
        ],

        "treatment": [
            "Apply recommended fungicides",
            "Remove infected plant material",
            "Maintain proper field hygiene"
        ]
    },


    "Strawberry___healthy": {

        "crop": "Strawberry",

        "status": "Healthy",

        "disease": "Healthy Plant",

        "severity": "None",

        "description":
            "The strawberry plant appears healthy with normal growth and no visible disease symptoms.",

        "symptoms": [
            "Green healthy leaves",
            "Normal flowering",
            "Good fruit development"
        ],

        "causes": [
            "Proper cultivation practices"
        ],

        "prevention": [
            "Maintain soil health",
            "Regular pest monitoring",
            "Proper irrigation"
        ],

        "treatment": [
            "No treatment required"
        ]
    },
        # ======================================================
    # TOMATO
    # ======================================================

    "Tomato___Bacterial_spot": {

        "crop": "Tomato",

        "status": "Diseased",

        "disease": "Bacterial Spot",

        "severity": "Medium",

        "description":
            "Bacterial Spot is a common tomato disease that affects leaves, stems, and fruits. It can reduce plant health and fruit quality.",

        "symptoms": [
            "Small dark spots on leaves",
            "Yellow halos around spots",
            "Raised spots on fruits",
            "Leaf damage and drop"
        ],

        "causes": [
            "Xanthomonas bacteria",
            "Warm humid weather",
            "Contaminated seeds",
            "Water splash transmission"
        ],

        "prevention": [
            "Use disease-free seeds",
            "Avoid overhead watering",
            "Practice crop rotation",
            "Remove infected plants"
        ],

        "treatment": [
            "Copper-based bactericides",
            "Remove infected leaves",
            "Maintain field sanitation"
        ]
    },


    "Tomato___Early_blight": {

        "crop": "Tomato",

        "status": "Diseased",

        "disease": "Early Blight",

        "severity": "Medium",

        "description":
            "Early Blight is a fungal disease caused by Alternaria solani. It commonly affects older leaves and can reduce tomato yield.",

        "symptoms": [
            "Brown circular spots",
            "Concentric ring patterns",
            "Yellowing leaves",
            "Stem lesions"
        ],

        "causes": [
            "Alternaria solani fungus",
            "Warm humid conditions",
            "Poor crop rotation"
        ],

        "prevention": [
            "Remove infected leaves",
            "Maintain plant spacing",
            "Avoid wet foliage"
        ],

        "treatment": [
            "Apply chlorothalonil fungicide",
            "Use copper fungicides",
            "Remove infected plant parts"
        ]
    },


    "Tomato___Late_blight": {

        "crop": "Tomato",

        "status": "Diseased",

        "disease": "Late Blight",

        "severity": "Very High",

        "description":
            "Late Blight is a highly destructive disease caused by Phytophthora infestans. It can spread rapidly and destroy tomato crops.",

        "symptoms": [
            "Large dark leaf patches",
            "White fungal growth under leaves",
            "Fruit rot",
            "Rapid plant collapse"
        ],

        "causes": [
            "Phytophthora infestans",
            "Cool wet weather",
            "High humidity"
        ],

        "prevention": [
            "Improve air circulation",
            "Avoid excessive moisture",
            "Use resistant varieties"
        ],

        "treatment": [
            "Apply fungicides early",
            "Remove infected plants",
            "Use copper-based sprays"
        ]
    },


    "Tomato___Leaf_Mold": {

        "crop": "Tomato",

        "status": "Diseased",

        "disease": "Leaf Mold",

        "severity": "Medium",

        "description":
            "Leaf Mold is a fungal disease commonly affecting tomatoes grown in humid environments, especially greenhouses.",

        "symptoms": [
            "Yellow spots on upper leaves",
            "Olive-green mold underneath leaves",
            "Leaf curling",
            "Reduced growth"
        ],

        "causes": [
            "Passalora fulva fungus",
            "High humidity",
            "Poor ventilation"
        ],

        "prevention": [
            "Improve greenhouse ventilation",
            "Reduce humidity",
            "Avoid overhead irrigation"
        ],

        "treatment": [
            "Apply fungicides",
            "Remove infected leaves",
            "Increase airflow"
        ]
    },


    "Tomato___Septoria_leaf_spot": {

        "crop": "Tomato",

        "status": "Diseased",

        "disease": "Septoria Leaf Spot",

        "severity": "Medium",

        "description":
            "Septoria Leaf Spot is a fungal disease that mainly affects tomato leaves and causes premature leaf loss.",

        "symptoms": [
            "Small circular spots",
            "Dark borders around spots",
            "Yellowing leaves",
            "Leaf drop"
        ],

        "causes": [
            "Septoria lycopersici fungus",
            "Wet weather",
            "Infected plant debris"
        ],

        "prevention": [
            "Remove old plant debris",
            "Avoid touching wet plants",
            "Use crop rotation"
        ],

        "treatment": [
            "Apply fungicides",
            "Remove infected leaves"
        ]
    },


    "Tomato___Spider_mites Two-spotted_spider_mite": {

        "crop": "Tomato",

        "status": "Diseased",

        "disease": "Spider Mites",

        "severity": "Medium",

        "description":
            "Spider mites are tiny pests that feed on tomato leaves and damage plant cells, reducing plant growth.",

        "symptoms": [
            "Yellow speckled leaves",
            "Fine webbing",
            "Leaf drying",
            "Reduced plant strength"
        ],

        "causes": [
            "Two-spotted spider mite infestation",
            "Hot dry conditions"
        ],

        "prevention": [
            "Maintain proper humidity",
            "Inspect plants regularly",
            "Remove affected leaves"
        ],

        "treatment": [
            "Use neem oil",
            "Apply insecticidal soap",
            "Use recommended miticides"
        ]
    },


    "Tomato___Target_Spot": {

        "crop": "Tomato",

        "status": "Diseased",

        "disease": "Target Spot",

        "severity": "Medium",

        "description":
            "Target Spot is a fungal disease affecting tomato leaves, stems, and fruits.",

        "symptoms": [
            "Circular target-like spots",
            "Leaf yellowing",
            "Fruit lesions",
            "Defoliation"
        ],

        "causes": [
            "Corynespora cassiicola fungus",
            "Warm humid conditions"
        ],

        "prevention": [
            "Improve air circulation",
            "Avoid wet leaves",
            "Use crop rotation"
        ],

        "treatment": [
            "Apply fungicides",
            "Remove infected material"
        ]
    },


    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {

        "crop": "Tomato",

        "status": "Diseased",

        "disease": "Tomato Yellow Leaf Curl Virus",

        "severity": "Very High",

        "description":
            "TYLCV is a viral disease transmitted by whiteflies that severely affects tomato production.",

        "symptoms": [
            "Yellow curled leaves",
            "Stunted growth",
            "Reduced fruit production",
            "Small leaves"
        ],

        "causes": [
            "Tomato Yellow Leaf Curl Virus",
            "Whitefly transmission"
        ],

        "prevention": [
            "Control whiteflies",
            "Use resistant varieties",
            "Remove infected plants"
        ],

        "treatment": [
            "No direct cure for virus",
            "Control insect vectors",
            "Remove infected plants"
        ]
    },


    "Tomato___Tomato_mosaic_virus": {

        "crop": "Tomato",

        "status": "Diseased",

        "disease": "Tomato Mosaic Virus",

        "severity": "High",

        "description":
            "Tomato Mosaic Virus affects plant growth and fruit quality. It spreads through contaminated tools and plant contact.",

        "symptoms": [
            "Mosaic leaf patterns",
            "Leaf distortion",
            "Reduced growth",
            "Poor fruit development"
        ],

        "causes": [
            "Tomato Mosaic Virus",
            "Contaminated hands or tools"
        ],

        "prevention": [
            "Disinfect tools",
            "Use healthy seeds",
            "Remove infected plants"
        ],

        "treatment": [
            "No chemical cure",
            "Remove infected plants",
            "Practice sanitation"
        ]
    },


    "Tomato___healthy": {

        "crop": "Tomato",

        "status": "Healthy",

        "disease": "Healthy Plant",

        "severity": "None",

        "description":
            "The tomato plant appears healthy with normal growth and no visible disease symptoms.",

        "symptoms": [
            "Green healthy leaves",
            "Strong stems",
            "Normal fruit development"
        ],

        "causes": [
            "Proper cultivation practices"
        ],

        "prevention": [
            "Regular monitoring",
            "Balanced fertilizer",
            "Proper irrigation"
        ],

        "treatment": [
            "No treatment required"
        ]
    }

}
