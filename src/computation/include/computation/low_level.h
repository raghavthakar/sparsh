#ifndef LOW_LEVEL_H
#define LOW_LEVEL_H

#include <string>
#include <map>

// Declaring a Function Pointer
// Verbose: return_type (foo*)(signature) 
typedef void (*function)(void);

// Declaring a hash map for the incoming string values and initializing
// the function through the key element
typedef std::map<std::string, function> function_map_;

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
        
        // Declaration of Constructor
        public: Controller();

        // Defining of functions for low level control
        public: void number_filter(int_fast16_t); //Trivia: int_fast16_t is faster than int
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
        function_map_var_.emplace();
    }
} // namespace ActuatePiston

#endif