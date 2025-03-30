#################
### FUNCTIONS ###
#################

TMP_ARR_BUFFER=()

# function with parameters: original_text, text_to_replace
replace_text() {
    sed -i "s/$1/$2/g" pyproject.toml
}

# search the text in the file
search_string_in_file() {
    local string="$1"
    local file="$2"

    if grep -q "$string" "$file"; then
        echo -e "\033[0;32mDONE\033[0m String '$string' found in $file"
        return 0
    else
        echo -e "\033[0;31mFAIL\033[0m String '$string' NOT found in $file"
        return 1
    fi
}

# function to make a key merge with an array of values
generate_array() {
    local key="$1"
    shift
    local values=("$@")
    local list=()
    for value in "${values[@]}"; do
        list+=("${key} = ${value}")
    done

    TMP_ARR_BUFFER=()
    TMP_ARR_BUFFER+=("${list[@]}")  # Store the generated array in a temporary buffer
}

# merge and then append
merge_to_string() {
    local prefix="$1"
    shift  # Remove the first argument (prefix)
    local list=$(generate_array ${prefix} "$@")
    
    local result_string="$prefix: "
    for part in "${list[@]}"; do
        result_string+="$part "
    done

    # Trim the trailing space and return the string
    echo "${result_string% }"
}

# Function to convert a string into an array and output it
convert_string_to_array() {
    local string="$1"
    # Extract the part after the first colon and split by space into the array
    IFS=' ' read -r -a temp_array <<< "${string#*:}"
    
    # Output the array (space-separated)
    # Get the result by array_result=($(convert_string_to_array "array1:value1a value1b value1c"))
    echo "${temp_array[@]}"
}

#############################
### EXPERIMENT PARAMETERS ###
#############################
# IMPORTANT: enter 1. the number of experiments to run 2. the number of arrays of paramters you set
echo "[HYPERPARAMETERS SETTING]"
n=2
num_arrays=4
pyproject_file="pyproject.toml"

# number of clients
p_key="options.num-supernodes"
p_value=(\
2 \
4 \
)
search_string_in_file "${p_key} =" "${pyproject_file}" || exit 1
p_original=$(cat "${pyproject_file}" | grep "${p_key} = [0-9]\+")
generate_array "${p_key}" "${p_value[@]}"
p_arr1+=("${p_original}" "${TMP_ARR_BUFFER[@]}")

# number of rounds
p_key="num-server-rounds"
p_value=(\
3 \
5 \
)
search_string_in_file "${p_key} =" "${pyproject_file}" || exit 1
p_original=$(cat "${pyproject_file}" | grep "${p_key} = [0-9]\+")
generate_array "${p_key}" "${p_value[@]}"
p_arr2+=("${p_original}" "${TMP_ARR_BUFFER[@]}")

# learning rate
p_key="learning-rate"
p_value=(\
0.1 \
0.01 \
0.001 \
0.0001 \
)
search_string_in_file "${p_key} =" "${pyproject_file}" || exit 1
p_original=$(cat "${pyproject_file}" | grep "${p_key} = [0-9]\+")
generate_array "${p_key}" "${p_value[@]}"
p_arr3+=("${p_original}" "${TMP_ARR_BUFFER[@]}")

# hetero
p_key="hetero"
p_value=(\
0 \
1 \
)
search_string_in_file "${p_key} =" "${pyproject_file}" || exit 1
p_original=$(cat "${pyproject_file}" | grep "${p_key} = [0-9]\+")
generate_array "${p_key}" "${p_value[@]}"
p_arr4+=("${p_original}" "${TMP_ARR_BUFFER[@]}")


###########################
### EXPERIMENT CHECKING ###
###########################

echo "[CHECKING HYPERPARAMETERS]"
echo "Number of experiments: $n"
echo "Kinds of parameters: $num_arrays"

# check the number of parameters match n
for ((i=0; i<num_arrays; i++)); do
    array_name="p_arr$((i+1))"
    eval "current_array=(\"\${$array_name[@]}\")"

    arr_length=${#current_array[@]}
    current_array_length=${#current_array[@]}
    if [ $(($current_array_length-1)) -lt $n ]; then
        echo -e "\033[0;31mFAIL\033[0m len(${array_name})=$(($arr_length-1)) is less than n=${n}. Please check the parameters."
        exit 1
    elif [ $(($current_array_length-1)) -gt $n ]; then
        echo -e "\033[0;33mWARNING\033[0m len(${array_name})=$(($arr_length-1)) is greater than n=${n}. Keep going and some of the parameters will not be set in experiments."
    else
        continue
    fi
done

# dry run
echo "[DRY RUN]"
for i in $(seq 1 $n); do
    # check previous hyperparameters exist for each array (p_arr1, p_arr2...)
    for ((j=1; j<=num_arrays; j++)); do
        array_name="p_arr$j"
        eval "current_array=(\"\${$array_name[@]}\")"
        search_string_in_file "${current_array[$i-1]}" pyproject.toml || $(echo "Failed in EXPERIMENT #$i"; exit 1)
    done

    # test replacing the hyperparameters for each array (p_arr1, p_arr2...)
    for ((j=1; j<=num_arrays; j++)); do
        array_name="p_arr$j"
        eval "current_array=(\"\${$array_name[@]}\")"
        # replace the hyperparameters
        replace_text "${current_array[$i-1]}" "${current_array[$i]}"
        echo "replace ${current_array[$i-1]} -> ${current_array[$i]}"
    done
done

# recover the original pyproject.toml for each array (p_arr1, p_arr2...)
for ((j=1; j<=num_arrays; j++)); do
    array_name="p_arr$j"
    eval "current_array=(\"\${$array_name[@]}\")"
    # replace the hyperparameters
    replace_text "${current_array[$n]}" "${current_array[0]}"
    echo "recover ${current_array[$n]} -> ${current_array[0]}"
done
echo "[DRY RUN] DONE"

#######################
### RUN EXPERIMENTS ###
#######################

# doing the experiments (1~n, including n)
for i in $(seq 1 $n); do
    echo -e "\n===\n[EXPERIMENT #$i]\n"

    echo -e "[Replace Config]"
    for ((j=1; j<=num_arrays; j++)); do
        array_name="p_arr$j"
        eval "current_array=(\"\${$array_name[@]}\")"
        # replace the hyperparameters
        replace_text "${current_array[$i-1]}" "${current_array[$i]}"
        echo "replace ${current_array[$i-1]} -> ${current_array[$i]}"
    done

    # run the experiment
    cat pyproject.toml
    flwr run .
    # end
    echo -e "\n[EXPERIMENT #$i] DONE\n===\n"
done