"use client";
import React , { useState, useEffect } from "react";
import { Label } from "@/components/ui/label"
import axios from 'axios';
import {PythonShell} from 'python-shell';
import * as XLSX from 'xlsx';

import path from 'path';
import os from 'os';
import fs from 'fs';


import {Chart} from "@/components/Chart";
import { Component } from "@/components/component";
import MultipleSelector, { Option } from '@/components/Features';
import {
    Table,
    TableBody,
    TableCaption,
    TableCell,
    TableFooter,
    TableHead,
    TableHeader,
    TableRow,
  } from "@/components/ui/table"

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group";
import { Switch } from "@/components/ui/switch"



// const OPTIONS: Option[] = [
//     { label: 'CorrelationCoefficient', value: 'CorrelationCoefficient' },
//     { label: 'QStatistics', value: 'QStatistics'  },
//     { label: 'DifferencesMeasure', value: 'DifferencesMeasure'  },
//     { label: 'DoubleFaultMeasure', value: 'DoubleFaultMeasure' },
//     { label: 'CombinationD_DF', value: 'CombinationD_DF'  },

//   ];


 export default function AboutPage() {
    



    const [selectedColumns, setSelectedColumns] = React.useState<Option[]>([]);
    const [file, setFile] = useState<File | null>(null);
    const [tableData, setTableData] = useState<any[][]>([]);
    const [columns, setColumns] = useState<Option[]>([]);
    const [selectorKey, setSelectorKey] = useState<number>(0);
    const [jsonData, setJsonData] = useState<any>(null);
    const [selectedMetrics, setSelectedMetrics] = React.useState<Option[]>([]);
    const [isPairwise, setisPairwise] = useState<boolean>(false);
    const [radioValue, setRadioValue] = useState<string>("Classification");
    const [options, setOptions] = React.useState<Option[]>([]);
    const [MetricselectorKey, setMetricSelectorKey] = useState<number>(0);
    
    
    useEffect(() => {
        const newOptions: Option[] = (() => {
            if (isPairwise && radioValue === "Classification") {
                return [
                    { label: 'Entropy', value: 'Entropy' },
                    { label: 'KohaviWolpertVariance', value: 'KohaviWolpertVariance' },
                    { label: 'MeasurementInterraterAgreement', value: 'MeasurementInterraterAgreement' },
                ];
            } else if (!isPairwise && radioValue === "Classification") {
                return [
                    { label: 'CorrelationCoefficient_clas', value: 'CorrelationCoefficient_clas' },
                    { label: 'QStatistics_clas', value: 'QStatistics_clas' },
                    { label: 'DifferencesMeasure', value: 'DifferencesMeasure' },
                    { label: 'DoubleFaultMeasure', value: 'DoubleFaultMeasure' },
                    { label: 'CombinationD_DF', value: 'CombinationD_DF' },
                ];
            } else if (isPairwise && radioValue === "Regression") {
                return [
                    { label: 'VarianceOutputs', value: 'VarianceOutputs' },
                    { label: 'Ambiguity', value: 'Ambiguity' },
                    { label: 'VariationCoefficient', value: 'VariationCoefficient' },
                    { label: 'DiversityDensity', value: 'DiversityDensity' },
                    { label: 'ErrorVariance', value: 'ErrorVariance' },
                    { label: 'AmbiguityDecomposition', value: 'AmbiguityDecomposition' },
                ];
            } else if (!isPairwise && radioValue === "Regression") {
                return [
                    { label: 'CorrelationCoefficient_reg', value: 'CorrelationCoefficient_reg' },
                    { label: 'MeanSquaredDifference', value: 'MeanSquaredDifference' },
                    { label: 'MeanAbsoluteDifference', value: 'MeanAbsoluteDifference' },
                    { label: 'ErrorCorrelation', value: 'ErrorCorrelation' },
                    { label: 'DisagreementMesure', value: 'DisagreementMesure' },
                    { label: 'RankCorrelation', value: 'RankCorrelation' },
                    { label: 'Qstatistic_reg', value: 'Qstatistic_reg' },
                    { label: 'CovarianceError', value: 'CovarianceError' },
                    { label: 'PartialCorrelationCoefficient', value: 'PartialCorrelationCoefficient' },
                    { label: 'DoubleFaultMeasure_reg', value: 'DoubleFaultMeasure_reg' },
                ];
            }
    
            return [];
        })();
        setOptions(newOptions);
        setMetricSelectorKey(prevKey => prevKey + 1);
        console.log("Options:", options);    
    }, [isPairwise, radioValue]);

    
    
    // Handle file upload
    const handleFileUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
        const uploadedFile = event.target.files?.[0];
        if (!uploadedFile) return;



        console.log("Uploaded file:", uploadedFile.name);
        setFile(uploadedFile);

        // Temporary file path (optional for other purposes)
        const tempFilePath = URL.createObjectURL(uploadedFile);
        console.log("Temporary file path:", tempFilePath);

        // Read the file using FileReader
        const reader = new FileReader();

        reader.onload = (e) => {
            const data = new Uint8Array(e.target?.result as ArrayBuffer);
            const workbook = XLSX.read(data, { type: "array" });
            const sheetName = workbook.SheetNames[0];
            const worksheet = XLSX.utils.sheet_to_json<any[]>(workbook.Sheets[sheetName], { header: 1 });

            setTableData(worksheet);

            // Extract column names from the first row
            const columnNames: Option[] = worksheet[0].map((col, index) => {
                if (index === worksheet[0].length - 1) {
                    return { label: col, value: col, disable: true };
                }
                return { label: col, value: col };
            });
            setColumns(columnNames);

   

            // Update selector key to trigger re-render if needed
            setSelectorKey((prevKey) => prevKey + 1);
        };

        // Handle file reading errors
        reader.onerror = (err) => {
            console.error("Error reading file:", err);
        };

        reader.readAsArrayBuffer(uploadedFile);
    };

    // Handle the process button click
    const handleProcessClick = async () => {
        try {
            if (!file) {
                console.error("No file selected.");
                return;
            }

            if (selectedColumns.length < 2) {
                console.error("Please select at least two columns.");
                return;
            }
            if (selectedMetrics.length < 1) {
                console.error("Please select at least one metric.");
                return;
            }

            const aa = {data: tableData, columns: selectedColumns.map(col => col.value),  metrics: selectedMetrics.map(metric => metric.value)};

            // Convert the table data into JSON format for the Python script
            console.log("Sending: ");
            console.log(aa);
            
            const jsonContent = JSON.stringify(aa);
            console.log("JSON content:", jsonContent);

            if (!jsonContent) {
                console.error("No JSON content available.");
                return;
            }

            // Pass the JSON content to the Electron function to process the Python script
            let result = await window.electron.runPythonScript("diversity_metrics/process_file.py", jsonContent);
            result = JSON.parse(result[result.length - 1]);

            console.log("Processed result:", result);

            // Update state with the result
            if (result.status === "success")
                setJsonData(result);
        } catch (error) {
            console.error("Error running Python script:", error);
        }
    };



    return (
        <div className="h-screen w-screen overflow-auto">
            <div className="grid grid-rows-[auto_auto] gap-4 h-full w-full">
                <div className="grid border p-4 grid-cols-2 gap-4">
                    <div className="grid h-auto border  p-4">
                        <Label htmlFor="email" >Upload your file:</Label>
                        <Input
                            type="file"
                            id="file"
                            accept=".xlsx,.xls"
                            onChange={handleFileUpload}
                        />
                        <RadioGroup defaultValue="Classification " onValueChange={setRadioValue}>
                        <div className="flex items-center space-x-2 mt-4">
                            <RadioGroupItem value="Classification" id="Classification" />
                            <Label htmlFor="Classification">Classification</Label>
                        </div>
                        <div className="flex items-center space-x-2 mt-4">
                            <RadioGroupItem value="Regression" id="Regression" />
                            <Label htmlFor="Regression">Regression</Label>
                        </div>
                        </RadioGroup>
                        <Switch onCheckedChange={(checked) => setisPairwise(checked)} />
                        <div className="mb-4"></div> {/* Add margin-bottom to give more space */}
                        <Label htmlFor="email">Choose the features to compute:</Label>
                        <MultipleSelector
                            key={selectorKey}
                            value={selectedColumns}
                            onChange={(newSelection) => {setSelectedColumns(newSelection)}}
                            defaultOptions={columns}
                            placeholder="Features you like..."
                            emptyIndicator={
                                <p className="text-center text-lg leading-10 text-gray-600 dark:text-gray-400">
                                    No results found.
                                </p>
                            }
                        />
                        <Label htmlFor="email">Choose the Metric:</Label>
                        <MultipleSelector
                            key={MetricselectorKey}
                            value = {selectedMetrics}
                            onChange={(newMetrics) => {setSelectedMetrics(newMetrics)}}
                            defaultOptions={options} // Use the options state
                            placeholder="Metric you like..."
                            emptyIndicator={
                                <p className="text-center text-lgnpm install xlsx leading-10 text-gray-600 dark:text-gray-400">
                                    No results found.
                                </p>
                            }
                        />
                        <Button className="top-0 left-0 mt-4 ml-4 p-2 w-auto h-auto" onClick={handleProcessClick}>Process</Button>
                    </div>
                    <div className="border max-h-50 max-w-full overflow-auto">
                        <Table>
                            <TableCaption>Data overview.</TableCaption>
                            <TableHeader>
                                <TableRow>
                                    {tableData[0] && tableData[0].map((header, index) => (
                                        <TableHead key={index}>{header}</TableHead>
                                    ))}
                                </TableRow>
                            </TableHeader>
                            <TableBody>
                                {tableData.slice(1).map((row, rowIndex) => (
                                    <TableRow key={rowIndex}>
                                        {row.map((cell, cellIndex) => (
                                            <TableCell key={cellIndex}>{cell}</TableCell>
                                        ))}
                                    </TableRow>
                                ))}
                            </TableBody>
                        </Table>
                    </div>
                </div>
                <div className="border p-4  max-h-full max-w-full">
                    <Label htmlFor="email">Calculation Report:</Label>
                    
                    <div className="mt-4">
                        <h3 className="font-bold text-lg">Report Summary</h3>
                        <p className="mt-2">Here is a summary of the calculation performed:</p>

                        <div className="mt-4">
                            <h4 className="font-semibold"></h4>
                            <ul className="list-disc ml-5">
                                <li><strong>Columns :</strong> C1 ,C2</li>
                                <li><strong>Metric:</strong> Qstatistics</li>
                            </ul>
                        </div>

                        <div className="mt-4 max-h-full max-w-full">
                            <h4 className="font-semibold">Detailed Breakdown:</h4>
                            <table className="min-w-full table-auto border-collapse border border-gray-200">
                                <tbody>
                                    {jsonData && Object.entries(jsonData.data).map(([key, value]) => (
                                   
                                    <TableRow key={key}>
                                        <TableCell className="border border-gray-300 p-2">{key}</TableCell>
                                        <TableCell className="border border-gray-300 p-2">{String(value)}</TableCell> {/* Cast value to string */}
                                    </TableRow>
                                   
                                    ))}
                                    <tr className="bg-gray-100">
                                        <td className="border border-gray-300 p-2">Discount (10%)</td>
                                        <td className="border border-gray-300 p-2">-$120</td>
                                    </tr>
                                    <tr className="font-bold">
                                        <td className="border border-gray-300 p-2">Final Amount</td>
                                        <td className="border border-gray-300 p-2">$1080</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
}