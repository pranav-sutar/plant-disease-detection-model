import streamlit as st
import tensorflow as tf
import numpy as np
# import os
#tensorflow model prediction
model = tf.keras.models.load_model('./trained_model.h5')

def model_prediction(test_image):

    image = tf.keras.preprocessing.image.load_img(test_image, target_size = (128,128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])
    prediction = model.predict(input_arr)
    result_index = np.argmax(prediction)
    return result_index

# **************************** Solutions ************************************
Apple___Apple_scab = """ Managing apple scab, a fungal disease caused by Venturia inaequalis, requires a combination of preventive measures, cultural practices, and, in some cases, fungicidal treatments. Here's a treatment solution:

1. **Cultural Practices**:
   - **Pruning**: Prune apple trees during the dormant season to improve air circulation within the canopy, which reduces humidity and inhibits fungal growth.
   - **Remove Infected Leaves and Fruit**: Remove and destroy fallen leaves and infected fruit promptly to reduce the source of inoculum for future infections.
   - **Spacing**: Plant apple trees at appropriate distances to ensure adequate airflow and light penetration, reducing the risk of infection.
   - **Mulching**: Apply organic mulch around the base of trees to prevent soil splash onto lower leaves, which can spread the disease.

2. **Resistant Varieties**:
   - Consider planting apple varieties that are resistant to apple scab. Resistant varieties can significantly reduce the severity of the disease and may require fewer fungicide applications.

3. **Fungicidal Treatments**:
   - **Preventive Fungicides**: Apply fungicides preventively, starting before bud break and continuing throughout the growing season at regular intervals. Common fungicides used against apple scab include captan, mancozeb, chlorothalonil, and myclobutanil.
   - **Systemic Fungicides**: Systemic fungicides, such as thiophanate-methyl and tebuconazole, are absorbed by the plant and provide longer-lasting protection against apple scab.
   - **Rotate Fungicides**: Rotate between different classes of fungicides to reduce the risk of resistance development in the fungal population.

4. **Weather Monitoring**:
   - Monitor weather conditions, particularly periods of high humidity and rainfall, which favor apple scab development. Adjust fungicide application schedules accordingly during periods of increased disease pressure.

5. **Post-Harvest Measures**:
   - Prune out and remove infected branches and fruit after harvest to reduce overwintering sites for the fungus.
   - Practice good sanitation by removing fallen leaves and debris from the orchard floor to prevent the spread of the disease.

6. **Integrated Pest Management (IPM)**:
   - Implement an integrated approach to apple scab management, combining cultural practices, resistant varieties, and fungicidal treatments as part of an overall IPM strategy.
   - Monitor orchards regularly for signs of disease development and adjust management practices as needed based on disease severity and environmental conditions.

7. **Education and Training**:
   - Educate orchard workers about the symptoms of apple scab and proper disease management practices to minimize its spread.

By implementing these treatment solutions, apple growers can effectively manage apple scab and minimize its impact on orchard health and productivity. Regular monitoring, proper cultural practices, and timely fungicide applications are key to successful disease management."""
Apple___Black_rot ="""Apple black rot is a fungal disease caused by Botryosphaeria obtusa. Managing black rot typically involves a combination of cultural, biological, and chemical methods. Here's a comprehensive treatment solution:

1. **Cultural Practices**:
   - **Pruning**: Proper pruning to improve air circulation and sunlight penetration reduces the risk of infection. Remove dead or diseased branches.
   - **Sanitation**: Regularly remove fallen leaves, infected fruit, and pruned branches to prevent the fungus from overwintering and spreading.
   - **Spacing**: Plant apple trees at appropriate distances to allow for good air circulation.
   - **Mulching**: Apply organic mulch around the base of the trees to prevent splashing of spores from the soil onto the lower leaves.

2. **Biological Control**:
   - **Beneficial Microorganisms**: Some microbial agents, such as Bacillus subtilis and Trichoderma spp., have shown efficacy in suppressing fungal pathogens. These can be applied as foliar sprays or soil drenches.

3. **Chemical Control**:
   - **Fungicides**: Apply fungicides preventively during the growing season, especially during periods of high humidity and rainfall. Common fungicides used against apple black rot include captan, thiophanate-methyl, and mancozeb. Follow label instructions carefully and rotate between different classes of fungicides to prevent resistance.
   - **Systemic Fungicides**: Systemic fungicides can be absorbed by the plant and provide longer-lasting protection. Examples include tebuconazole and myclobutanil.

4. **Post-Harvest Measures**:
   - **Storage Conditions**: Store harvested apples in a cool, dry place with good ventilation to prevent the spread of the disease in storage.
   - **Post-Harvest Fungicides**: Application of post-harvest fungicides can further reduce the risk of rot during storage. Thiabendazole is commonly used for this purpose.

5. **Integrated Pest Management (IPM)**:
   - **Monitor**: Regularly monitor orchards for signs of disease development.
   - **Thresholds**: Establish action thresholds for fungicide application based on disease severity and weather conditions.
   - **Non-Chemical Methods**: Integrate cultural practices, biological control agents, and resistant varieties into an overall IPM strategy to minimize reliance on chemical treatments.

6. **Resistant Varieties**:
   - Planting resistant apple varieties can significantly reduce the incidence and severity of black rot. Consult with local agricultural extension services or nurseries for recommended resistant varieties.

7. **Educational Efforts**:
   - Educate orchard workers about the disease, its symptoms, and proper sanitation practices to minimize its spread.

8. **Weather Monitoring**:
   - Keep track of weather conditions, particularly rainfall and humidity levels, as these can influence the development and spread of black rot.

By combining these approaches, growers can effectively manage apple black rot and minimize its impact on orchard yields. Regular monitoring and adaptation of control measures based on local conditions are essential for long-term disease management. """
Apple___Cedar_apple_rust =""" Cedar apple rust is a fungal 
disease caused by Gymnosporangium juniperi-virginianae. Controlling cedar apple rust involves a combination of cultural, biological, and chemical methods. Here's a treatment solution:

1. **Cultural Practices**:
   - **Sanitation**: Remove any cedar or juniper trees within a half-mile radius of the apple orchard, if possible, as these act as alternate hosts for the fungus.
   - **Pruning**: Prune apple trees to improve air circulation and sunlight penetration, which helps reduce humidity and create an unfavorable environment for fungal growth.
   - **Avoid Overhead Irrigation**: Minimize overhead irrigation to prevent prolonged leaf wetness, which favors disease development.
   - **Fall Clean-up**: Remove fallen leaves and debris from the orchard floor to reduce the overwintering sites for the fungus.

2. **Biological Control**:
   - **Beneficial Microorganisms**: Some microbial agents, such as Bacillus subtilis and Streptomyces spp., may help suppress fungal pathogens. These can be applied as foliar sprays or soil drenches.

3. **Chemical Control**:
   - **Fungicides**: Apply fungicides preventively starting in early spring before symptoms appear and continue at regular intervals throughout the growing season, especially during periods of high humidity and rainfall. Fungicides commonly used against cedar apple rust include captan, mancozeb, myclobutanil, and triadimefon. Follow label instructions carefully and rotate between different classes of fungicides to prevent resistance.
   - **Systemic Fungicides**: Systemic fungicides can be absorbed by the plant and provide longer-lasting protection. Examples include thiophanate-methyl and tebuconazole.

4. **Post-Harvest Measures**:
   - **Prune Infected Branches**: After harvest, prune out any branches showing symptoms of cedar apple rust to reduce inoculum levels for the following season.
   - **Storage Conditions**: Store harvested apples in a cool, dry place with good ventilation to prevent the spread of the disease in storage.

5. **Integrated Pest Management (IPM)**:
   - **Monitor**: Regularly monitor orchards for signs of disease development.
   - **Thresholds**: Establish action thresholds for fungicide application based on disease severity and weather conditions.
   - **Non-Chemical Methods**: Integrate cultural practices, biological control agents, and resistant varieties into an overall IPM strategy to minimize reliance on chemical treatments.

6. **Resistant Varieties**:
   - Consider planting apple varieties that are less susceptible to cedar apple rust. While no apple varieties are completely immune, some are more resistant than others.

7. **Educational Efforts**:
   - Educate orchard workers about the disease, its symptoms, and proper sanitation practices to minimize its spread.

By implementing these strategies in an integrated manner, growers can effectively manage cedar apple rust and reduce its impact on apple orchards. Regular monitoring and adaptation of control measures based on local conditions are essential for successful disease management."""
Apple___healthy = """For a healthy apple plant, your web application could provide a specific description along with care tips tailored for apple trees:

**Confirmation of Health**:
"Congratulations! Your apple tree appears to be in excellent health. The leaves are vibrant and show no signs of common apple diseases such as fire blight or apple scab."

**Care Tips**:
- **Sunlight**: Ensure your apple tree continues to receive at least 6-8 hours of full sun daily⁷.
- **Watering**: Water deeply once a week during dry spells, but avoid overwatering to prevent root rot[^10^].
- **Pruning**: Regular pruning helps maintain tree health and promotes better air circulation, which can reduce disease risk⁹.
- **Fertilization**: Apply a balanced fertilizer during the growing season to support healthy growth and fruit production⁹.

**Preventative Measures**:
- **Disease Monitoring**: Keep an eye out for signs of common diseases like apple scab, cedar apple rust, and powdery mildew, and take action early if you notice any symptoms¹.
- **Pest Control**: Monitor for pests such as apple maggots and codling moths, which can affect the health of your apple tree⁶.
"""
Blueberry___healthy ="""**Confirmation of Health**:
"Your blueberry bush is looking vibrant and full of life! The foliage is lush and green, with no signs of common diseases like mummy berry or stem blight."

**Care Tips**:
- **Sunlight**: Blueberries thrive in full sun, requiring about 6 hours of sunlight per day to produce the best fruit⁷.
- **Soil**: They prefer acidic, well-drained soil. Aim for a soil pH between 4.5 and 5.5⁵.
- **Watering**: Keep the soil moist but not waterlogged. Blueberries have shallow root systems and need 1 to 2 inches of water per week⁹.
- **Mulching**: Apply a 2- to 4-inch layer of mulch like pine needles or wood chips to conserve moisture and suppress weeds⁹.

**Preventative Measures**:
- **Disease Monitoring**: Watch out for signs of diseases such as bacterial canker, crown gall, and armillaria root rot².
- **Pest Control**: Protect your blueberries from birds and insects that can damage the fruit and foliage¹.
"""
Cherry___Powdery_mildew =""" Cherry powdery mildew, caused by the fungus Podosphaera clandestina, can be managed through various cultural, chemical, and biological methods. Here are some treatments and preventive measures:

1. **Cultural Practices**:
   - Prune infected branches: Remove and destroy infected plant parts to prevent the spread of the disease.
   - Improve air circulation: Proper spacing of trees and pruning can help improve air movement, reducing humidity levels that favor the growth of powdery mildew.
   - Maintain good sanitation: Clean up fallen leaves and debris around the trees to reduce overwintering sites for the fungus.

2. **Chemical Controls**:
   - Fungicides: Apply fungicides labeled for cherry powdery mildew control, following recommended rates and timing. Common fungicides include sulfur, potassium bicarbonate, and synthetic fungicides like myclobutanil and propiconazole. Rotate between different classes of fungicides to prevent resistance.
   - Apply preventively: Begin fungicide applications before symptoms appear, especially during periods of high humidity or when environmental conditions are favorable for disease development.

3. **Biological Controls**:
   - Biofungicides: Some biofungicides containing beneficial microorganisms like Bacillus subtilis or Trichoderma spp. can suppress powdery mildew infections.
   - Beneficial insects: Encourage populations of natural predators like ladybugs and lacewings, which feed on powdery mildew spores and help keep their numbers in check.

4. **Resistant Varieties**: Plant cherry cultivars that are resistant to powdery mildew, as they are less susceptible to infection.

5. **Avoid Overfertilization**: Excessive nitrogen fertilization can promote lush, succulent growth that is more susceptible to powdery mildew. Use balanced fertilization practices.

6. **Monitor and Early Detection**: Regularly inspect cherry trees for signs of powdery mildew infection, such as white powdery spots on leaves, shoots, and fruit. Early detection allows for prompt intervention.

Remember to always read and follow the instructions on fungicide labels, and consider integrated pest management (IPM) strategies that combine multiple approaches for effective disease management while minimizing environmental impact."""
Cherry___healthy= """**Confirmation of Health**:
"Your cherry tree is thriving! The leaves are glossy and free from spots, the branches are robust, and there are no signs of common diseases such as black knot, brown rot, or cherry leaf spot."

**Care Tips**:
- **Sunlight**: Cherry trees need full sun, so ensure they get at least 6 hours of direct sunlight each day⁶.
- **Soil**: They prefer well-drained, fertile soil with a pH of 6.0-7.0[^10^].
- **Watering**: Water your cherry tree regularly, especially during dry spells. Young trees need more frequent watering until they are established⁷.
- **Pruning**: Prune during the dormant season to remove any dead or diseased wood and to shape the tree⁷.

**Preventative Measures**:
- **Disease Monitoring**: Keep an eye out for symptoms of diseases like powdery mildew and canker, which can be managed with good sanitation practices and fungicides³.
- **Pest Control**: Look out for pests such as aphids, spider mites, caterpillars, and beetles, and manage them using organic pest control methods³.
""" 


