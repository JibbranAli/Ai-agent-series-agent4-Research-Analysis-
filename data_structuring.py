"""
Data Structuring and Output Formatting Module
Organizes research findings into structured outputs like tables, summaries, and charts
"""

import json
import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, asdict
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import logging
from jinja2 import Template
import io
import base64

logger = logging.getLogger(__name__)

@dataclass
class DataTable:
    """Represents a structured data table"""
    title: str
    columns: List[str]
    data: List[List[Any]]
    metadata: Dict[str, Any]
    source: str
    created_date: str

@dataclass
class ChartConfig:
    """Configuration for data visualization"""
    chart_type: str  # bar, line, pie, scatter, heatmap
    title: str
    x_axis: str
    y_axis: str
    color_scheme: str
    width: int
    height: int
    show_legend: bool
    show_grid: bool

@dataclass
class StructuredOutput:
    """Represents structured research output"""
    title: str
    summary: str
    tables: List[DataTable]
    charts: List[Dict[str, Any]]
    key_insights: List[str]
    recommendations: List[str]
    sources: List[str]
    metadata: Dict[str, Any]
    created_date: str

class DataStructurer:
    """Advanced data structuring and formatting engine"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        
        # Set up plotting style
        plt.style.use('seaborn-v0_8')
        sns.set_palette("husl")
        
        # Chart color schemes
        self.color_schemes = {
            'default': ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd'],
            'business': ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#7209B7'],
            'tech': ['#00D4AA', '#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'],
            'finance': ['#2C3E50', '#E74C3C', '#F39C12', '#27AE60', '#8E44AD']
        }
    
    def structure_research_data(self, research_data: Dict[str, Any], 
                               output_type: str = 'comprehensive') -> StructuredOutput:
        """
        Structure research data into organized output
        
        Args:
            research_data: Raw research data
            output_type: Type of output (comprehensive, summary, detailed)
            
        Returns:
            StructuredOutput object
        """
        logger.info(f"Structuring research data for output type: {output_type}")
        
        # Extract key components
        title = self._extract_title(research_data)
        summary = self._generate_summary(research_data)
        
        # Create data tables
        tables = self._create_data_tables(research_data)
        
        # Generate charts
        charts = self._generate_charts(research_data)
        
        # Extract insights and recommendations
        insights = self._extract_key_insights(research_data)
        recommendations = self._generate_recommendations(research_data)
        
        # Collect sources
        sources = self._collect_sources(research_data)
        
        # Create metadata
        metadata = self._create_metadata(research_data, output_type)
        
        structured_output = StructuredOutput(
            title=title,
            summary=summary,
            tables=tables,
            charts=charts,
            key_insights=insights,
            recommendations=recommendations,
            sources=sources,
            metadata=metadata,
            created_date=datetime.now().isoformat()
        )
        
        return structured_output
    
    def create_comparison_table(self, entities: List[Dict[str, Any]], 
                              comparison_fields: List[str]) -> DataTable:
        """
        Create a comparison table for multiple entities
        
        Args:
            entities: List of entities to compare
            comparison_fields: Fields to compare
            
        Returns:
            DataTable object
        """
        logger.info(f"Creating comparison table for {len(entities)} entities")
        
        # Prepare table data
        table_data = []
        for entity in entities:
            row = []
            for field in comparison_fields:
                value = entity.get(field, 'N/A')
                row.append(value)
            table_data.append(row)
        
        # Create metadata
        metadata = {
            'entity_count': len(entities),
            'comparison_fields': comparison_fields,
            'table_type': 'comparison'
        }
        
        table = DataTable(
            title=f"Comparison of {len(entities)} Entities",
            columns=comparison_fields,
            data=table_data,
            metadata=metadata,
            source="Research Agent Analysis",
            created_date=datetime.now().isoformat()
        )
        
        return table
    
    def create_summary_statistics(self, data: List[Dict[str, Any]], 
                                numeric_fields: List[str]) -> DataTable:
        """
        Create summary statistics table
        
        Args:
            data: Raw data
            numeric_fields: Fields to calculate statistics for
            
        Returns:
            DataTable with summary statistics
        """
        logger.info(f"Creating summary statistics for {len(numeric_fields)} fields")
        
        # Convert to DataFrame for easier calculation
        df = pd.DataFrame(data)
        
        # Calculate statistics
        stats_data = []
        for field in numeric_fields:
            if field in df.columns:
                field_data = pd.to_numeric(df[field], errors='coerce')
                stats = {
                    'Field': field,
                    'Count': field_data.count(),
                    'Mean': field_data.mean(),
                    'Median': field_data.median(),
                    'Std Dev': field_data.std(),
                    'Min': field_data.min(),
                    'Max': field_data.max()
                }
                stats_data.append(list(stats.values()))
        
        columns = ['Field', 'Count', 'Mean', 'Median', 'Std Dev', 'Min', 'Max']
        
        metadata = {
            'total_records': len(data),
            'numeric_fields': numeric_fields,
            'table_type': 'summary_statistics'
        }
        
        table = DataTable(
            title="Summary Statistics",
            columns=columns,
            data=stats_data,
            metadata=metadata,
            source="Research Agent Analysis",
            created_date=datetime.now().isoformat()
        )
        
        return table
    
    def create_trend_analysis_table(self, trends: List[Dict[str, Any]]) -> DataTable:
        """
        Create trend analysis table
        
        Args:
            trends: List of trend data
            
        Returns:
            DataTable with trend analysis
        """
        logger.info(f"Creating trend analysis table for {len(trends)} trends")
        
        table_data = []
        for trend in trends:
            row = [
                trend.get('name', 'Unknown'),
                trend.get('category', 'Unknown'),
                trend.get('growth_rate', 0),
                trend.get('adoption_level', 'Unknown'),
                trend.get('impact_level', 'Unknown'),
                trend.get('confidence_score', 0),
                trend.get('first_detected', 'Unknown')
            ]
            table_data.append(row)
        
        columns = [
            'Trend Name', 'Category', 'Growth Rate (%)', 
            'Adoption Level', 'Impact Level', 'Confidence Score', 'First Detected'
        ]
        
        metadata = {
            'trend_count': len(trends),
            'table_type': 'trend_analysis'
        }
        
        table = DataTable(
            title="Trend Analysis Summary",
            columns=columns,
            data=table_data,
            metadata=metadata,
            source="Research Agent Analysis",
            created_date=datetime.now().isoformat()
        )
        
        return table
    
    def generate_bar_chart(self, data: Dict[str, Any], config: ChartConfig) -> Dict[str, Any]:
        """
        Generate bar chart visualization
        
        Args:
            data: Data to visualize
            config: Chart configuration
            
        Returns:
            Dictionary containing chart data and metadata
        """
        logger.info(f"Generating bar chart: {config.title}")
        
        # Extract data for visualization
        categories = list(data.keys())
        values = list(data.values())
        
        # Create Plotly bar chart
        fig = go.Figure(data=[
            go.Bar(
                x=categories,
                y=values,
                marker_color=self.color_schemes[config.color_scheme][:len(categories)]
            )
        ])
        
        fig.update_layout(
            title=config.title,
            xaxis_title=config.x_axis,
            yaxis_title=config.y_axis,
            width=config.width,
            height=config.height,
            showlegend=config.show_legend,
            plot_bgcolor='white',
            paper_bgcolor='white'
        )
        
        if config.show_grid:
            fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
            fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        
        # Convert to JSON for storage
        chart_json = fig.to_json()
        
        return {
            'chart_type': 'bar',
            'title': config.title,
            'data': chart_json,
            'config': asdict(config),
            'created_date': datetime.now().isoformat()
        }
    
    def generate_line_chart(self, data: Dict[str, List[float]], config: ChartConfig) -> Dict[str, Any]:
        """
        Generate line chart visualization
        
        Args:
            data: Time series data
            config: Chart configuration
            
        Returns:
            Dictionary containing chart data and metadata
        """
        logger.info(f"Generating line chart: {config.title}")
        
        fig = go.Figure()
        
        colors = self.color_schemes[config.color_scheme]
        for i, (series_name, values) in enumerate(data.items()):
            fig.add_trace(go.Scatter(
                x=list(range(len(values))),
                y=values,
                mode='lines+markers',
                name=series_name,
                line=dict(color=colors[i % len(colors)])
            ))
        
        fig.update_layout(
            title=config.title,
            xaxis_title=config.x_axis,
            yaxis_title=config.y_axis,
            width=config.width,
            height=config.height,
            showlegend=config.show_legend,
            plot_bgcolor='white',
            paper_bgcolor='white'
        )
        
        if config.show_grid:
            fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
            fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
        
        chart_json = fig.to_json()
        
        return {
            'chart_type': 'line',
            'title': config.title,
            'data': chart_json,
            'config': asdict(config),
            'created_date': datetime.now().isoformat()
        }
    
    def generate_pie_chart(self, data: Dict[str, float], config: ChartConfig) -> Dict[str, Any]:
        """
        Generate pie chart visualization
        
        Args:
            data: Categorical data
            config: Chart configuration
            
        Returns:
            Dictionary containing chart data and metadata
        """
        logger.info(f"Generating pie chart: {config.title}")
        
        labels = list(data.keys())
        values = list(data.values())
        
        fig = go.Figure(data=[go.Pie(
            labels=labels,
            values=values,
            marker_colors=self.color_schemes[config.color_scheme][:len(labels)]
        )])
        
        fig.update_layout(
            title=config.title,
            width=config.width,
            height=config.height,
            showlegend=config.show_legend
        )
        
        chart_json = fig.to_json()
        
        return {
            'chart_type': 'pie',
            'title': config.title,
            'data': chart_json,
            'config': asdict(config),
            'created_date': datetime.now().isoformat()
        }
    
    def generate_heatmap(self, data: List[List[float]], 
                        row_labels: List[str], 
                        col_labels: List[str], 
                        config: ChartConfig) -> Dict[str, Any]:
        """
        Generate heatmap visualization
        
        Args:
            data: Matrix data
            row_labels: Row labels
            col_labels: Column labels
            config: Chart configuration
            
        Returns:
            Dictionary containing chart data and metadata
        """
        logger.info(f"Generating heatmap: {config.title}")
        
        fig = go.Figure(data=go.Heatmap(
            z=data,
            x=col_labels,
            y=row_labels,
            colorscale='Viridis'
        ))
        
        fig.update_layout(
            title=config.title,
            width=config.width,
            height=config.height
        )
        
        chart_json = fig.to_json()
        
        return {
            'chart_type': 'heatmap',
            'title': config.title,
            'data': chart_json,
            'config': asdict(config),
            'created_date': datetime.now().isoformat()
        }
    
    def export_to_excel(self, structured_output: StructuredOutput, filename: str) -> str:
        """
        Export structured output to Excel format
        
        Args:
            structured_output: Structured output to export
            filename: Output filename
            
        Returns:
            Success message
        """
        try:
            with pd.ExcelWriter(filename, engine='openpyxl') as writer:
                # Export summary
                summary_df = pd.DataFrame({
                    'Section': ['Title', 'Summary', 'Created Date'],
                    'Content': [
                        structured_output.title,
                        structured_output.summary,
                        structured_output.created_date
                    ]
                })
                summary_df.to_excel(writer, sheet_name='Summary', index=False)
                
                # Export tables
                for i, table in enumerate(structured_output.tables):
                    table_df = pd.DataFrame(table.data, columns=table.columns)
                    sheet_name = f"Table_{i+1}_{table.title[:20]}"
                    table_df.to_excel(writer, sheet_name=sheet_name, index=False)
                
                # Export insights
                insights_df = pd.DataFrame({
                    'Key Insights': structured_output.key_insights
                })
                insights_df.to_excel(writer, sheet_name='Insights', index=False)
                
                # Export recommendations
                recommendations_df = pd.DataFrame({
                    'Recommendations': structured_output.recommendations
                })
                recommendations_df.to_excel(writer, sheet_name='Recommendations', index=False)
            
            return f"Structured output exported to {filename}"
        except Exception as e:
            return f"Export failed: {str(e)}"
    
    def export_to_json(self, structured_output: StructuredOutput, filename: str) -> str:
        """
        Export structured output to JSON format
        
        Args:
            structured_output: Structured output to export
            filename: Output filename
            
        Returns:
            Success message
        """
        try:
            # Convert to dictionary
            output_dict = asdict(structured_output)
            
            with open(filename, 'w') as f:
                json.dump(output_dict, f, indent=2, default=str)
            
            return f"Structured output exported to {filename}"
        except Exception as e:
            return f"Export failed: {str(e)}"
    
    def _extract_title(self, research_data: Dict[str, Any]) -> str:
        """Extract title from research data"""
        if 'topic' in research_data:
            return f"Research Analysis: {research_data['topic']}"
        elif 'industry' in research_data:
            return f"Industry Analysis: {research_data['industry']}"
        else:
            return "Research Analysis Report"
    
    def _generate_summary(self, research_data: Dict[str, Any]) -> str:
        """Generate executive summary from research data"""
        summary_parts = []
        
        if 'topic' in research_data:
            summary_parts.append(f"This analysis examines {research_data['topic']}.")
        
        if 'competitors' in research_data:
            competitor_count = len(research_data['competitors'])
            summary_parts.append(f"Analysis covers {competitor_count} key competitors.")
        
        if 'trends' in research_data:
            trend_count = len(research_data['trends'])
            summary_parts.append(f"Identified {trend_count} significant trends.")
        
        if 'market_share' in research_data:
            summary_parts.append("Market share analysis reveals competitive positioning.")
        
        return " ".join(summary_parts) if summary_parts else "Comprehensive research analysis completed."
    
    def _create_data_tables(self, research_data: Dict[str, Any]) -> List[DataTable]:
        """Create data tables from research data"""
        tables = []
        
        # Create competitor comparison table
        if 'competitors' in research_data:
            competitor_table = self.create_comparison_table(
                research_data['competitors'],
                ['name', 'market_share', 'strengths']
            )
            tables.append(competitor_table)
        
        # Create market share table
        if 'market_share' in research_data:
            market_share_data = [
                {'Company': company, 'Market Share (%)': share}
                for company, share in research_data['market_share'].items()
            ]
            market_share_table = self.create_comparison_table(
                market_share_data,
                ['Company', 'Market Share (%)']
            )
            tables.append(market_share_table)
        
        # Create trend analysis table
        if 'trends' in research_data:
            trend_table = self.create_trend_analysis_table(research_data['trends'])
            tables.append(trend_table)
        
        return tables
    
    def _generate_charts(self, research_data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate charts from research data"""
        charts = []
        
        # Generate market share pie chart
        if 'market_share' in research_data:
            config = ChartConfig(
                chart_type='pie',
                title='Market Share Distribution',
                x_axis='',
                y_axis='',
                color_scheme='business',
                width=600,
                height=400,
                show_legend=True,
                show_grid=False
            )
            pie_chart = self.generate_pie_chart(research_data['market_share'], config)
            charts.append(pie_chart)
        
        # Generate trend growth bar chart
        if 'trends' in research_data:
            trend_growth = {
                trend['name']: trend.get('growth_rate', 0)
                for trend in research_data['trends']
            }
            config = ChartConfig(
                chart_type='bar',
                title='Trend Growth Rates',
                x_axis='Trends',
                y_axis='Growth Rate (%)',
                color_scheme='tech',
                width=800,
                height=500,
                show_legend=False,
                show_grid=True
            )
            bar_chart = self.generate_bar_chart(trend_growth, config)
            charts.append(bar_chart)
        
        return charts
    
    def _extract_key_insights(self, research_data: Dict[str, Any]) -> List[str]:
        """Extract key insights from research data"""
        insights = []
        
        if 'market_share' in research_data:
            max_share_company = max(research_data['market_share'], 
                                  key=research_data['market_share'].get)
            insights.append(f"{max_share_company} leads the market with {research_data['market_share'][max_share_company]}% share.")
        
        if 'trends' in research_data:
            high_growth_trends = [t for t in research_data['trends'] if t.get('growth_rate', 0) > 30]
            insights.append(f"{len(high_growth_trends)} trends show high growth potential (>30%).")
        
        if 'competitors' in research_data:
            insights.append(f"Market is highly competitive with {len(research_data['competitors'])} major players.")
        
        return insights
    
    def _generate_recommendations(self, research_data: Dict[str, Any]) -> List[str]:
        """Generate strategic recommendations"""
        recommendations = [
            "Monitor emerging trends for early opportunity identification",
            "Develop competitive differentiation strategies",
            "Focus on high-growth market segments",
            "Strengthen market positioning through innovation"
        ]
        
        if 'trends' in research_data:
            early_trends = [t for t in research_data['trends'] if t.get('adoption_level') in ['innovator', 'early_adopter']]
            if early_trends:
                recommendations.append(f"Consider early investment in {len(early_trends)} emerging trends.")
        
        return recommendations
    
    def _collect_sources(self, research_data: Dict[str, Any]) -> List[str]:
        """Collect and deduplicate sources"""
        sources = set()
        
        # Extract sources from various data structures
        if 'sources' in research_data:
            sources.update(research_data['sources'])
        
        if 'competitors' in research_data:
            for competitor in research_data['competitors']:
                if 'sources' in competitor:
                    sources.update(competitor['sources'])
        
        return list(sources)
    
    def _create_metadata(self, research_data: Dict[str, Any], output_type: str) -> Dict[str, Any]:
        """Create metadata for the structured output"""
        metadata = {
            'output_type': output_type,
            'analysis_date': datetime.now().isoformat(),
            'data_sources_count': len(self._collect_sources(research_data)),
            'tables_count': len(self._create_data_tables(research_data)),
            'charts_count': len(self._generate_charts(research_data))
        }
        
        return metadata
