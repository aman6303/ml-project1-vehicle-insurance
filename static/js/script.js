document.addEventListener("DOMContentLoaded", function() {
    // 1. Loading State Animation
    const form = document.getElementById('predictionForm');
    const btn = document.getElementById('predictBtn');
    
    if(form && btn) {
        form.addEventListener('submit', function() {
            btn.classList.add('loading');
            btn.querySelector('.btn-text').innerText = 'Processing...';
            btn.disabled = true;
        });
    }

    // Attach event listeners for Vehicle Age logic
    const ageLt1 = document.getElementById('Vehicle_Age_lt_1_Year');
    const ageGt2 = document.getElementById('Vehicle_Age_gt_2_Years');

    if(ageLt1 && ageGt2) {
        ageLt1.addEventListener('change', handleVehicleAgeLogic);
        ageGt2.addEventListener('change', handleVehicleAgeLogic);
    }
});

// 2. Smart Logic for Vehicle Age
function handleVehicleAgeLogic() {
    const ageLt1 = document.getElementById('Vehicle_Age_lt_1_Year');
    const ageGt2 = document.getElementById('Vehicle_Age_gt_2_Years');
    const form = document.getElementById('predictionForm');

    if (ageLt1.value === "1") {
        ageGt2.value = "0";
        ageGt2.disabled = true; 
        ensureHiddenInput(form, 'Vehicle_Age_gt_2_Years_hidden', 'Vehicle_Age_gt_2_Years', "0");
    } else if (ageGt2.value === "1") {
        ageLt1.value = "0";
        ageLt1.disabled = true;
        ensureHiddenInput(form, 'Vehicle_Age_lt_1_Year_hidden', 'Vehicle_Age_lt_1_Year', "0");
    } else {
        ageLt1.disabled = false;
        ageGt2.disabled = false;
        removeHiddenInput('Vehicle_Age_gt_2_Years_hidden');
        removeHiddenInput('Vehicle_Age_lt_1_Year_hidden');
    }
}

function ensureHiddenInput(form, id, name, value) {
    let existing = document.getElementById(id);
    if (!existing) {
        const input = document.createElement('input');
        input.type = 'hidden';
        input.id = id;
        input.name = name;
        input.value = value;
        form.appendChild(input);
    }
}

function removeHiddenInput(id) {
    const existing = document.getElementById(id);
    if (existing) existing.remove();
}