corn_maiz_clsglf =""" Cercospora leaf spot and gray leaf spot are two distinct diseases affecting corn (maize) caused by different fungi (Cercospora zeae-maydis and Cercospora zeina, respectively). Here are some treatments and management strategies:
1. **Cultural Practices**:
   - Crop rotation: Avoid planting corn in the same field consecutively. Rotate with non-host crops to reduce inoculum buildup in the soil.
   - Tillage: Incorporate crop residue into the soil after harvest to reduce overwintering of fungal pathogens.
   - Planting density: Proper spacing between plants promotes air circulation, reducing humidity levels and slowing disease spread.

2. **Resistant Varieties**:
   - Plant corn hybrids that are genetically resistant or tolerant to Cercospora leaf spot and gray leaf spot. Many seed companies offer hybrids with varying levels of resistance.

3. **Fungicides**:
   - Fungicides can be applied to manage Cercospora leaf spot and gray leaf spot, especially in fields with a history of severe disease or when weather conditions favor disease development.
   - Fungicides containing active ingredients such as azoxystrobin, pyraclostrobin, propiconazole, or triazoles are effective against these diseases.
   - Follow the label instructions regarding application rates, timing, and safety precautions.

4. **Crop Management**:
   - Timely planting: Plant corn early to avoid peak periods of disease development.
   - Balanced fertilization: Maintain proper nutrient levels to promote plant health and vigor, which can help reduce susceptibility to foliar diseases.
   - Weed control: Keep fields free from weeds, as they can serve as alternative hosts for Cercospora fungi.

5. **Monitor and Early Detection**:
   - Regular scouting of corn fields is essential to detect symptoms of Cercospora leaf spot and gray leaf spot early.
   - Symptoms include small, circular to oval lesions with gray centers and dark brown borders on leaves. Lesions may coalesce under favorable conditions.
   - Early detection allows for timely fungicide applications if warranted.

6. **Crop Residue Management**:
   - Remove and destroy crop residues after harvest to reduce the amount of inoculum available for the next planting season.
   - Incorporate residues into the soil through tillage to facilitate decomposition and reduce fungal survival.

Integrated pest management (IPM) approaches that combine cultural, chemical, and biological strategies offer the most effective and sustainable management of Cercospora leaf spot and gray leaf spot in corn crops. """

Corn_maize___Common_rust = """ Managing common rust in corn (maize) involves a combination of cultural practices, resistant varieties, and, if necessary, fungicide applications. Here's a more detailed look at each approach:
1. **Resistant Varieties**:
   - Plant corn hybrids that have been bred for resistance or tolerance to common rust. Resistant varieties can significantly reduce the impact of the disease.
   - Consult seed catalogs or agricultural extension services for information on available resistant varieties suitable for your region.

2. **Cultural Practices**:
   - Crop rotation: Rotate corn with non-host crops to break the disease cycle and reduce inoculum levels in the soil.
   - Tillage: Incorporate crop residues into the soil after harvest to accelerate decomposition and reduce overwintering of rust spores.
   - Planting density: Proper spacing between plants promotes air circulation, which can help reduce humidity and slow the spread of rust.

3. **Fungicides**:
   - Fungicides can be used as a preventive measure or to manage severe outbreaks of common rust.
   - Apply fungicides containing active ingredients such as triazoles (e.g., propiconazole), strobilurins (e.g., azoxystrobin), or combination products.
   - Timing is crucial: Apply fungicides preventively before rust symptoms appear or at the onset of initial infection.
   - Follow label instructions regarding application rates, timing, and safety precautions.

4. **Monitoring and Scouting**:
   - Regularly monitor corn fields for signs of common rust, including small, circular pustules on leaves, stems, and husks.
   - Early detection allows for timely intervention and better disease management.

5. **Sanitation**:
   - Clean equipment and machinery between fields to prevent the spread of rust spores.
   - Remove and destroy crop residues, especially if they are infected with rust, to reduce the source of inoculum for future infections.

6. **Integrated Pest Management (IPM)**:
   - Implement a holistic approach to pest and disease management that combines cultural, biological, and chemical control methods.
   - Incorporate practices such as crop rotation, use of resistant varieties, and judicious fungicide applications into an overall management strategy.

By combining these strategies, farmers can effectively manage common rust in corn crops while minimizing the use of chemical interventions and promoting sustainable agricultural practices."""

Corn_maize___Northern_Leaf_Blight=""" Managing Northern leaf blight (NLB) in corn (maize) involves a combination of cultural practices, genetic resistance, and, if necessary, fungicide applications. Here's a comprehensive approach to treating NLB:

1. **Resistant Varieties**:
   - Plant corn hybrids that have been bred for resistance to Northern leaf blight. Resistant varieties can significantly reduce the impact of the disease.
   - Consult seed catalogs or agricultural extension services for information on available resistant varieties suitable for your region.

2. **Cultural Practices**:
   - Crop rotation: Rotate corn with non-host crops to break the disease cycle and reduce inoculum levels in the soil.
   - Tillage: Incorporate crop residues into the soil after harvest to accelerate decomposition and reduce overwintering of NLB spores.
   - Planting density: Proper spacing between plants promotes air circulation, which can help reduce humidity and slow the spread of NLB.

3. **Fungicides**:
   - Fungicides can be used as a preventive measure or to manage severe outbreaks of NLB.
   - Apply fungicides containing active ingredients such as triazoles (e.g., azoxystrobin, propiconazole), strobilurins (e.g., pyraclostrobin), or combination products.
   - Timing is crucial: Apply fungicides preventively before NLB symptoms appear or at the onset of initial infection.
   - Follow label instructions regarding application rates, timing, and safety precautions.

4. **Monitoring and Scouting**:
   - Regularly monitor corn fields for signs of NLB, including cigar-shaped lesions with wavy edges on leaves.
   - Early detection allows for timely intervention and better disease management.

5. **Sanitation**:
   - Clean equipment and machinery between fields to prevent the spread of NLB spores.
   - Remove and destroy crop residues, especially if they are infected with NLB, to reduce the source of inoculum for future infections.

6. **Integrated Pest Management (IPM)**:
   - Implement a holistic approach to pest and disease management that combines cultural, biological, and chemical control methods.
   - Incorporate practices such as crop rotation, use of resistant varieties, and judicious fungicide applications into an overall management strategy.

By combining these strategies, farmers can effectively manage Northern leaf blight in corn crops while minimizing the use of chemical interventions and promoting sustainable agricultural practices."""

