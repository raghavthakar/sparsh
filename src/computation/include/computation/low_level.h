#ifndef LOW_LEVEL_H
#define LOW_LEVEL_H

#include <string>
#include <map>
#include <string>
#include <vector>
#include <math.h>
// Declaring a Function Pointer
// Verbose: return_type (foo*)(signature) 
typedef void (*function)(void);

// Declaring a hash map for the incoming string values and initializing
// the function through the key element
typedef std::map<int_fast16_t, function> function_map_;

// Declaring a string of vector to return values to left_num_ and 
// right_num_ from number_filter function in class Controller
typedef std::vector<int_fast16_t> vect_int;

namespace ActuatePiston
{
    class Controller {

        /* left_num_ and right_num_ are two string variables which will be extracted 
        from a subscriber in main Controller class  which will divide the incoming number into two parts
        Eg: Incoming number = 67 
            left_num_ = 6
            right_num_ = 7
        */
        private: std::string left_num_;
        private: std::string right_num_;
        
        // Declaring a variable for the typedef function_map_
        private: function_map_ function_map_var_;
        
        private: vect_int vect_string_val_;
        // Declaration of Constructor
        public: Controller();

        // Defining of functions for low level control
        public: vect_int number_filter(int_fast16_t); //Trivia: int_fast16_t is faster than int
        public: void all_up();
        public: void reset();
        public: void reset_left();
        public: void reset_right();
        public: void _10();
        public: void _20();
        public: void _30();
        public: void _40();
        public: void _50();
        public: void _60();
        public: void _70();
        public: void _1();
        public: void _2();
        public: void _3();
        public: void _4();
        public: void _5();
        public: void _6();
        public: void _7();

        // This caller will be used to initiate the function based on left_num_
        // and right_num_ in the input stream
        private: void caller(function_map_&, const std::string&);

    };


    Controller::Controller(){
        // Add the key and elements here.
        // Trivia: Emplace is a faster version of insert
        function_map_var_.emplace(10, &_10);
        function_map_var_.emplace(20, &_20);
        function_map_var_.emplace(30, &_30);
        function_map_var_.emplace(40, &_40);
        function_map_var_.emplace(50, &_50);
        function_map_var_.emplace(60, &_60);
        function_map_var_.emplace(70, &_70);
        function_map_var_.emplace(1, &_1);
        function_map_var_.emplace(2, &_2);
        function_map_var_.emplace(3, &_3);
        function_map_var_.emplace(4, &_4);
        function_map_var_.emplace(5, &_5);
        function_map_var_.emplace(6, &_6);
        function_map_var_.emplace(7, &_7);

    }

    vect_int Controller::number_filter(int_fast16_t incoming_num)
    {
        int_fast16_t right = fmod(incoming_num, 10);
        incoming_num = fmod(incoming_num, 10);
        int_fast16_t left = floor(incoming_num);
        vect_int v;
        v.push_back(left);
        v.push_back(right);
        
        return v;
    }
} // namespace ActuatePiston

#endif