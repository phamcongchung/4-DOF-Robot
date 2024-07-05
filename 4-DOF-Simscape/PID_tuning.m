% Create slTuner interface
TunedBlocks = {'PD1', 'PD2', 'PD3', 'PD4'};
ST0 = slTuner('Assem',TunedBlocks);

% Mark outputs of PID blocks as plant inputs
addPoint(ST0,TunedBlocks);

% Mark joint angles as plant outputs
addPoint(ST0,'Mux2/thetad');

% Mark reference signals
RefSignals = {...
    'Assem/trajectory1/t1', 'Assem/trajectory1/t2', 'Assem/trajectory1/t3', 'Assem/trajectory1/t4'};
addPoint(ST0,RefSignals);

% Defining Inputs and Outputs and Tuning the system
Controls = TunedBlocks;                     % actuator commands
Measurements = 'Assem/Mux2/thetad';         % joint angle measurements
Options = looptuneOptions('RandomStart',80','UseParallel',true);
TR = TuningGoal.StepTracking(RefSignals,Measurements,0.05,0);
ST1 = looptune(ST0,Controls,Measurements,TR,Options);

% Update PID Block
writeBlockValue(ST1);