Corn_maize___healthy= """ **Confirmation of Health**:
"Your corn plants are looking robust and healthy! The stalks are strong, the leaves are a deep green without any discoloration, and there are no signs of common diseases such as Maize Dwarf Mosaic Virus or Northern Corn Leaf Blight."

**Care Tips**:
- **Sunlight**: Corn plants need full sunlight, so they should be planted where they will receive a minimum of six hours of direct sun per day¹.
- **Soil**: The soil should be fertile with good drainage. Corn prefers a slightly acidic to neutral pH (6.0-7.0)².
- **Watering**: Provide consistent moisture, especially during the flowering and ear development stages. Corn requires about 1 to 2 inches of water per week¹.
- **Nutrients**: Corn is a heavy feeder, particularly of nitrogen. Apply a balanced fertilizer or well-rotted manure at planting time and side-dress when the plants are knee-high¹.

**Preventative Measures**:
- **Disease Monitoring**: Regularly inspect your plants for signs of diseases. Early detection can prevent the spread and minimize damage⁸.
- **Pest Control**: Keep an eye out for pests like corn earworms and aphids, which can be managed through natural predators or appropriate insecticides¹.
"""

Grape___Black_rot= """ Black rot is a destructive fungal disease affecting grapes, caused by the pathogen Guignardia bidwellii. Effective management of black rot involves a combination of cultural, chemical, and biological strategies. Here are some treatment options:

1. **Cultural Practices**:
   - Pruning: Proper pruning practices promote air circulation and sunlight penetration, reducing humidity levels and creating an environment less conducive to disease development.
   - Canopy Management: Manage vine canopy to reduce humidity and improve air circulation within the canopy.
   - Weed Control: Remove weeds and other vegetation around grapevines to reduce moisture retention and eliminate potential hosts for the black rot fungus.

2. **Sanitation**:
   - Remove and destroy any infected plant material, including mummified fruit and diseased canes, to reduce the source of inoculum for future infections.
   - Clean pruning tools and equipment to prevent the spread of spores between vines.

3. **Fungicides**:
   - Apply fungicides to protect grapevines from black rot infection.
   - Fungicides containing active ingredients such as captan, mancozeb, myclobutanil, triazoles (e.g., tebuconazole), strobilurins (e.g., azoxystrobin), and copper-based fungicides are commonly used for black rot management.
   - Follow the label instructions regarding application rates, timing, and safety precautions. Apply fungicides preventively before the onset of disease symptoms or during periods of high disease pressure.

4. **Biological Control**:
   - Some biofungicides containing beneficial microorganisms like Bacillus subtilis or Trichoderma spp. can suppress black rot infections. These products can be used as part of an integrated pest management (IPM) approach to disease management.

5. **Resistant Varieties**:
   - Plant grape varieties that are resistant or tolerant to black rot, if available. Resistant varieties can reduce the severity of disease and minimize the need for chemical treatments.

6. **Monitoring and Early Detection**:
   - Regularly inspect grapevines for symptoms of black rot, including brown lesions on leaves, fruit, and stems, as well as shriveled or mummified berries.
   - Early detection allows for timely intervention and better disease management.

7. **Weather Monitoring**:
   - Monitor weather conditions, especially during periods of prolonged wetness and high humidity, which favor black rot development. Adjust fungicide applications accordingly to protect vines during critical infection periods.

Integrated pest management (IPM) practices that combine multiple control strategies are often the most effective approach for managing black rot and reducing reliance on fungicides while promoting sustainable grape production. """

Grape___Esca_Black_Measles= """ Esca, including its severe form known as Black Measles, is a complex grapevine disease caused by multiple fungi, including Phaeomoniella chlamydospora, Phaeoacremonium spp., and others. Managing Esca and Black Measles requires an integrated approach due to the multifactorial nature of the disease. Here are some treatment options:

1. **Cultural Practices**:
   - Pruning: Prune grapevines during the dormant season, removing infected wood and canes to reduce the inoculum source.
   - Wound Protection: Protect pruning wounds with wound sealants or protectants to prevent fungal spore entry.
   - Avoid Overhead Irrigation: Minimize leaf wetness periods by using drip irrigation or other methods that don't wet the foliage.

2. **Sanitation**:
   - Remove and destroy infected wood, including pruning debris and canes showing symptoms of Esca and Black Measles.
   - Clean pruning tools thoroughly between vines to prevent the spread of the disease.

3. **Fungicides**:
   - Fungicide applications can be part of an integrated disease management strategy for Esca and Black Measles.
   - Fungicides containing active ingredients such as boscalid, fluopyram, fosetyl-aluminum, propiconazole, and others can help suppress fungal pathogens associated with the disease.
   - Fungicide timing and application rates should be based on disease risk assessment and local recommendations.

4. **Biological Control**:
   - Some biofungicides containing beneficial microorganisms, such as Bacillus spp. or Trichoderma spp., can be used to suppress fungal pathogens associated with Esca.
   - Biocontrol agents may be applied to the soil or foliage as part of an integrated disease management program.

5. **Nutritional Management**:
   - Ensure proper vine nutrition to maintain vine health and vigor, which can improve the plant's ability to resist and recover from Esca infections.
   - Consider foliar applications of micronutrients, such as boron and manganese, which are sometimes deficient in Esca-affected vines.

6. **Resistant Varieties**:
   - Plant grapevine varieties that exhibit some level of resistance or tolerance to Esca and Black Measles, if available.
   - While no completely resistant varieties are available, some show reduced susceptibility to the disease.

7. **Monitoring and Early Detection**:
   - Regularly monitor grapevines for symptoms of Esca and Black Measles, including leaf discoloration, wilting, and wood decay.
   - Early detection allows for prompt intervention, such as targeted pruning and fungicide applications.

8. **Integrated Pest Management (IPM)**:
   - Implement an integrated approach to disease management that combines cultural practices, sanitation, fungicides, and other control measures.
   - Incorporate disease forecasting models and weather monitoring to optimize fungicide application timing.

It's important to note that while these treatments can help manage Esca and Black Measles, complete eradication of the disease from affected vineyards is challenging. Instead, the goal is to reduce disease incidence and severity, preserve vine health, and maintain sustainable grape production. Regular monitoring, proper sanitation, and a holistic management approach are essential for long-term disease control."""

Grape___Leaf_blight_Isariopsis_Leaf_Spot= """ Isariopsis Leaf Spot, also known as grape leaf blight, is caused by the fungus Isariopsis (=Scolecotrichum) leaf spot (Isariopsis (=Scolecotrichum) viticola). While this disease doesn't usually cause significant economic losses, it can affect the aesthetics and vigor of grapevines. Here are some treatment options:

1. **Cultural Practices**:
   - Pruning: Proper pruning practices can improve air circulation and sunlight penetration within the grapevine canopy, reducing humidity and creating conditions less favorable for fungal growth.
   - Canopy Management: Manage vine canopy to minimize excessive foliage density, which can increase humidity and favor disease development.
   - Irrigation Management: Avoid overhead irrigation, as wet foliage can promote fungal growth. Instead, use drip or other targeted irrigation methods to keep the foliage dry.

2. **Sanitation**:
   - Remove and destroy infected leaves and plant debris to reduce the source of inoculum for future infections.
   - Practice proper sanitation during pruning, ensuring that infected plant material is removed from the vineyard.

3. **Fungicides**:
   - Fungicides can be applied to manage Isariopsis Leaf Spot, especially in vineyards with a history of the disease or during periods of favorable weather conditions for fungal growth.
   - Fungicides containing active ingredients such as copper-based compounds, sulfur, mancozeb, captan, and others may be effective against Isariopsis Leaf Spot.
   - Follow label instructions regarding application rates, timing, and safety precautions.

4. **Biological Control**:
   - Some biofungicides containing beneficial microorganisms, such as Bacillus subtilis or Trichoderma spp., may offer suppression of Isariopsis Leaf Spot. These products can be used as part of an integrated pest management (IPM) approach.

5. **Resistant Varieties**:
   - Plant grapevine varieties that exhibit some level of resistance or tolerance to Isariopsis Leaf Spot, if available. While complete resistance may not be common, some varieties may show reduced susceptibility.

6. **Monitoring and Early Detection**:
   - Regularly monitor grapevines for symptoms of Isariopsis Leaf Spot, including small circular lesions on leaves, which may have gray centers and reddish-brown margins.
   - Early detection allows for prompt intervention, such as targeted fungicide applications and sanitation measures.

7. **Integrated Pest Management (IPM)**:
   - Implement an integrated approach to disease management that combines cultural practices, sanitation, fungicides, and other control measures.
   - Incorporate disease forecasting models and weather monitoring to optimize fungicide application timing.

While Isariopsis Leaf Spot may not always require intensive management, particularly in low-pressure situations, a proactive approach to disease prevention and control can help maintain vine health and minimize the impact of the disease on grape production."""

Grape___healthy= """**Healthy Grape Alert!**
*Your grapevines are thriving! Our advanced diagnostic tools have not detected any signs of disease in your grape plants. They exhibit vibrant green leaves, robust growth, and optimal fruit development, indicating a clean bill of health.*

*Continue to provide your grapes with consistent care, and they'll reward you with a bountiful harvest. Remember, healthy grapevines are the cornerstone of exquisite wines and delightful raisins!*

*For tips on maintaining the health of your grapevines or to learn more about preventive measures, explore our resources or consult with our experts.*

---

 """

Orange___Haunglongbing_Citrus_greening= """ Huanglongbing (HLB), also known as citrus greening, is a devastating bacterial disease affecting citrus trees, including oranges. Managing HLB is challenging due to the lack of effective treatments once trees are infected. However, there are some strategies to help prevent the spread of the disease and manage its impact:

1. **Plant Health**:
   - Start with healthy planting material from reputable sources.
   - Ensure proper planting practices and site selection to promote tree vigor.

2. **Vector Control**:
   - Manage Asian citrus psyllids (Diaphorina citri), the insect vectors that transmit the HLB bacterium, through insecticide applications.
   - Regularly monitor for psyllid populations and implement control measures as needed.
   - Biological control methods using natural enemies of the psyllids, such as predatory insects or parasitic wasps, can also be employed.

3. **Sanitation**:
   - Remove and destroy infected trees promptly to prevent further spread of the disease.
   - Prune trees to remove symptomatic branches and improve air circulation within the canopy.

4. **Nutritional Management**:
   - Implement balanced fertilization practices to promote tree health and tolerance to the disease.
   - Correct nutrient deficiencies based on soil and tissue analysis.

5. **Antibiotic Treatments**:
   - In some cases, antibiotics such as oxytetracycline or streptomycin may be used as a part of an integrated disease management program.
   - These treatments are primarily used in high-value orchards under strict regulations and are most effective as preventive measures before infection occurs.

6. **Resistance Breeding**:
   - Research efforts are underway to develop citrus varieties with improved tolerance or resistance to HLB.
   - Incorporate HLB-resistant rootstocks and scion varieties when available.

7. **Biosecurity Measures**:
   - Implement strict biosecurity protocols to prevent the introduction and spread of HLB in citrus-growing regions.
   - Avoid movement of infected plant material and psyllid-infested plants.
   - Clean and sanitize equipment, tools, and vehicles between orchards to minimize disease spread.

8. **Research and Monitoring**:
   - Support ongoing research efforts to develop new management strategies, including genetic approaches, biological control, and early detection methods.
   - Monitor orchards regularly for symptoms of HLB and psyllid activity, and report any suspected cases to local agricultural authorities.

Overall, an integrated approach combining vector control, sanitation, nutritional management, and ongoing research efforts is essential for managing HLB and reducing its impact on citrus production. However, prevention remains the most effective strategy, emphasizing the importance of early detection and proactive measures to prevent the introduction and spread of the disease."""

Peach___Bacterial_spot= """ Bacterial spot is a common and damaging disease affecting peach trees, caused by the bacterium Xanthomonas arboricola pv. pruni. Managing bacterial spot in peach orchards requires a combination of cultural, biological, and chemical control methods. Here are some treatment options:

1. **Cultural Practices**:
   - Pruning: Prune peach trees to improve air circulation and sunlight penetration within the canopy, which helps reduce humidity and create conditions less favorable for bacterial growth.
   - Thinning: Thin fruit clusters to reduce crowding and improve air circulation, which can help reduce disease severity.
   - Irrigation: Use drip or micro-sprinkler irrigation to avoid wetting foliage and minimize leaf moisture, as wet conditions promote bacterial spot development.
   - Weed Management: Keep orchards free of weeds and other vegetation that can harbor bacteria or interfere with air circulation.

2. **Sanitation**:
   - Remove and destroy infected plant material, including infected leaves, shoots, and fruit, to reduce the source of bacterial inoculum.
   - Clean pruning tools and equipment between trees to prevent the spread of bacteria within the orchard.

3. **Copper-Based Sprays**:
   - Copper-based bactericides are commonly used to manage bacterial spot in peach orchards.
   - Apply copper sprays according to label instructions, typically during dormant and pre-bloom stages to protect new growth and blossoms from infection.
   - Avoid applying copper sprays during hot weather, as phytotoxicity can occur under certain conditions.

4. **Biological Control**:
   - Some biocontrol agents, such as certain strains of Bacillus spp., can suppress bacterial populations and reduce disease severity.
   - Biocontrol products can be applied preventively or as part of an integrated disease management program.

5. **Resistant Varieties**:
   - Plant peach varieties that exhibit some level of resistance or tolerance to bacterial spot, if available.
   - While no completely resistant varieties may be available, some cultivars show reduced susceptibility to the disease.

6. **Fertilization**:
   - Maintain proper tree nutrition with balanced fertilization to promote tree health and vigor, which can improve tolerance to bacterial spot infection.

7. **Weather Monitoring**:
   - Monitor weather conditions, particularly rainfall and humidity, which favor bacterial spot development.
   - Adjust irrigation practices and spray schedules accordingly to minimize leaf wetness and disease pressure.

8. **Integrated Pest Management (IPM)**:
   - Implement an integrated approach to disease management that combines cultural practices, sanitation, chemical control, and biological control methods.
   - Regular scouting and monitoring for disease symptoms and pest activity are essential components of IPM.

By incorporating these strategies into an integrated disease management program, growers can effectively manage bacterial spot in peach orchards and minimize its impact on fruit yield and quality. Regular monitoring, timely intervention, and adherence to best management practices are critical for successful disease control.""" 

Peach___healthy= """**Peach Perfection Detected!**

*Rejoice, peach enthusiasts! Our system has scanned your peach trees and the results are in – they're the picture of health. The leaves are lush and green, the branches are strong, and the peaches themselves are plump and juicy.*

*This is a testament to your attentive care and favorable growing conditions. Keep up the excellent work to ensure these peach trees continue to flourish, yielding fruit that's as nutritious as it is delicious.*

*Should you seek advice on nurturing your peach trees or wish to delve into preventive care strategies, our resources are at your disposal. Connect with our experts for tailored guidance.*

---
""" 

Pepper_bell___Bacterial_spot= """ Bacterial spot is a common and destructive disease affecting pepper (bell pepper) plants, caused by the bacterium Xanthomonas campestris pv. vesicatoria. Managing bacterial spot in pepper plants requires a combination of cultural, biological, and chemical control methods. Here are some treatment options:

1. **Cultural Practices**:
   - Crop Rotation: Rotate pepper plants with non-host crops to break the disease cycle and reduce inoculum levels in the soil.
   - Sanitation: Remove and destroy infected plant debris, including leaves, stems, and fruit, to reduce the source of bacterial inoculum.
   - Weed Management: Keep the area around pepper plants free from weeds, as they can harbor bacteria and interfere with airflow, promoting disease development.
   - Irrigation: Use drip irrigation or soaker hoses to avoid wetting foliage, as moisture on leaves promotes bacterial growth. Water early in the day to allow foliage to dry quickly.

2. **Resistant Varieties**:
   - Plant pepper varieties that are resistant or tolerant to bacterial spot, if available. Resistant varieties can significantly reduce disease severity.
   - Consult seed catalogs or local extension services for information on available resistant pepper varieties suitable for your region.

3. **Biological Control**:
   - Some biocontrol agents, such as certain strains of Bacillus spp., can suppress bacterial populations and reduce disease severity.
   - Biocontrol products can be applied preventively or as part of an integrated disease management program.

4. **Chemical Control**:
   - Copper-Based Sprays: Copper-based bactericides are commonly used to manage bacterial spot in pepper plants.
   - Apply copper sprays according to label instructions, starting at the first sign of disease or as a preventive measure during periods of high disease pressure.
   - Rotate between different chemical classes to reduce the risk of resistance development.

5. **Weather Monitoring**:
   - Monitor weather conditions, particularly rainfall and humidity, which favor bacterial spot development.
   - Adjust irrigation practices and spray schedules accordingly to minimize leaf wetness and disease pressure.

6. **Integrated Pest Management (IPM)**:
   - Implement an integrated approach to disease management that combines cultural practices, sanitation, chemical control, and biological control methods.
   - Regular scouting and monitoring for disease symptoms and pest activity are essential components of IPM.

By incorporating these strategies into an integrated disease management program, growers can effectively manage bacterial spot in pepper plants and minimize its impact on yield and quality. Regular monitoring, timely intervention, and adherence to best management practices are critical for successful disease control.""" 

Pepper_bell___healthy= """**Bell Pepper Bonanza!**

*Gardeners and chefs, take note: your bell peppers are in prime condition! Our system's analysis shows no disease presence, and your peppers are displaying all the signs of health. They boast crisp, vibrant-colored skins and firm, succulent flesh – a true mark of well-maintained plants.*

*These nutritional powerhouses are not just a feast for the eyes but also a boon for your well-being, packed with **vitamin C**, **vitamin A**, **potassium**, and a host of **antioxidants**¹².*

*To ensure your bell peppers continue to prosper, stick to your gardening regimen, and they'll keep providing you with their flavorful crunch. For more insights on care or to explore preventive measures against potential diseases, our resources are here to help.*

---
""" 

Potato___Early_blight= """ Managing early blight in potatoes involves a combination of cultural, biological, and chemical control methods. Here are some treatment options:

1. **Cultural Practices**:
   - Crop Rotation: Rotate potatoes with non-host crops such as grains or legumes to break the disease cycle and reduce inoculum levels in the soil.
   - Planting Density: Proper spacing between plants promotes air circulation and reduces humidity, which can help prevent early blight.
   - Weed Control: Keep the potato field free of weeds to reduce competition for nutrients and water, which can stress plants and make them more susceptible to disease.
   - Remove Infected Plant Debris: Remove and destroy any infected potato plant debris after harvest to reduce overwintering sources of the early blight fungus.

2. **Resistant Varieties**:
   - Plant potato varieties that are resistant or tolerant to early blight, if available. Resistant varieties can significantly reduce disease severity.
   - Consult with local agricultural extension services or seed suppliers for information on resistant potato varieties suitable for your region.

3. **Biological Control**:
   - Some biocontrol agents, such as certain strains of Bacillus spp. or Trichoderma spp., can suppress the early blight fungus.
   - Biocontrol products can be applied preventively or as part of an integrated disease management program.

4. **Chemical Control**:
   - Fungicides: Apply fungicides labeled for early blight control, following recommended rates and timing.
   - Common fungicides used for early blight management include chlorothalonil, mancozeb, azoxystrobin, and copper-based products.
   - Rotate between different chemical classes to reduce the risk of resistance development.

5. **Nutritional Management**:
   - Maintain proper soil fertility and pH levels through balanced fertilization to promote plant health and vigor.
   - Adequate potassium levels in the soil can help improve potato plant resistance to early blight.

6. **Weather Monitoring**:
   - Monitor weather conditions, particularly humidity and rainfall, which can promote early blight development.
   - Adjust irrigation practices to avoid prolonged leaf wetness, as this creates favorable conditions for the disease.

7. **Integrated Pest Management (IPM)**:
   - Implement an integrated approach to disease management that combines cultural practices, sanitation, chemical control, and biological control methods.
   - Regular scouting and monitoring for disease symptoms and pest activity are essential components of IPM.

By incorporating these strategies into an integrated disease management program, growers can effectively manage early blight in potatoes and minimize its impact on yield and quality. Regular monitoring, timely intervention, and adherence to best management practices are critical for successful disease control.""" 

Potato___Late_blight= """ Late blight is a devastating fungal disease affecting potatoes, caused by the pathogen Phytophthora infestans. Managing late blight requires a combination of cultural, biological, and chemical control methods. Here are some treatment options:

1. **Cultural Practices**:
   - Crop Rotation: Rotate potatoes with non-host crops such as grains or legumes to break the disease cycle and reduce inoculum levels in the soil.
   - Planting Density: Proper spacing between plants promotes air circulation and reduces humidity, which can help prevent late blight.
   - Timely Planting and Harvesting: Plant potatoes early to avoid peak periods of disease development. Harvest potatoes promptly to minimize exposure to late blight-infected foliage.

2. **Resistant Varieties**:
   - Plant potato varieties that are resistant or tolerant to late blight, if available. Resistant varieties can significantly reduce disease severity.
   - Consult with local agricultural extension services or seed suppliers for information on resistant potato varieties suitable for your region.

3. **Biological Control**:
   - Some biocontrol agents, such as certain strains of Bacillus spp. or Trichoderma spp., can suppress the late blight fungus.
   - Biocontrol products can be applied preventively or as part of an integrated disease management program.

4. **Chemical Control**:
   - Fungicides: Apply fungicides labeled for late blight control, following recommended rates and timing.
   - Common fungicides used for late blight management include chlorothalonil, mancozeb, azoxystrobin, and copper-based products.
   - Rotate between different chemical classes to reduce the risk of resistance development.

5. **Sanitation**:
   - Remove and destroy any infected potato plant debris after harvest to reduce overwintering sources of the late blight fungus.
   - Properly dispose of volunteer potato plants and cull piles to prevent the survival of late blight inoculum.

6. **Weather Monitoring**:
   - Monitor weather conditions, particularly humidity, rainfall, and temperature, which can promote late blight development.
   - Use disease forecasting models to predict and manage late blight outbreaks, and adjust fungicide application schedules accordingly.

7. **Integrated Pest Management (IPM)**:
   - Implement an integrated approach to disease management that combines cultural practices, sanitation, chemical control, and biological control methods.
   - Regular scouting and monitoring for disease symptoms and pest activity are essential components of IPM.

By incorporating these strategies into an integrated disease management program, growers can effectively manage late blight in potatoes and minimize its impact on yield and quality. Regular monitoring, timely intervention, and adherence to best management practices are critical for successful disease control."""

Potato___healthy= """**Potato Prosperity Check!**

*Gardeners, your potato plants are flourishing! Our precise analysis indicates that your potatoes are in excellent health. They're showing all the right signs: vigorous growth, resilient stems, and potatoes with smooth, unblemished skins.*

*These tubers are not just a staple food; they're a nutritional treasure trove. Packed with **vitamins C and B6**, **potassium**, **manganese**, **magnesium**, **phosphorus**, **niacin**, and **folate**¹, they're a great addition to any diet. Plus, they're rich in **antioxidants** like flavonoids, carotenoids, and phenolic acids, which may help reduce the risk of chronic diseases¹.*

*To keep your potatoes in tip-top shape, continue your current care routine and consider our expert tips for disease prevention. Dive into our resources for more information on keeping your potatoes happy and healthy.*

---
""" 

Raspberry___healthy= """**Healthy Raspberry Plants**

Raspberries, belonging to the genus *Rubus* within the Rosaceae family, are not only delightful to the taste but also a powerhouse of nutrition. A healthy raspberry plant is characterized by its robust growth and the production of vibrant, plump berries that are a rich source of vitamin C and antioxidants¹.

**Key Indicators of Health:**
- **Vigorous Growth:** A well-established raspberry plant will exhibit strong, green canes and a dense leaf canopy.
- **Berry Quality:** The berries should be firm, brightly colored, and free from any spots or signs of decay.
- **Leaf Appearance:** The leaves of a healthy raspberry plant are typically lush, deep green, and free from curling or yellowing, which can indicate nutrient deficiencies or disease.

**Cultivation Tips:**
- **Sunlight:** Raspberry plants thrive in full sun but can tolerate partial shade¹.
- **Soil:** They prefer well-draining sandy loams, rich in organic matter, with a pH between 5.5 and 6.5⁵.
- **Pruning:** Annual pruning is essential to remove dead canes and encourage the growth of new fruit-bearing ones¹.

**Disease Prevention:**
- **Proper Airflow:** Ensure there is adequate spacing between plants to promote air circulation and reduce the risk of fungal diseases.
- **Regular Monitoring:** Keep an eye out for any signs of distress, such as discolored leaves or the presence of pests, and address issues promptly to maintain plant health.

By providing clear images of healthy raspberry plants, your website can help users distinguish between a thriving plant and one that may be suffering from disease, ensuring timely and accurate treatment.

---
"""

Soybean___healthy= """**Healthy Soybean Plants**

Soybeans, scientifically known as *Glycine max*, are a staple legume crop with significant agricultural and nutritional importance. Healthy soybean plants are a testament to their resilience and adaptability, offering a rich source of protein and other essential nutrients¹.

**Key Indicators of Health:**
- **Sturdy Stature:** A healthy soybean plant stands erect with branching stems and can reach over 2 meters in height¹.
- **Leaf Vigor:** The leaves are broad and green, indicating a robust photosynthetic capacity and overall plant health⁵.
- **Pod Production:** Each plant produces 60 to 80 pods, with each pod containing three pea-sized beans, a sign of good fertility³.

**Cultivation Tips:**
- **Soil Requirements:** Soybeans flourish in warm, fertile, well-drained, sandy loam soil with a pH between 6.0 and 7.5¹.
- **Planting Time:** The crop is sown after the last frost and requires a full growing season to mature¹.
- **Nitrogen Fixation:** As legumes, soybeans enrich the soil by fixing nitrogen, which is beneficial for crop rotation practices¹.

**Disease Prevention:**
- **Crop Rotation:** This practice helps prevent soil-borne diseases and reduces pest populations.
- **Regular Inspections:** Monitoring for pests and signs of disease can help maintain the health of the crop and ensure timely interventions.

By providing users with clear images and descriptions of healthy soybean plants, your website can serve as an invaluable tool for farmers and gardeners to identify and treat plant diseases effectively.

---
"""

Squash___Powdery_mildew= """ Powdery mildew is a fungal disease that commonly affects squash plants, including zucchini, pumpkins, and other varieties. Managing powdery mildew involves several strategies to prevent its spread and minimize its impact on plant health and yield. Here are some treatment options:

1. **Cultural Practices**:
   - Plant Resistant Varieties: Some squash varieties show resistance or tolerance to powdery mildew. Choose resistant varieties when available.
   - Spacing: Proper plant spacing promotes air circulation around the plants, which can help reduce humidity and minimize conditions favorable for powdery mildew development.
   - Avoid Overhead Irrigation: Water the plants at the base to keep the foliage dry. Wet leaves provide an ideal environment for powdery mildew growth.
   - Crop Rotation: Rotate squash crops with unrelated plants to disrupt the disease cycle and reduce the buildup of powdery mildew spores in the soil.

2. **Fungicides**:
   - Apply Fungicides: Fungicides can be used to manage powdery mildew, especially in cases of severe infection or when environmental conditions favor disease development.
   - Fungicides containing active ingredients such as sulfur, potassium bicarbonate, neem oil, or horticultural oils are commonly used for powdery mildew control.
   - Follow label instructions regarding application rates, timing, and safety precautions.

3. **Biological Control**:
   - Biological fungicides containing beneficial microorganisms, such as Bacillus subtilis or certain strains of Trichoderma spp., can help suppress powdery mildew development.
   - Apply biofungicides preventively or at the first sign of powdery mildew symptoms as part of an integrated pest management (IPM) approach.

4. **Pruning and Plant Hygiene**:
   - Remove Infected Leaves: Prune off severely infected leaves to reduce the spread of powdery mildew to healthy plant parts.
   - Cleanliness: Remove and dispose of plant debris and fallen leaves to reduce the source of inoculum for future infections.

5. **Weather Monitoring**:
   - Monitor weather conditions, particularly humidity and temperature, which can influence powdery mildew development.
   - Adjust cultural practices and fungicide applications based on weather forecasts to optimize disease management.

6. **Foliar Applications**:
   - Foliar applications of potassium bicarbonate or baking soda solutions can help control powdery mildew when applied preventively or at the onset of symptoms.
   - Mix solutions according to recommended rates and spray plants thoroughly, covering both upper and lower leaf surfaces.

7. **Integrated Pest Management (IPM)**:
   - Implement an integrated approach to disease management that combines cultural practices, sanitation, chemical control, and biological control methods.
   - Regular scouting and monitoring for disease symptoms and pest activity are essential components of IPM.

By incorporating these strategies into an integrated disease management program, growers can effectively manage powdery mildew in squash crops and minimize its impact on yield and quality. Regular monitoring, timely intervention, and adherence to best management practices are critical for successful disease control.""" 

Strawberry___Leaf_scorch= """ Leaf scorch in strawberries can be caused by various factors, including fungal pathogens, environmental stress, and nutrient deficiencies. Here are some treatment options to manage leaf scorch in strawberries:

1. **Cultural Practices**:
   - Plant Health: Start with healthy planting material from reputable sources to reduce the risk of introducing pathogens.
   - Crop Rotation: Rotate strawberries with non-host crops to break disease cycles and reduce pathogen buildup in the soil.
   - Proper Irrigation: Maintain consistent soil moisture levels to avoid water stress, but avoid overwatering, which can promote fungal growth.
   - Weed Control: Keep the area around strawberry plants free from weeds to reduce competition for nutrients and water.

2. **Fungicides**:
   - Apply fungicides labeled for use against leaf scorch pathogens, following recommended rates and application timings.
   - Common fungicides used for leaf scorch control in strawberries include those containing active ingredients such as captan, mancozeb, and chlorothalonil.
   - Rotate between different chemical classes to reduce the risk of resistance development.

3. **Nutrient Management**:
   - Ensure proper soil fertility with balanced fertilization to promote plant health and vigor.
   - Correct nutrient deficiencies identified through soil tests or tissue analysis, as imbalances can contribute to leaf scorch symptoms.

4. **Sanitation**:
   - Remove and destroy infected plant material, including affected leaves and runners, to reduce the source of inoculum.
   - Clean pruning tools and equipment between plants to prevent the spread of pathogens within the strawberry patch.

5. **Biological Control**:
   - Some biofungicides containing beneficial microorganisms, such as Bacillus subtilis or Trichoderma spp., can help suppress fungal pathogens associated with leaf scorch.
   - Biocontrol products can be applied preventively or as part of an integrated disease management program.

6. **Weather Monitoring**:
   - Monitor weather conditions, particularly humidity and rainfall, which can promote fungal growth and exacerbate leaf scorch symptoms.
   - Adjust irrigation practices and fungicide application schedules based on weather forecasts to optimize disease management.

7. **Integrated Pest Management (IPM)**:
   - Implement an integrated approach to disease management that combines cultural practices, sanitation, chemical control, and biological control methods.
   - Regular scouting and monitoring for disease symptoms and pest activity are essential components of IPM.

By incorporating these strategies into an integrated disease management program, growers can effectively manage leaf scorch in strawberries and minimize its impact on yield and quality. Regular monitoring, timely intervention, and adherence to best management practices are critical for successful disease control."""

Strawberry___healthy= """**Healthy Strawberry Plants**

Strawberries, the sweet and succulent fruits of *Fragaria* species, are cherished around the globe for their delightful flavor and nutritional benefits. Healthy strawberry plants are key to a bountiful harvest and are easily identifiable by their vibrant growth and fruit production.

**Key Indicators of Health:**
- **Lush Foliage:** Look for bright green leaves and a dense leaf structure, which indicate a thriving plant¹.
- **Flower Development:** White or slightly pink flowers should appear in small clusters, signaling potential fruit development¹.
- **Fruit Quality:** The strawberries should be uniformly red, firm, and free of blemishes or signs of disease⁴.

**Cultivation Tips:**
- **Climate:** Strawberry plants prefer cooler environments and can struggle in hot, dry climates. Provide afternoon shade and regular watering if you're in a warmer region³.
- **Soil:** They thrive in well-drained, loamy soil rich in organic matter, with a pH between 5.5 and 6.5¹.
- **Watering:** Consistent moisture is crucial, especially during the fruiting period, to ensure plump and juicy berries³.

**Disease Prevention:**
- **Proper Spacing:** Ensure plants are spaced adequately to promote air circulation and reduce the risk of fungal infections.
- **Mulching:** Use straw or pine needles to mulch around the plants, which helps retain moisture and prevent weed growth.

By providing clear images and descriptions of healthy strawberry plants, your website can empower users to detect early signs of disease and take appropriate measures to maintain plant health.

---
"""

Tomato___Bacterial_spot= """ Bacterial spot is a common and damaging disease affecting tomatoes, caused by the bacterium Xanthomonas vesicatoria. Managing bacterial spot in tomatoes involves a combination of cultural, biological, and chemical control methods. Here are some treatment options:

1. **Cultural Practices**:
   - Crop Rotation: Rotate tomatoes with non-host crops such as grains or legumes to break the disease cycle and reduce inoculum levels in the soil.
   - Sanitation: Remove and destroy infected plant debris, including affected leaves, stems, and fruit, to reduce the source of bacterial inoculum.
   - Weed Management: Keep the area around tomato plants free of weeds to reduce competition for nutrients and water, which can stress plants and make them more susceptible to disease.
   - Avoid Overhead Irrigation: Water the plants at the base to keep the foliage dry. Wet leaves provide an ideal environment for bacterial growth.

2. **Resistant Varieties**:
   - Plant tomato varieties that are resistant or tolerant to bacterial spot, if available. Resistant varieties can significantly reduce disease severity.
   - Consult with local agricultural extension services or seed suppliers for information on resistant tomato varieties suitable for your region.

3. **Biological Control**:
   - Some biocontrol agents, such as certain strains of Bacillus spp. or Pseudomonas spp., can suppress bacterial populations and reduce disease severity.
   - Biocontrol products can be applied preventively or as part of an integrated disease management program.

4. **Chemical Control**:
   - Copper-Based Sprays: Copper-based bactericides are commonly used to manage bacterial spot in tomatoes.
   - Apply copper sprays according to label instructions, starting at the first sign of disease or as a preventive measure during periods of high disease pressure.
   - Rotate between different chemical classes to reduce the risk of resistance development.

5. **Weather Monitoring**:
   - Monitor weather conditions, particularly humidity and rainfall, which can promote bacterial spot development.
   - Adjust irrigation practices to avoid prolonged leaf wetness, as this creates favorable conditions for the disease.

6. **Integrated Pest Management (IPM)**:
   - Implement an integrated approach to disease management that combines cultural practices, sanitation, chemical control, and biological control methods.
   - Regular scouting and monitoring for disease symptoms and pest activity are essential components of IPM.

By incorporating these strategies into an integrated disease management program, growers can effectively manage bacterial spot in tomatoes and minimize its impact on yield and quality. Regular monitoring, timely intervention, and adherence to best management practices are critical for successful disease control."""

Tomato___Early_blight= """ Early blight, caused by the fungus Alternaria solani, is a common and destructive disease affecting tomatoes. Managing early blight requires a combination of cultural, biological, and chemical control methods. Here are some treatment options:

1. **Cultural Practices**:
   - Crop Rotation: Rotate tomatoes with non-host crops such as grains or legumes to break the disease cycle and reduce inoculum levels in the soil.
   - Sanitation: Remove and destroy infected plant debris, including affected leaves and stems, to reduce the source of fungal inoculum.
   - Mulching: Apply organic mulch around tomato plants to reduce soil splash and minimize the spread of spores from the soil to the lower leaves.
   - Proper Spacing: Plant tomatoes with adequate spacing to promote air circulation and reduce humidity within the canopy, which can help prevent disease development.

2. **Resistant Varieties**:
   - Plant tomato varieties that are resistant or tolerant to early blight, if available. Resistant varieties can significantly reduce disease severity.
   - Consult with local agricultural extension services or seed suppliers for information on resistant tomato varieties suitable for your region.

3. **Biological Control**:
   - Some biocontrol agents, such as certain strains of Bacillus spp. or Trichoderma spp., can suppress fungal populations and reduce disease severity.
   - Biocontrol products can be applied preventively or as part of an integrated disease management program.

4. **Chemical Control**:
   - Fungicides: Apply fungicides labeled for early blight control, following recommended rates and application timings.
   - Common fungicides used for early blight management in tomatoes include those containing active ingredients such as chlorothalonil, mancozeb, azoxystrobin, and copper-based products.
   - Rotate between different chemical classes to reduce the risk of resistance development.

5. **Weather Monitoring**:
   - Monitor weather conditions, particularly humidity and rainfall, which can promote early blight development.
   - Adjust irrigation practices to avoid prolonged leaf wetness, as this creates favorable conditions for the disease.

6. **Integrated Pest Management (IPM)**:
   - Implement an integrated approach to disease management that combines cultural practices, sanitation, chemical control, and biological control methods.
   - Regular scouting and monitoring for disease symptoms and pest activity are essential components of IPM.

By incorporating these strategies into an integrated disease management program, growers can effectively manage early blight in tomatoes and minimize its impact on yield and quality. Regular monitoring, timely intervention, and adherence to best management practices are critical for successful disease control."""

Tomato___Late_blight= """ Late blight, caused by the oomycete pathogen Phytophthora infestans, is a devastating disease affecting tomatoes and potatoes. Managing late blight requires a combination of cultural, biological, and chemical control methods. Here are some treatment options:

1. **Cultural Practices**:
   - Crop Rotation: Rotate tomatoes with non-host crops such as grains or legumes to break the disease cycle and reduce inoculum levels in the soil.
   - Sanitation: Remove and destroy infected plant debris, including affected leaves, stems, and fruit, to reduce the source of fungal inoculum.
   - Proper Spacing: Plant tomatoes with adequate spacing to promote air circulation and reduce humidity within the canopy, which can help prevent disease development.
   - Mulching: Apply organic mulch around tomato plants to reduce soil splash and minimize the spread of spores from the soil to the lower leaves.

2. **Resistant Varieties**:
   - Plant tomato varieties that are resistant or tolerant to late blight, if available. Resistant varieties can significantly reduce disease severity.
   - Consult with local agricultural extension services or seed suppliers for information on resistant tomato varieties suitable for your region.

3. **Biological Control**:
   - Some biocontrol agents, such as certain strains of Bacillus spp. or Trichoderma spp., can suppress fungal populations and reduce disease severity.
   - Biocontrol products can be applied preventively or as part of an integrated disease management program.

4. **Chemical Control**:
   - Fungicides: Apply fungicides labeled for late blight control, following recommended rates and application timings.
   - Common fungicides used for late blight management in tomatoes include those containing active ingredients such as chlorothalonil, mancozeb, azoxystrobin, and copper-based products.
   - Rotate between different chemical classes to reduce the risk of resistance development.

5. **Weather Monitoring**:
   - Monitor weather conditions, particularly humidity and rainfall, which can promote late blight development.
   - Adjust irrigation practices to avoid prolonged leaf wetness, as this creates favorable conditions for the disease.

6. **Integrated Pest Management (IPM)**:
   - Implement an integrated approach to disease management that combines cultural practices, sanitation, chemical control, and biological control methods.
   - Regular scouting and monitoring for disease symptoms and pest activity are essential components of IPM.

By incorporating these strategies into an integrated disease management program, growers can effectively manage late blight in tomatoes and minimize its impact on yield and quality. Regular monitoring, timely intervention, and adherence to best management practices are critical for successful disease control."""

Tomato___Leaf_Mold= """ Leaf mold, caused by the fungus Fulvia fulva (formerly Cladosporium fulvum), is a common disease affecting tomatoes, particularly in areas with high humidity and poor air circulation. Managing leaf mold requires a combination of cultural, biological, and chemical control methods. Here are some treatment options:

1. **Cultural Practices**:
   - Proper Spacing: Plant tomatoes with adequate spacing to promote air circulation and reduce humidity within the canopy, which can help prevent disease development.
   - Pruning: Prune tomato plants to remove excess foliage and improve airflow, reducing humidity levels and creating an environment less favorable for fungal growth.
   - Mulching: Apply organic mulch around tomato plants to reduce soil splash and minimize the spread of spores from the soil to the lower leaves.
   - Avoid Overhead Irrigation: Water the plants at the base to keep the foliage dry. Wet leaves provide an ideal environment for fungal growth.

2. **Resistant Varieties**:
   - Plant tomato varieties that are resistant or tolerant to leaf mold, if available. Resistant varieties can significantly reduce disease severity.
   - Consult with local agricultural extension services or seed suppliers for information on resistant tomato varieties suitable for your region.

3. **Biological Control**:
   - Some biocontrol agents, such as certain strains of Bacillus spp. or Trichoderma spp., can suppress fungal populations and reduce disease severity.
   - Biocontrol products can be applied preventively or as part of an integrated disease management program.

4. **Chemical Control**:
   - Fungicides: Apply fungicides labeled for leaf mold control, following recommended rates and application timings.
   - Common fungicides used for leaf mold management in tomatoes include those containing active ingredients such as chlorothalonil, mancozeb, azoxystrobin, and copper-based products.
   - Rotate between different chemical classes to reduce the risk of resistance development.

5. **Weather Monitoring**:
   - Monitor weather conditions, particularly humidity and rainfall, which can promote leaf mold development.
   - Adjust irrigation practices to avoid prolonged leaf wetness, as this creates favorable conditions for the disease.

6. **Integrated Pest Management (IPM)**:
   - Implement an integrated approach to disease management that combines cultural practices, sanitation, chemical control, and biological control methods.
   - Regular scouting and monitoring for disease symptoms and pest activity are essential components of IPM.

By incorporating these strategies into an integrated disease management program, growers can effectively manage leaf mold in tomatoes and minimize its impact on yield and quality. Regular monitoring, timely intervention, and adherence to best management practices are critical for successful disease control."""

Tomato___Septoria_leaf_spot= """ Septoria leaf spot, caused by the fungus Septoria lycopersici, is a common foliar disease affecting tomatoes. Managing Septoria leaf spot requires a combination of cultural, biological, and chemical control methods. Here are some treatment options:

1. **Cultural Practices**:
   - Crop Rotation: Rotate tomatoes with non-host crops such as grains or legumes to break the disease cycle and reduce inoculum levels in the soil.
   - Sanitation: Remove and destroy infected plant debris, including affected leaves and stems, to reduce the source of fungal inoculum.
   - Proper Spacing: Plant tomatoes with adequate spacing to promote air circulation and reduce humidity within the canopy, which can help prevent disease development.
   - Mulching: Apply organic mulch around tomato plants to reduce soil splash and minimize the spread of spores from the soil to the lower leaves.

2. **Resistant Varieties**:
   - Plant tomato varieties that are resistant or tolerant to Septoria leaf spot, if available. Resistant varieties can significantly reduce disease severity.
   - Consult with local agricultural extension services or seed suppliers for information on resistant tomato varieties suitable for your region.

3. **Biological Control**:
   - Some biocontrol agents, such as certain strains of Bacillus spp. or Trichoderma spp., can suppress fungal populations and reduce disease severity.
   - Biocontrol products can be applied preventively or as part of an integrated disease management program.

4. **Chemical Control**:
   - Fungicides: Apply fungicides labeled for Septoria leaf spot control, following recommended rates and application timings.
   - Common fungicides used for Septoria leaf spot management in tomatoes include those containing active ingredients such as chlorothalonil, mancozeb, azoxystrobin, and copper-based products.
   - Rotate between different chemical classes to reduce the risk of resistance development.

5. **Weather Monitoring**:
   - Monitor weather conditions, particularly humidity and rainfall, which can promote Septoria leaf spot development.
   - Adjust irrigation practices to avoid prolonged leaf wetness, as this creates favorable conditions for the disease.

6. **Integrated Pest Management (IPM)**:
   - Implement an integrated approach to disease management that combines cultural practices, sanitation, chemical control, and biological control methods.
   - Regular scouting and monitoring for disease symptoms and pest activity are essential components of IPM.

By incorporating these strategies into an integrated disease management program, growers can effectively manage Septoria leaf spot in tomatoes and minimize its impact on yield and quality. Regular monitoring, timely intervention, and adherence to best management practices are critical for successful disease control."""

Tomato___Spider_mites_Two_spotted_spider_mite= """ Controlling spider mites, particularly the two-spotted spider mite (Tetranychus urticae), on tomatoes requires a multifaceted approach. Here's how you can manage these pests effectively:

1. **Cultural Control**:
   - Pruning: Remove heavily infested leaves to reduce spider mite populations and improve air circulation, which can help deter further infestation.
   - Weed Management: Keep the area around tomato plants free of weeds, as they can harbor spider mites and provide alternative hosts.
   - Avoid Overhead Watering: Spider mites thrive in dry conditions, so water tomato plants at the base to keep foliage dry and minimize mite infestations.

2. **Biological Control**:
   - Predatory Mites: Introduce predatory mites such as Phytoseiulus persimilis or Neoseiulus californicus, which feed on spider mites and help control their populations.
   - Ladybugs: Release ladybugs (predatory beetles) in the tomato garden, as they also feed on spider mites and can contribute to their suppression.

3. **Chemical Control**:
   - Insecticidal Soap: Apply insecticidal soap solutions to tomato plants, focusing on the undersides of leaves where spider mites congregate. Repeat applications as necessary.
   - Horticultural Oil: Use horticultural oils to smother spider mite populations. Apply according to label instructions, especially during cooler temperatures to avoid plant damage.
   - Acaricides: Apply acaricides (miticides) labeled for use against spider mites. Rotate between different chemical classes to prevent resistance development. Follow label instructions carefully.

4. **Cultural Practices**:
   - Monitor: Regularly inspect tomato plants for signs of spider mite infestation, including stippling, webbing, and small moving dots (mites) on the undersides of leaves.
   - Early Detection: Detect spider mite infestations early to prevent population explosions. Consider using a hand lens or magnifying glass for better visibility.
   - High-Quality Plants: Start with healthy transplants from reputable sources, as stressed plants are more susceptible to spider mite attacks.

5. **Natural Enemies**:
   - Encourage biodiversity in the garden to attract natural enemies of spider mites, such as predatory insects and spiders.
   - Plant companion plants known to repel spider mites, such as marigolds, garlic, and chives, around tomato plants to deter infestations.

6. **Integrated Pest Management (IPM)**:
   - Implement an integrated approach to pest management that combines cultural, biological, and chemical control methods.
   - Rotate control methods and monitor the effectiveness of each strategy to maintain sustainable pest control.

By implementing these strategies, you can effectively manage spider mites, including the two-spotted spider mite, on tomato plants while minimizing the use of chemical pesticides and promoting a healthy garden ecosystem.""" 

Tomato___Target_Spot= """ Target spot, caused by the fungus Corynespora cassiicola, is a foliar disease that can affect tomatoes. Managing target spot involves several strategies aimed at reducing the spread of the fungus and minimizing its impact on plant health and yield. Here are some treatment options:

1. **Cultural Practices**:
   - Crop Rotation: Rotate tomatoes with non-host crops to break the disease cycle and reduce inoculum levels in the soil.
   - Sanitation: Remove and destroy infected plant debris, including affected leaves and stems, to reduce the source of fungal inoculum.
   - Proper Spacing: Plant tomatoes with adequate spacing to promote air circulation and reduce humidity within the canopy, which can help prevent disease development.
   - Mulching: Apply organic mulch around tomato plants to reduce soil splash and minimize the spread of spores from the soil to the lower leaves.

2. **Resistant Varieties**:
   - Plant tomato varieties that are resistant or tolerant to target spot, if available. Resistant varieties can significantly reduce disease severity.
   - Consult with local agricultural extension services or seed suppliers for information on resistant tomato varieties suitable for your region.

3. **Biological Control**:
   - Some biocontrol agents, such as certain strains of Bacillus spp. or Trichoderma spp., can suppress fungal populations and reduce disease severity.
   - Biocontrol products can be applied preventively or as part of an integrated disease management program.

4. **Chemical Control**:
   - Fungicides: Apply fungicides labeled for target spot control, following recommended rates and application timings.
   - Common fungicides used for target spot management in tomatoes include those containing active ingredients such as chlorothalonil, mancozeb, azoxystrobin, and copper-based products.
   - Rotate between different chemical classes to reduce the risk of resistance development.

5. **Weather Monitoring**:
   - Monitor weather conditions, particularly humidity and rainfall, which can promote target spot development.
   - Adjust irrigation practices to avoid prolonged leaf wetness, as this creates favorable conditions for the disease.

6. **Integrated Pest Management (IPM)**:
   - Implement an integrated approach to disease management that combines cultural practices, sanitation, chemical control, and biological control methods.
   - Regular scouting and monitoring for disease symptoms and pest activity are essential components of IPM.

By incorporating these strategies into an integrated disease management program, growers can effectively manage target spot in tomatoes and minimize its impact on yield and quality. Regular monitoring, timely intervention, and adherence to best management practices are critical for successful disease control.""" 

Tomato___Tomato_Yellow_Leaf_Curl_Virus= """ Tomato Yellow Leaf Curl Virus (TYLCV) is a devastating viral disease affecting tomatoes, transmitted primarily by the silverleaf whitefly (Bemisia tabaci). Unfortunately, there is no cure for viral diseases like TYLCV once a plant is infected. However, there are several management strategies to help prevent the virus from spreading and reduce its impact:

1. **Resistant Varieties**:
   - Plant tomato varieties that are resistant or tolerant to TYLCV, if available. Resistant varieties can significantly reduce the severity of the disease.
   - Consult with local agricultural extension services or seed suppliers for information on resistant tomato varieties suitable for your region.

2. **Vector Control**:
   - Manage Whiteflies: Implement control measures to manage populations of the silverleaf whitefly, the primary vector of TYLCV.
   - Use Yellow Sticky Traps: Place yellow sticky traps around tomato plants to attract and capture adult whiteflies, reducing their numbers.

3. **Sanitation**:
   - Remove Infected Plants: Promptly remove and destroy tomato plants showing symptoms of TYLCV to prevent the virus from spreading to healthy plants.
   - Weed Control: Keep the area around tomato plants free of weeds, as they can serve as alternative hosts for whiteflies and TYLCV.

4. **Physical Barriers**:
   - Use Row Covers: Install row covers over tomato plants to physically block whiteflies from accessing the plants and transmitting the virus.

5. **Resistant Companion Plants**:
   - Interplant with Repellent Plants: Some plants, such as marigolds and basil, are known to repel whiteflies. Interplanting these repellent plants with tomatoes may help reduce whitefly populations.

6. **Timing**:
   - Planting Time: Consider planting tomatoes during periods when whitefly populations are lower to reduce the risk of virus transmission.
   - Early Detection: Monitor tomato plants regularly for symptoms of TYLCV and take action promptly if symptoms are observed.

7. **Chemical Control** (Use with Caution):
   - Insecticides: Insecticides can be used to manage whitefly populations, but they should be used judiciously and in combination with other control measures to avoid the development of insecticide resistance.
   - Consult with local agricultural authorities or extension services for recommendations on insecticides approved for whitefly management in your area.

It's essential to employ an integrated approach to manage TYLCV effectively. By combining cultural practices, vector control, sanitation, and other management strategies, growers can help minimize the impact of Tomato Yellow Leaf Curl Virus on tomato crops. Additionally, practicing good farm hygiene and following recommended planting and management practices can help reduce the risk of virus transmission and optimize overall crop health and productivity."""

Tomato___Tomato_mosaic_virus = """ Tomato Mosaic Virus (ToMV) is a highly contagious viral disease that affects tomatoes, causing significant yield loss and reducing fruit quality. Unfortunately, there is no cure for viral infections once a plant is infected. However, there are several management strategies to help prevent the spread of Tomato Mosaic Virus and minimize its impact on tomato crops:

1. **Resistant Varieties**:
   - Plant tomato varieties that are resistant or tolerant to Tomato Mosaic Virus, if available. Resistant varieties can significantly reduce the severity of the disease.
   - Consult with local agricultural extension services or seed suppliers for information on resistant tomato varieties suitable for your region.

2. **Sanitation**:
   - Remove Infected Plants: Promptly remove and destroy tomato plants showing symptoms of Tomato Mosaic Virus to prevent the virus from spreading to healthy plants.
   - Weed Control: Keep the area around tomato plants free of weeds, as they can serve as alternative hosts for the virus.

3. **Vector Control**:
   - Manage Aphids: Aphids can transmit Tomato Mosaic Virus between plants. Implement control measures to manage aphid populations and reduce virus transmission.
   - Use Reflective Mulches: Reflective mulches placed around tomato plants can deter aphids and reduce the spread of Tomato Mosaic Virus.

4. **Physical Barriers**:
   - Use Row Covers: Install row covers over tomato plants to physically block aphids from accessing the plants and transmitting the virus.

5. **Resistant Companion Plants**:
   - Interplant with Repellent Plants: Some plants, such as garlic and chives, are known to repel aphids. Interplanting these repellent plants with tomatoes may help reduce aphid populations.

6. **Timing**:
   - Planting Time: Consider planting tomatoes during periods when aphid populations are lower to reduce the risk of virus transmission.
   - Early Detection: Monitor tomato plants regularly for symptoms of Tomato Mosaic Virus and take action promptly if symptoms are observed.

7. **Chemical Control** (Use with Caution):
   - Insecticides: Insecticides can be used to manage aphid populations, but they should be used judiciously and in combination with other control measures to avoid the development of insecticide resistance.
   - Consult with local agricultural authorities or extension services for recommendations on insecticides approved for aphid management in your area.

It's essential to employ an integrated approach to manage Tomato Mosaic Virus effectively. By combining cultural practices, vector control, sanitation, and other management strategies, growers can help minimize the impact of the virus on tomato crops. Additionally, practicing good farm hygiene and following recommended planting and management practices can help reduce the risk of virus transmission and optimize overall crop health and productivity."""

Tomato___healthy= """**Healthy Tomato Plants**

Tomatoes, known scientifically as *Solanum lycopersicum*, are not only a culinary favorite but also a vital crop in agriculture. A healthy tomato plant is the cornerstone of a fruitful harvest and is characterized by several key features:

**Vital Signs of Health:**
- **Robust Growth:** Healthy tomato plants have strong, upright stems with vibrant green foliage¹.
- **Flower Formation:** Bright yellow flowers bloom, indicating the plant is ready to produce fruit¹.
- **Fruit Appearance:** Look for tomatoes that are uniformly colored (usually red), firm, and free from spots or lesions¹.

**Cultivation Best Practices:**
- **Sunlight Exposure:** Tomato plants require full sun for at least 6-8 hours per day¹.
- **Soil Conditions:** They thrive in well-draining soil with a pH of 6.0 to 7.5, rich in organic matter¹.
- **Watering Routine:** Consistent watering is crucial, allowing the soil to dry slightly between sessions¹.

**Disease Prevention Strategies:**
- **Crop Rotation:** This helps prevent soil-borne diseases and maintains soil health.
- **Regular Monitoring:** Keep an eye out for pests or unusual spots on leaves and fruits, and take action if needed.

By adhering to these guidelines, farmers can ensure their tomato plants remain healthy and productive, providing a bountiful and disease-free harvest.

---
"""





arr_sol = [ Apple___Apple_scab,  Apple___Black_rot, Apple___Cedar_apple_rust,Apple___healthy ,Blueberry___healthy,
Cherry___Powdery_mildew,
Cherry___healthy,
corn_maiz_clsglf,
Corn_maize___Common_rust,
Corn_maize___Northern_Leaf_Blight,
Corn_maize___healthy,
Grape___Black_rot,
Grape___Esca_Black_Measles,
Grape___Leaf_blight_Isariopsis_Leaf_Spot,
Grape___healthy,
Orange___Haunglongbing_Citrus_greening,
Peach___Bacterial_spot,
Peach___healthy,
Pepper_bell___Bacterial_spot,
Pepper_bell___healthy,
Potato___Early_blight,
Potato___Late_blight,
Potato___healthy,
Raspberry___healthy,
Soybean___healthy,
Squash___Powdery_mildew,
Strawberry___Leaf_scorch,
Strawberry___healthy,
Tomato___Bacterial_spot,
Tomato___Early_blight,
Tomato___Late_blight,
Tomato___Leaf_Mold,
Tomato___Septoria_leaf_spot,
Tomato___Spider_mites_Two_spotted_spider_mite,
Tomato___Target_Spot,
Tomato___Tomato_Yellow_Leaf_Curl_Virus,
Tomato___Tomato_mosaic_virus,
Tomato___healthy
]

 #Prediction page

st.header("Please upload image... So we can Predict...")
test_image = st.file_uploader("Choose image: ")
if(st.button("Show image")):
    st.image(test_image, use_column_width =True)
# predict
if(st.button("Predict")):
    st.write("Prediction: ")
   #  st.write(os.path.isfile("./trained_model.keras"))
    result_index = model_prediction(test_image)
    #class
    class_name = ['Apple___Apple_scab',
 'Apple___Black_rot',
 'Apple___Cedar_apple_rust',
 'Apple___healthy',
 'Blueberry___healthy',
 'Cherry___Powdery_mildew',
 'Cherry___healthy',
 'Corn_maize___Cercospora_leaf_spot_Gray_leaf_spot',
 'Corn_maize___Common_rust_',
 'Corn_maize___Northern_Leaf_Blight',
 'Corn_maize___healthy',
 'Grape___Black_rot',
 'Grape___Esca_Black_Measles',
 'Grape___Leaf_blight_Isariopsis_Leaf_Spot',
 'Grape___healthy',
 'Orange___Haunglongbing_Citrus_greening',
 'Peach___Bacterial_spot',
 'Peach___healthy',
 'Pepper_bell___Bacterial_spot',
 'Pepper_bell___healthy',
 'Potato___Early_blight',
 'Potato___Late_blight',
 'Potato___healthy',
 'Raspberry___healthy',
 'Soybean___healthy',
 'Squash___Powdery_mildew',
 'Strawberry___Leaf_scorch',
 'Strawberry___healthy',
 'Tomato___Bacterial_spot',
 'Tomato___Early_blight',
 'Tomato___Late_blight',
 'Tomato___Leaf_Mold',
 'Tomato___Septoria_leaf_spot',
 'Tomato___Spider_mites_Two_spotted_spider_mite',
 'Tomato___Target_Spot',
 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
 'Tomato___Tomato_mosaic_virus',
 'Tomato___healthy']
    st.write("Predicted Disease is: ")
    st.success("{}".format(class_name[result_index]))

    for i in range(0,39):
       if(i == result_index):
          st.write(arr_sol[result_index])

 
                
